# crie uma função que receba o lado de um quadrado
# e retorne o valo de sua área (A=lado^2) >>> a = l ** 2
def lado(x):
    l = x ** 2
    return l
v=int(input("Digite o valor do lado => "))
y=lado(v)
print(f"A área do quadrado com um lado de tamanho {v} é {y}")