F1 = str(input("digite uma frase"))
invertido = F1.upper() [::-1] 
invertido = invertido.replace(" ", "")
if F1 == invertido:
    print("palíndromo")
else:
    print("não é palíndromo")