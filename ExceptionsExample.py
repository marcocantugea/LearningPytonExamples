

def get_division(valor1, valor2):
    return valor1 / valor2

try:
    # print(get_name_from_input(input("this is a error")))
    print(get_division(345, 0))
except ZeroDivisionError:
    print("Division invalida, numero no se puede divir entre 0")
except ValueError:
    print("Error ")



