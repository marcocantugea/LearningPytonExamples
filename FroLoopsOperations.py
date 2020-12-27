
for item in 'python':
    print(item)

for nombres in ['Marco', 'Noely','Maley']:
    print(nombres)

for numero in range(1, 51,3):
    print(numero)


prices = [129.34, 183.45, 1923.40, 123.40, 124.49]

total=0.0
for price in prices:
    total+=price

print(f"Total {total}")

# nested loops
# lista de coordenadas

for coordenadaX in range(4):
    for coordenadaY in range(3):
        print(f"coordenadas ({coordenadaX},{coordenadaY})")

