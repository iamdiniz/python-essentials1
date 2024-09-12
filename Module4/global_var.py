def func():
    global var
    var = 5
    print(f"Eu consigo pegar essa variavel aqui fora do espoco? {var}")

func() # aqui ela valhe 5
var = 10 # aqui valhe 10
print(var)