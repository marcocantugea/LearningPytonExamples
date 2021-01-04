# aqui se define el modulo de random
import random

# genera un numero aleatorio del 0 al 1
for i in range(3):
    print(random.random())

print("")
# genera un numero aleatrio int definido
for e in range(3):
    print(random.randint(1,10))

# selecciona un item aleatorio de la lista
usuarios = ["Marco", "Meme", "Beto"]
sorteo= random.choice(usuarios)
print(sorteo)