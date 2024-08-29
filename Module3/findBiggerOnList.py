# my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
# largest = my_list[0] # assumir temporariamente que o primeiro elemento é o maior

# for i in range(1, len(my_list)): # começa no 2 elemento (indice 1)
#     if my_list[i] > largest: # verifica a hipotese em relação aos outros...
#         largest = my_list[i]

# print(largest)

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]
 
for i in my_list: # percorre todos os elementos, sem se preocupar com nada.
    if i > largest:
        largest = i
 
print(largest)
 