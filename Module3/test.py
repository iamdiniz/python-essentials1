print("sem variavel auxiliar")

variable_1 = 1
variable_2 = 2

print(f"variavel 1: {variable_1}, variavel 2: {variable_2}")
 
variable_2 = variable_1
variable_1 = variable_2

print(f"variavel 1: {variable_1}, variabel 2: {variable_2}")

# quando você faz isso, voce perde o valor armazenado na variavel 2
# voce precisa de uma terceira variavel que serve como armazenamento auxiliar!

print("\n com variavel auxiliar...\n")

var1 = 1
var2 = 2

print(f"variavel 1: {var1}, variavel 2: {var2}")

varAuxiliar = var1
var1 = var2
var2 = varAuxiliar

print(f"variavel auxiliar: {varAuxiliar}")
print(f"var1 : {var1}, var2 {var2}")
