#variable de texto

mi_variable_Andres="Hola Mundo"
print(mi_variable_Andres)

#lista de numeros 
las_compras= [1,2,3,4]
print(las_compras)

#diccionario 
conjunto = {"clave_1": "valor1", "clave_2": "valor_2", "clave_3": "valor_3"}
print(conjunto)
####################################
# declarar vector de enteros

vectorsaso= [10]*5
print(vectorsaso)
# declarar vector flotantes
pi_vector = [3.14]*5
print(pi_vector)
# declarar diccionarios
diccionario = {"entero": vectorsaso, "flotantes": pi_vector, "complejo": pi_vector}
print(diccionario)

#Cadenas 

cadena_basica = 'Hola, mundo!'

cadena_doble = ["¡Python es poderoso!", "Me gusta aprender"]

###############################3

#data frame 

import pandas as pd
# Crear un DataFrame con los datos de rendimiento en juegos
datos = {
    'Nombre': ['Andres', 'Elena', 'karen', 'Damaris'],
    'Juego 1 (puntos)': [150, 180, 130, 200],
    'Juego 2 (puntos)': [120, 90, 110, 150],
    'Juego 3 (puntos)': [200, 160, 180, 190]
}

df = pd.DataFrame(datos)

# Mostrar el DataFrame
print(df)
