import os

#funcion para limpiar pantalla
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#juego de adivinanza
# El usuario tiene que adivinar el numero que se defina al principio

# Setear el numero adivinar
print("Juego de adivinar el numero")
print("Seleccione el numero para el jugador que adivinara el numero")
numero_adivinar = input("Seleccione numero a divinar entre 1 al 10: ")

# valida que el valor sea numerico
while not numero_adivinar.isnumeric():
    print("Numero invalido, Intente nuevamente")
    numero_adivinar = input("Seleccione numero a divinar entre 1 al 10: ")

# valida que el valor numerico sea menor que 10
while int(numero_adivinar) > 10:
    print("El numero que selecciono es mayor a 10")
    numero_adivinar = input("Seleccione un numero entre 1 al 10:")

cls()
numero_adivinar_int = int(numero_adivinar)

#Obtenemos los tips de adivinanza
# revisamos si es un numero par para darle el tip si es numero none o par
es_par = False
calc_par = numero_adivinar_int % 2
if calc_par == 0:
    es_par = True

# obtenemos un rango para darle el tip entre que numeros esta
numero_inicio = numero_adivinar_int - 3
numero_fin = numero_adivinar_int + 3
# si pasa de los limites establece 0
if numero_inicio < 0:
    numero_inicio = 0

if numero_fin > 10:
    numero_fin = 10

# Saca la potencia del numero a diviniar para el tip no. 3
pista_potencia_numero_adivinar = numero_adivinar_int ** 3

# primer intento
mensaje_par = "no es numero par"
if es_par:
    mensaje_par="es numero par"

# Primera pregunta para el jugdor que adivinara el numero
intento_uno = input(f"El numero a divinar {mensaje_par} que numero es? :")

while not intento_uno.isnumeric():
    print("Heee no tecleaste un numero.")
    intento_uno = input(f"El numero a divinar {mensaje_par} que numero es? :")

intento_uno_int = int(intento_uno)

if intento_uno==numero_adivinar_int:
    print(f"Adivinaste el numero! ... el numero era : {numero_adivinar_int}")
    exit()
else:
    print("No intenta de nuevo")

# Segunda pregunta para el jugdor que adivinara el numero
intento_dos = input(f"El numero a adivinar esta entre el {numero_inicio} y el {numero_fin}, cual es? :")
while not intento_dos.isnumeric():
    print("Heee no tecleaste un numero.")
    intento_dos = input(f"El numero a adivinar esta entre el {numero_inicio} y el {numero_fin}, cual es? :")

intento_dos_int = int(intento_dos)

if intento_dos_int==numero_adivinar_int:
    print(f"Adivinaste el numero! ... el numero era : {numero_adivinar_int}")
    exit()
else:
    print("Nop, intenta de nuevo")

# Tercera pregunta para el jugdor que adivinara el numero
intento_tres = input(f"El numero a adivinar, su resultado a la 3era potencia es {pista_potencia_numero_adivinar},cual es?: ")
while not intento_tres.isnumeric():
    print("Heee no tecleaste un numero.")
    intento_tres = input(f"El numero a adivinar, su resultado a la 3era potencia es {pista_potencia_numero_adivinar},cual es?: ")

intento_tres_int = int(intento_tres)

if intento_tres_int==numero_adivinar_int:
    print(f"Adivinaste el numero! ... el numero era : {numero_adivinar_int}")
    exit()


print(f"No pudiste adivinar el numero, el numero era : {numero_adivinar_int}")