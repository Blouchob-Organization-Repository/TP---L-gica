tablero = int(input('de que tamaño quieres que sea el tablero '))
lista = []

for i in range (tablero):
    fila = []
    for j in range (tablero): #asi se hacen las listas
        fila.append(0)
    lista.append(fila)

hormigax = tablero // 2 #ordena eje x de hormiga
hormigay = tablero // 2 #ordena eje y de hormiga


direccion = 0
paso = 0

while 0 <= hormigax < tablero and 0 <= hormigay < tablero: #esto es para documentar cada paso
    print("PASO", paso + 1 )
    print('¡¡¡LA HORMIGA SE ESTA MOVIENDO!!!')
    print('- ' * len(lista[hormigax]))
    for i in range(tablero): 
        for j in range (tablero):
            if i == hormigax and j == hormigay:
                print("H", end= ' ') #para poner h donde esta la hormiga
            else:
                print (lista[i][j], end=' ') #para sacar h cuando se va
        print()
    print()
    
# movimiento hormiga
    if lista[hormigax][hormigay] == 0: #para ver en que numero esta parada y que tiene que hacer
        lista[hormigax][hormigay] = 1 #el numero que deja en la celda en la que estuvo
        direccion = (direccion - 1 ) % 4 
    else:
        lista[hormigax][hormigay] = 0 #el numero que deja en la celda en la que estuvr
        direccion = (direccion + 1) % 4

    if direccion == 0:
        hormigax -= 1
    elif direccion == 2:
         hormigax += 1 
    elif direccion == 1:
        hormigay += 1 
    else:
        hormigay -= 1 
    paso += 1
    if 0 > hormigax or hormigax >= tablero and 0 > hormigay or hormigay >= tablero:
        print('¡¡¡¡¡¡LA HORMIGA HA ESCAPADO DEL TABLERO!!!!!!')