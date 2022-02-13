# PokeDexAPI
Given a Pokemon name, returns standard pokemon description along with additional information.

#Installation Instructions
1. Install Python 3.x - https://www.python.org/downloads/
2. Upgrade pip.
   Python is typically installed in below directory.
   From cmd, go to C:\Users\<username>\AppData\Local\Programs\Python\Python310
   Run - python.exe -m pip install --upgrade pip
4. Install requests and flask.
    From cmd, go to C:\Users\<username>\AppData\Local\Programs\Python\Python310
    Run - 'pip install requests'.
    Run - 'pip install flask'.

#Execution Instructions.
1. Download code files to a local directory and extract them.
2. In cmd, navigate to above folder and Run 'py pokedexweb.py'.
3. From browser execute http get such as 
http://localhost:5000/pokemon/ivysaur/
http://localhost:5000/pokemon/mewtwo/
http://localhost:5000/pokemon/bulbasaur/
http://localhost:5000/pokemon/translated/ivysaur/
http://localhost:5000/pokemon/translated/mewtwo/
http://localhost:5000/pokemon/translated/bulbasaur/

#Ideas for Production API.
1. Would create a Pokemon class with the necessary fields forming the object.
2. Better error handling.
3. Authentication as required.
