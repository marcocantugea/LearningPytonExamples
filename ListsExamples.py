
# definicion de arreglos lista

names=['Noely', 'Maley', 'Marco', 'Delia']

#obtiene el ultimo
print(names[-1])

# obtiene los items desde el index 2
print(names[2:])

# obtiene los items desde el index 2 hasta el que se defina
print(names[1:3])

# ejercicio realizar una lista y obtner el el numero mayor de la lista
index=0
lista_numeros=[2,5,7,9,10,23,45,67,89,192,34,5,67,89,7,32,54,65,76]
numero_mayor=0

for numero in lista_numeros:
    for item in lista_numeros:
        if numero>item and numero_mayor<numero:
            numero_mayor=numero

print(f"el numero mayor es : {numero_mayor}")

# tuple son array inmutables o que no se puedan cambiar
# Ejemplo de tuple
tuple_array = (1,2,3,4)
