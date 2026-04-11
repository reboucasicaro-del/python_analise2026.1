# desenvolva um código python que imprima 
# na tela os números de 15 a 30 e diga
# cada um deles se é par ou impar
for i in range(15,31):
    r=i % 2 #função resto
    if r == 0:
        print(f"{i} - é par")
    else:
        print(f"{i} - é impar")