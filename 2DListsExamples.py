# ejemplo de array bidimencional

matrix=[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [5,3,5],
    [5,6,7]
]

print(matrix[0][1])


#agregar nuevo objeto
matrix.append([10,11,12])

#agregar objeto en medio
matrix.insert(2,[13,14,15])
matrix.insert(2,["remover","remover","remover"])

for row in matrix:
    for item in row:
        print(item)

#elimina elemento en el array
matrix[2].remove("remover")

print(matrix[2])

# elminina el ultimo elemento del arreglo
matrix.pop()
for row in matrix:
    for item in row:
        print(item)

# busca objeto en matrix
print(matrix.index([4,5,6]))
print([1,2,3] in matrix)

#funcion de contar
contar=0
for row in matrix:
    contar+=row.count(5)

print(contar)

#ordenamiento de arrays
for row in matrix:
    row.sort()

print(matrix)

#ordenamiento de array en inversa

for row in matrix:
    row.reverse()

print(matrix)

# copiar el contenido de un array a otro
matrix_segunda= matrix.copy()
matrix_segunda[0].clear()

print(matrix)
print(matrix_segunda)
