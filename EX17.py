n1 = int(input("Digite o valor N1 => ")) #poderia aplicar float
n2 = int(input("Digite o valor N2 => "))
n3 = int(input("Digite o valor N3 => "))
if n1 > n2 and n1 > n3:
    print("N1 é o maior valor")
elif n2 > n3 and n2 > n1: #outra solução n2 > n3
    print("N2 é o maior valor")
elif n3 > n2 and n3 > n1:
    print("N3 é o maio valor")
else: #outro elif também resolveria
    print("Iguais")




