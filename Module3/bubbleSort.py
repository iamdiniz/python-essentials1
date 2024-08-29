my_list = [8, 10, 6, 2, 4]  # Lista para ordenar
swapped = True  # É um pouco falso, precisamos dele para entrar no loop while.
 
while swapped:
    swapped = False  # nenhuma troca até agora
    for i in range(len(my_list) - 1): # - 1 para ficar no comprimento certo da lista
        if my_list[i] > my_list[i + 1]: # se o primeiro for maior que o segundo
            swapped = True  # uma troca ocorreu!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i] # atribuição múltipla
 
print(my_list)

# Atribuição múltipla permite trocar os valores de duas variáveis sem a necessidade de uma variável temporária intermediária.
# nesse código: my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
# Primeiro, o Python avalia tudo o que está à direita do `=`. 
# o lado direito é `my_list[i + 1], my_list[i]`.
# depois o python atribui esses valores aos elementos do lado esquerdo do =. no caso em my_list[i], my_list[i + 1]
# o valor que estava em my_list[i + 1] vai para my_list[i]
# e o valor que estava em my_list[i] vai para my_list[i + 1].

# leitura
# avalia pra mim esse lado direito... se a condicao for verdadeira...
# atribui ao lado esquerdo
