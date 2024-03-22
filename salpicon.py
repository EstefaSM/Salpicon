N = int(input("Ingrese la cantidad de frutas para preparar el salpicón: "))

frutas = []
totalCostoSalpicon = 0

for i in range(N):
    idFruta = input("Ingrese el ID de la fruta: ")
    nombreFruta = input("Ingrese el nombre de la fruta: ")
    precioUnitario = float(input("Ingrese el precio unitario de la fruta: "))
    cantidad = int(input("Indícanos cuántas unidades necesitas: "))
    print()
    
    costoFruta = precioUnitario * cantidad
    totalCostoSalpicon += costoFruta
    
    frutas.append((idFruta, nombreFruta, precioUnitario, cantidad, costoFruta))

print()
print("¡DISFRUTA TU SALPICÓN!")
print("\nEl costo total del salpicón es: $", totalCostoSalpicon)

frutasOrdenadas = sorted(frutas, key=lambda x: x[4], reverse=True)
print("\nFrutas ordenadas de mayor a menor costo: ")
for fruta in frutasOrdenadas:
    print(fruta)

frutaMasBarata = min(frutas, key=lambda x: x[2])
print("\nLa fruta más barata es: ")
print(frutaMasBarata)

