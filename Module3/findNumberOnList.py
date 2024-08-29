numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numero_a_encontrar = 5
achou = False
 
for i in range(len(numeros)):
    achou = numeros[i] == numero_a_encontrar
    if achou:
        break
 
if achou:
    print("Elemento encontrado no índice", i)
else:
    print("ausente")