import pandas as pd
df = pd.read_csv('ClassicDisco.csv')
#print(df.to_string()) 
#print(df.head()) >>>  #exibe as 5 primeiras linhas
print(df.tail(10))