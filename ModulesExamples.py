#ejemplo de modulos

# para agregar funciones de un archivo de python se usa la siguiente forma
import converters
# para agregar la funcion solamente usamos lo siguiente
from converters import  lbs_to_kg
from utils import find_max
# importando paquetes
import ecommerce.shipping
# tambien se puede hacer de esta manera
from ecommerce import shipping
# de esta manera tambien funciona
from ecommerce.shipping import calculate_shipping

#para llamar la funcion del modulo
print(converters.kg_to_lbs(400))
print(lbs_to_kg(200))

lista_numeros=[1, 3, 4, 5, 6, 7, 8, 12, 23, 34, 45, 56, 86, 35, 78, 90, 64, 32, 84, 67, 8654, 33345, 67654, 3456, 6543, 3456]
print(find_max(lista_numeros))
ecommerce.shipping.calculate_shipping()
shipping.calculate_shipping()
calculate_shipping()