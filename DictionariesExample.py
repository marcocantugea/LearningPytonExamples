# ejemplo para crear un dictionary

customer={
    "name": "Marco Cantu",
    "age": 30,
    "is_verified": True
}
# agrega nueva llave
customer["birthdate"]="20 nov 1981"
print(customer.get("birthdate","no tiene"))

for item,value in customer.items():
    print(item,'->',value)


#obtener solo las llaves

for key in customer.keys():
    print(key)

#obtiene los valores solamente
for value in customer.values():
    print(value)