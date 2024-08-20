numbers = [1, 2, 3]
print("List content: ", numbers)

# atribuindo valor na posicao 0
numbers[0] = 7
print("New value: ", numbers)

# copiar o elemento do indice 2 para o indice 0
numbers[0] = numbers[2]
print("New value: ", numbers)

# printar o valor no indice x
print("Value in indice 0: ", numbers[0])

# printar o comprimento da lista
print("Length of list: ", len(numbers))

# remover elemento da lista
print("Removing element on indice 0")
del numbers[0]
print("Length of list: ", len(numbers))
print("List complete: ", numbers)

# Indices negativos, -1 é o ultimo elemento na lista
print("Last element on list: ", numbers[-1])

# adicionar elementos com o metodo append e insert
print("Inserindo um elemento no final da lista")
numbers.append(7)
print("List: ", numbers)

print("Inserindo um elemento na posicao desejada (em especifico no comeco da lista)")
numbers.insert(0, 77)
print("List: ", numbers)
