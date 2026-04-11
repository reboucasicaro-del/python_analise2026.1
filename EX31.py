# desenvolva um código python que leia 10 médias de aluno,
# e ao momento que está lendo mostre se este aluno esta 
# aprovado se for maior que 5 ou em recuperação

for i in range(0,10):
    m = float(input(f"Digite a média do aluno => "))
    if m > 5:
        print("Aprovado")
    else:
        print("Em Recuperação")