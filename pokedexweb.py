from flask import Flask
import pokedex as pd

app = Flask(__name__)
@app.route('/pokemon/<string:name>/', methods=['GET'])
def pokeDetails(name):
    pokeDetails = pd.getPokemonDetails(name)
    if not pokeDetails:
        pokeDetails = "Not found!"
    return(pokeDetails)

@app.route('/pokemon/translated/<string:name>/', methods=['GET'])
def pokeTranslated(name):
    pokeDetails = pd.getPokemonDetailsWithTranslation(name)
    if not pokeDetails:
        pokeDetails = "Not found!"
    return(pokeDetails)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
