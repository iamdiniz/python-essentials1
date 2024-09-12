# fibonacci é uma sequencia de numeros inteiros. cada numero é a soma de dois numeros anteriores
def fib(number):
    if number < 1:
        return None
    if number < 3:
        return 1
 
    element1 = element2 = 1
    the_sum = 0

    for i in range(3, number + 1):
        the_sum = element1 + element2
        element1, element2 = element2, the_sum
    return the_sum
 
number_user_entered = int(input("How many numbers of fibonacci sequence u wanna se: "))
 
for number in range(1, number_user_entered):  # testando
    print(number, "->", fib(number))
 
