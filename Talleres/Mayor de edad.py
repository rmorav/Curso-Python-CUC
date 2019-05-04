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

V = ["Hola", "mundo", 4, 3, 2, 2, True, ["otro", "arreglo", "dentro"]]
v2 = ["Hola", "mundo"]
v3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]



# mostrar un elemento de un arreglo
print(V[0])
    

# modificar un elemento de un arreglo
v2[1] = "Rafael"

# Eliminar un elemento
v2.remove("Hola")

# eliminar el ultimo elemento
V.pop()


# eliminar un elemento en una posicion
V.pop(4)


# agregar un elemento al final
V.append(5)

# agregar un elemnto en una pisicion determinada
V.insert(1, "rafael")

# borrar elementos
V.clear()


# Posicion de un elemento
V.index("rafael")

# numero de elementos de un arreglo

len(V)

# cuantas veces aparece un elemento en arreglo
V.count(2)

# Ordenar un Arreglo
V.sort()


# acceder a un elemento de un arreglo interno
# forma 1
aux = V[-1]
aux = aux[0]
print(aux)

#forma 2
aux = V[-1][0]
print(aux)


# crear una matriz
m = [[2, 4],[2, 4]]


#Recorrer un vector con un for

V = V[:5]   # recorre el vector desde 0 hasta 4

for x in V[:5]:
    print(x)
    


# trabajo 2
# forma 1
print("Escriba tope de la sumatoria")
t = input()
t = int(t)
aux = 0
for x in range(t+1):
    aux = aux + x
print("la Sumatoria es: ", aux)

# forma 2 (mas agil)

print("Escriba tope de la sumatoria")
t = int(input())
aux = sum(range(t+1))
print("la Sumatoria es: ", aux)


# while

i = 2

while i <= 5:
    print(i)
    i = i + 1
    


# Metodos
    
# Crear un procedimiento (un prodimiento no retorna valor)
def hola_mundo():
    print("Hola Mundo")
   
# invocar un procedimiento
hola_mundo()

# crear una funcion (una funcion si retorna valor)

def elevar_cuadrado(numero=2):
    return numero ** 2

# invocar una funcion
    
elevar_cuadrado(5)



















