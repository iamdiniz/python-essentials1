def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

a = float(input('Digite o primeiro lado\'s comprimento: '))
b = float(input('Entre no segundo lado\'s comprimento: '))
c = float(input('Entre no terceiro lado\'s comprimento: '))

if is_a_triangle(a, b, c):
    print('Sim, pode ser um triângulo.')
else:
    print('Não, não pode ser um triângulo.')

