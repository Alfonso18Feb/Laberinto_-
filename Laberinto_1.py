"""Primera parte. Definir función (laberinto).
    Valores de entrada un número entero (medida) para dar la dimensión del laberinto
    y una lista de tuplas (muro) donde están los muros.
    Devuelve la lista de listas que forman el laberinto."""
def laberinto(medida, muro):
    laberinto = []
    #Crea la lista vacía del laberinto
    for i in range(medida):
     #Bucle (for) que añade las filas del laberinto según la (medida) dada.
        fila = []
        #Crea la lista vacía (fila) para añadir las filas del laberinto.
        for j in range(medida):
         #Bucle (for) para seguir las columnas del laberinto.
            if tuple([i, j]) in muros:
             #Condicional (if) para saber si la tupla (i,j) está en la lista (muros).
                fila.append("X")
                #Si está en (muros) escribe una equis ("X").
            else:
                fila.append(" ")
                #Si no está en (muros) escribe un espacio en blanco(" ").
        laberinto.append(fila)
        #Añade la fila al laberinto.
    return laberinto
    #Devuelve la lista de listas del laberinto formado (laberinto).

"""Segunda parte. Definir muros."""
muros = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3)) 
#Escribe las coordenadas con muro en la lista de tuplas (muros).
lab = laberinto(5, muros)   
#Llama a la función (laberinto) con medidas 5x5 y con los (muros).
#Luego recoge lista de listas devuelta por la función en la lista (lab).

"""Tercera parte. Imprimir laberinto."""
for i in lab:
 #Recorre la lista (lab).
    print("".join(i))
    #Imprime cada elemento fila de la lista (lab).