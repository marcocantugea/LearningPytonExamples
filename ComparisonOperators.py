#Para este ejemplo, realizamos un programa en donde si la temperatura
# Es mayor a 30 despliega mensaje de que es un dia soleado
# Si es menor a 10 es un dia frio
# de lo contrario despliega que es un dia agradable

temperatura=30

if temperatura>=30:
    print("Es un dia Soleado")
elif temperatura<10 and temperatura>=1:
    print("Hace mucho frio este dia")
elif temperatura<=0:
    print("Esta refrio el dia")
else:
    print("Es un dia agradable")