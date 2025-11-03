import pandas as pd
import os

dataset = 'dataset.csv' 

try: 
    df = pd.read_csv (dataset)

    print ("Datafram criado com sucesso")
    print (df.head())
    
except FileNotFoundError:
    print (f"Erro: o arquivo {dataset}, não foi encontrado.")
    print (f"Diretorio atual de execução {os.getcwd()}")