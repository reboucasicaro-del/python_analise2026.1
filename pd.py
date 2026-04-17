import pandas as pd
df = pd.read_csv('ClassicDisco.csv')
#print(df.to_string()) >>> imprimi todos os dados da planilha
#print(df.head()) >>>  #exibe as 5 primeiras linhas
#print(df.tail(10)) >>> imprimi as 5 ultimas linha do arquivo
print(df[10:15]) #>>> entre [xx:xx] mostra o intervalo especificado 
#print(df.shape) #indica o número de colunas e linhas do arquivo