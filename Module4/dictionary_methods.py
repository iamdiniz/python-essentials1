dictionary = {"cat": "gato", "dog": "cachorro", "horse": "cavalo"}
 
# Exibe chave e valor
for key in dictionary.keys():
    print(key, "->", dictionary[key])
    
print()

# Metodo items
for english, french in dictionary.items():
    print(english, "->", french)

print()

# Mudar valor
dictionary['cat'] = 'mel'
print(dictionary)

print()

# Exibe so os valores
for french in dictionary.values():
    print(french)
 
print()

# Ordena
for key in sorted(dictionary.keys()):
    print(key)

print()

# Adicionar uma chave e valor 'so colocar algo que nao existe no dicionario'
dictionary['livro'] = 'biblia'
print(dictionary)

print()

dictionary.update({"S.O": "Linux"})
print(dictionary)

print()

# Remover um par
del dictionary['dog']
print(dictionary)

print()

# Remove last item
dictionary.popitem()
print(dictionary)