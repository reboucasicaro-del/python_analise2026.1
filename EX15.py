i = int(input("Digite a sua idade => "))
g = input("Digite M para Masculino ou F para Feminino => ") #.upper()
if i >= 18 and g == "M" or g == "m":
    print("Apto ao alistamento")
else:
    print("Não apto(a)")