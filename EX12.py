g = input("Digite M para Masculino ou F para Feminino => ") #.upper()
if g == "M" or g == "m": #verifica a primeira condição
    print("Masculino")
elif g == "F" or g == "f": #verifica a segunda apenas se a primeira for falsa (se não se)
    print("Feminino") 
else: #executa se nenhuma das anteriores for verdadeira
    print("Não Informado")