n = input("Insira o seu nome => ")
an = int(input("Informe o ano do seu nascimento => "))
aa = int(input("Informe o ano atual => "))
i = aa - an
if i >= 18:
    print(f"{n} é maior de idade")
else:
    print(f"{n} é menor de idade")