tablero = int(input('de que tamaño quieres que sea el tablero '))
lista = []

for i in range (tablero):
    fila = []
    for j in range (tablero): #asi se hacen las listas
        valor = (i + j) % 2 
        fila.append(valor)
    lista.append(fila)
#ordenar a la hormiga en el medio
if tablero % 2 != 0:
    hormigax = tablero // 2
    hormigay = tablero // 2
else:
    hormigax = tablero // 3
    hormigay = tablero // 3
#mostrar hormiga
for i in range (tablero):
    for j in range (tablero):
        if i == hormigax and j == hormigay:
            print("H", end= ' ')
        else:
            print (lista[i][j], end=' ')
    print()
# movimiento hormiga
