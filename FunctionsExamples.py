# ejemplo de crear funciones

def function_mensaje_bienvenida():
    print('Bienvenido al sistema')


def function_mensaje_bienvenida_usuario(name):
    print(f'Bienvenido al sistema {name}')


function_mensaje_bienvenida()
function_mensaje_bienvenida_usuario('Marco Cantu')


# ejemplo de asignatura de argumentos y regreso de valores de la funcion
def function_suma_x_y(x, y):
    return x * y

print(function_suma_x_y(y=2, x=4))
print(function_suma_x_y(x=4, y=7))

# todas las funciones de python regresa None

