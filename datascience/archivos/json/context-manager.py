#https://www.geeksforgeeks.org/counting-the-frequencies-in-a-list-using-dictionary-in-python/

import json

with open('camaraFederaleditado.json', 'r') as camara:
    camara = json.load(camara)
    deputados = camara['deputados']['deputado']
    partidos = camara['deputados']['detalhes']

partidosArr = []

#guarda todos los partidos en partidosArr

for partido in deputados:
     partidosArr.append( partido['partido'] )


#cuenta las ocurrencias de cada partido en partidosArr
#itera por partidosArr y busca en el diccionario peso_partidos, si no encuentra la key, la crea con valor 1, si está presente, incrementa el valor
peso_partidos = {}

for partido in partidosArr:
    if partido in peso_partidos:
        
        v = peso_partidos.get( partido )
        v += 1
        peso_partidos.update( { partido : v } )

    else:
        peso_partidos.update( { partido : 1 } )

#print(peso_partidos)

partidos.update( {"peso partidos" : peso_partidos} )


camara['deputados']['detalhes'].update( partidos )
up = camara

with open('camaraFederalFinal.json', 'w+') as camara:
    
    json.dump( up, camara, indent=4 )










'''
with open('test.json', 'r') as file:
    file = json.load(file)
    el = { "nested2" : "cosas"}
    file.update(el)

with open('test.json', 'w+') as f:
    json.dump(file, f, indent=4)

i = {
    "element" : "some element",
    "items" : [
        1, "true", "thing"
    ],
    "nested": {
        "dfadf": "1080",
        "adfgf": "4"
    }
}


d = json.dumps(i, indent=4)
print(d)

d = json.loads(d)
print(d)

with open("test.json", 'w') as file:
  json.dump(i, file, indent=4)
'''


