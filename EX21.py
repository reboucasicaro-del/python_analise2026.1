s = float(input("Digite o Salário => "))
f1 = 7.5/100
f2 = 27/100
if s <= 5000:
    print(f"O salário é de R$ {s}, não incide imposto")
elif s <= 8000:
    print(f"O salário é de R$ {s}, o desconto do IR é R$ {s*f1}, logo o valor liquido é de R$ {s-(s*f1)}")
else:
    print(f"O salário é de R$ {s}, o desconto do IR é R$ {s*f2}, logo o valor liquido é de R$ {s-(s*f2)}")
print("teste git")

#if s <= 5000:
    #imposto = 0
#elif s <= 8000:
    #imposto = s * 0.075
#else
    #imposto = s * 0.27
#salfinal = s - imposto
#print(f"Salário - {s}, imposto - {imposto}, Salário líquido {salfinal}")

#### teste



