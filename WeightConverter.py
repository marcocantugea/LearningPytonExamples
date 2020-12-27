# Programa para convertir de Kilos a libras
import math
peso=input("Peso:")

# if not peso.isnumeric():
#    print("Peso invalido!")
#    exit(1)

try:
    float(peso)
except ValueError:
    print("Peso invalido!")
    exit(1)

unidad_medida=input("Seleccione (L) para Lbs o (K) para Kg:")


if unidad_medida.upper() != "L" and unidad_medida.upper() != "K":
    unidad_medida ="K"


if unidad_medida.upper()=="K":
    resultado=  float(peso) * 2.20462
    print(f"El peso en libras es de {round(resultado,4)} Lbs.")
    exit()

if unidad_medida.upper()=="L":
    resultado = float(peso) / 2.20462
    print(f"El peso en Kilosgramos es de {round(resultado,4)} Kg.")
    exit()