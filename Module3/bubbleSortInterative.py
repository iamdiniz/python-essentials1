import time

numbers = []
trocou = True
num = int(input("Quantos elementos você deseja embaralhar? "))

for i in range(num):
 valor = int(input("Entre com a lista de elementos:"))
 numbers.append(valor)

while trocou:
    trocou = False
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            trocou = True
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

print("Ordenando...")
time.sleep(3)
print("Lista ordenada: ")
print(numbers)
