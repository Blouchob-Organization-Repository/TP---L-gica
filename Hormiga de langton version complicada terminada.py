tablero = int(input('de que tamaño quieres que sea el tablero '))
lista = []

for i in range (tablero):
    fila = []
    for j in range (tablero): #asi se hacen las listas
        fila.append(0)
    lista.append(fila)
#ordenar a la hormiga en el medio
hormigax = tablero // 2
hormigay = tablero // 2

#mostrar hormiga
for i in range (tablero):
    for j in range (tablero):
        if i == hormigax and j == hormigay:
            print("H", end= ' ')
        else:
            print (lista[i][j], end=' ')
    print()
# movimiento hormiga
direccion = 0
for i in range (10): #iteraciones
    if lista[hormigax][hormigay] == 0:
        lista[hormigax][hormigay] == 1
        direccion = (direccion - 1 ) % 4 
    else:
        lista[hormigax][hormigay] == 0
        direccion = (direccion + 1) % 4
if direccion == 0:
    hormigax = hormigax - 1
elif direccion == 2:
    hormigax = hormigax + 1 
elif direccion == 1:
    hormigay = hormigay - 1
else:
    hormigay = hormigay + 1 


print (lista[i][j], end=' ')
print()