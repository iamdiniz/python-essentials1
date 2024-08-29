lista1 = [1]
lista2 = lista1[:] # lista 2 recebe o conteudo de lista1
lista1[0] = 2 # lista 1 na posicao 0 recebe 2
print(lista2)

lista_fatiada = [1, 2, 3, 4, 5]
nova_lista = lista_fatiada[1:3] # comece no indice 1 e va até o 3, mas não o inclua
print(nova_lista)

