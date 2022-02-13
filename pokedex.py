import argparse
import requests
import json

def getSoapResponse(url,parameters=None):
#    print('getSoapResponse url = {}, parameters = {}'.format(url,parameters))
    response = None
    retJson = None
    if parameters:
        response = requests.get(url,params=parameters)
    else:
        response = requests.get(url)
    if response.status_code == 200:
        retJson = response.json()
    elif response.status_code == 404:
        print('Page Not Found')
    elif response.status_code == 429:
        print('Too Many API Calls')
    else:
        print(response)
    return retJson

def getTranslation(type, textToTrans):
#    print('doing {} translation'.format(type))
    query = {'text':textToTrans}
    url = "https://api.funtranslations.com/translate/{}.json".format(type)
    ret = getSoapResponse(url,query)    
    transText = textToTrans
    if ret:
        transText = ret["contents"]["translated"]
    return transText

def getPokemonSpecies(pokeName):
#    print('Getting pokemonSpecies of {}'.format(pokeName))
    url = "https://pokeapi.co/api/v2/pokemon-species/{}/".format(pokeName)
    retJson = getSoapResponse(url)
    if not retJson:
        print('Unable to get species. Returning None.')
        return(None)
    return retJson

def getPokemon(pokeName):
#    print('Getting pokemon of {}'.format(pokeName))
    url = "https://pokeapi.co/api/v2/pokemon/{}/".format(pokeName)
    retJson = getSoapResponse(url)
    if not retJson:
        print('Unable to get pokeObj. Returning None.')
        return(None)
        #exit(0)
    return retJson

def getPokemonDetails(pokeName):
#    print('GettingPokemonDetails')
    pokeName = pokeName.lower()
    pokeObj = getPokemon(pokeName)
    if not pokeObj:
        return(None)
    name = pokeObj["name"]
      
    description = None
    species = getPokemonSpecies(pokeName)
        
    fte = species["flavor_text_entries"]
    if fte:
        for ft in fte:
            if ft["language"]["name"] == 'en' and ft["version"]["url"] == 'https://pokeapi.co/api/v2/version/1/':
                description = ft["flavor_text"].replace('\n',' ').replace('\f',' ')
    else:
        print('No flavor text entries')

    habitat = species["habitat"]["name"]
    is_legendary = species["is_legendary"]
    
    json_dump = None
    if name and description and habitat and is_legendary is not None:
        data_set = {"name":name,"description":description,"habitat":habitat,"is_legendary":is_legendary}
        json_dump = json.dumps(data_set)
        
    return(json_dump)

def getPokemonDetailsWithTranslation(pokeName):
#    print('getPokemonDetailsWithTranslation')
    pokeName = pokeName.lower()
    pokemonDetails = getPokemonDetails(pokeName)
    pokeDetails = None
    if pokemonDetails:
        pokeDetails = json.loads(pokemonDetails)
        if not pokeDetails:
            print('Unable to convert pokeDetails to json. Returning None.')
            return(None)
            #exit(0)
    else:
        print('Unable to get pokemon details. Returning None.')
        return(None)
        #exit(0)    
        
    description = pokeDetails["description"]
    translated = None
    if pokeDetails["habitat"] == 'cave' or pokeDetails["is_legendary"] == True:
        translated = getTranslation('yoda',description)
    else:
        translated = getTranslation('shakespeare',description)
    if translated:
        pokeDetails["description"] = translated

    data_set = {"name":pokeDetails["name"],"description":pokeDetails["description"],"habitat":pokeDetails["habitat"],"is_legendary":pokeDetails["is_legendary"]}
    json_dump = json.dumps(data_set)

    return(json_dump)

def main():
    parser = argparse.ArgumentParser(
                description = 'Pokedex API'
                )
    parser.add_argument(
            'pokeName', type = str, help = 'Name of the pokemon character')
    parser.add_argument(
            'fun', type = str, help = 'Include Fun Translation? True/False')
    try:
        args = parser.parse_args()
    except Exception:
        parser.print_help()
        exit(0)
    
    pokeName = args.pokeName
    retJson = None
    if args.fun.upper() == 'TRUE':
        retJson = getPokemonDetailsWithTranslation(pokeName)
    elif args.fun.upper() == 'FALSE':
        retJson = getPokemonDetails(pokeName)
    else:
        parser.print_help()
    print(retJson)

if __name__ == '__main__':
    main()
