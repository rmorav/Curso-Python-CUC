# -*- coding: utf-8 -*-
"""
Created on Sat May  4 09:08:01 2019

@author: android
"""
print("Digite su edad")
edad = input()
edad = int(edad)
"""if edad >= 18:
    print("ud es mayor de edad")
else:
    print("ud es menor de edad")    
"""

# si de linea con sino
print("ud es mayor de edad") if edad >= 18 else print("ud es menor de edad") 

# si de linea sin sino
if edad >= 18: print("ud es mayor de edad")


# Arrays

V = ["Hola", "mundo", 4, 3, 2, True, ["otro", "arreglo", "dentro"]]
v2 = ["Hola", "mundo"]
v3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]



# mostrar un elemento de un arreglo
print(V[0])
    

# modificar un elemento de un arreglo
v2[1] = "Rafael"

# Eliminar un elemento 
v2.remove("Hola")

