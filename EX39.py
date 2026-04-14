# desevolva um código python em que o usuário digite um numero 
# e irá mostrar a tabuada deste número usando while
x = int(input("Digite o número => ")) 
i = 0 #varíavel de inicialização
while i <= 10: #como se le: enquanto i for <= 10
    r = x*i
    print(f"{x} x {i} = {r}")
    i = i + 1 #de quantos em quantos ele vai repetir

