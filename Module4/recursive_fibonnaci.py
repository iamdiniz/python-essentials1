def fib(number):
    if number < 1:
        return None
    if number < 3:
        return 1
    return fib(number - 1) + fib(number - 2)
 
print(fib(10))

# lembre-se, a recursão há desvantagens como: alto consumo de mémoria e se não prestar 
# atenção pode causar um loop infinito