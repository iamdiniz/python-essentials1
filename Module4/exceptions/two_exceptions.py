valor = 1
try:
    value = int (input('Insira um número natural: ')) 
    print('O recíproco de', valor, 'é', 1 / value) 
except ValueError: 
    print('Não sei o que fazer.')
except ZeroDivisionError:
    print('A divisão por zero não é permitida em nosso Universo.') 
