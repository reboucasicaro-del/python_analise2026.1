# imc = peso / (altura * altura)
# float = transforma texto em número real, ou seja, que possua casas decimais
# int = tranforma texto em número inteiro
p = float(input("Digite o seu peso => "))
a = float(input("Digite sua altura => "))
imc = p/(a*a)
print(f"O imc do individuo é de {imc}")