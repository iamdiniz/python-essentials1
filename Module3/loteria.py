numeros_sorteados = [5, 11, 9, 42, 3, 49]
apostas = [3, 7, 11, 42, 34, 49]
acertos = 0
 
for number in apostas:
    if number in numeros_sorteados:
        acertos += 1
 
print(acertos)
 
