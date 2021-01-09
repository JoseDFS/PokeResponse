import requests
import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=.\SQLEXPRESS;'
                      'Database=POKEDEX;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
response = requests.get(
    'https://pokeapi.co/api/v2/pokemon/1'
    )

json_response = response.json()
print(json_response['name'],json_response['id'],json_response['height'],json_response['weight'])
#cursor.execute("INSERT INTO POKEDEX.dbo.Pokemon (id,name,height,weight) values ('"+str(json_response['id'])+"','"+json_response['name']+"',"+str(json_response['height'])+","+str(json_response['weight'])+")")
#cursor.commit()
i =1
response = requests.get(
    'https://pokeapi.co/api/v2/pokemon/'+str(i)
    )
while(response):
    json_response = response.json()
    print(json_response['name'],json_response['id'],json_response['height'],json_response['weight'])
    #cursor.execute("INSERT INTO POKEDEX.dbo.Pokemon (id,name,height,weight) values ("+str(json_response['id'])+",'"+json_response['name']+"',"+str(json_response['height'])+","+str(json_response['weight'])+")")
    #cursor.commit()
    i+=1
    response = requests.get(
    'https://pokeapi.co/api/v2/pokemon/'+str(i)
    )
    
i=1
response = requests.get(
    'https://pokeapi.co/api/v2/type/'+str(i)
    )
while(response):
    json_response = response.json()
    print(json_response['name'],json_response['id'])
    cursor.execute("INSERT INTO POKEDEX.dbo.Tipo (id,name) values ("+str(json_response['id'])+",'"+json_response['name']+"')")
    cursor.commit()

    pokemons = json_response['pokemon']
    print(pokemons[0]['pokemon']['url'])
    for pokemon in pokemons:
        response = requests.get(
            pokemon['pokemon']['url']
        )
        pokemon_response=response.json()
        cursor.execute("INSERT INTO POKEDEX.dbo.PokemonXTipo (pokemonId,tipoId) values ("+str(pokemon_response['id'])+","+str(json_response['id'])+")")
        cursor.commit()
        
    
    i+=1

    response = requests.get(
    'https://pokeapi.co/api/v2/type/'+str(i)
    )
conn.close()
