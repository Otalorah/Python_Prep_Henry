#3) Crear un archivo a partir de los datos presentes en el diccionario provisto. 
#El cual debe contener en la primera fila el nombre de las claves y luego cada línea los elementos
#i-ésimos de las listas de valores contiguos y separados por coma ','. Este archivo debe llamarse 
#clase09_ej3.csv

montañas = {'nombre':[  'Everest','K2','Kanchenjunga','Lhotse','Makalu',
                        'Cho Oyu','Dhaulagiri','Manaslu','Nanga Parbat','Annapurna I'],
            'orden':[1,2,3,4,5,6,7,8,9,10],
            'cordillera':['Himalaya','Karakórum','Himalaya','Himalaya','Himalaya'
                        ,'Himalaya','Himalaya','Himalaya','Karakórum','Himalaya'],
            'pais': ['Nepal','Pakistán','Nepal','Nepal','Nepal','Nepal','Nepal','Nepal',
                    'Pakistán','Nepal'],
            'altura':[8849,8611,8586,8516,8485,8188,8167,8163,8125,8091]}

elementos = list(zip( montañas["nombre"],montañas["orden"],montañas["cordillera"],montañas["pais"],montañas["altura"]))
with open("M10_manejodearchivos\\archivo_montañas.csv","w",encoding="utf-8") as archivo:
    for clave in montañas.keys():
        if clave == "altura": 
            archivo.write(clave)
            continue
        archivo.write(clave+",")
    for tupla in elementos:
        archivo.write("\n")
        for elemento in tupla:
            if elemento == tupla[4]: 
                archivo.write(str(elemento))
                continue
            archivo.write(str(elemento)+",")
        