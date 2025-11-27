import random
import datetime, timedelta
import numpy as np
import pandas as pd

def dsa_gera_dados_ficticios (num_registro = 600):

    print(f"\iniciando a geração de {num_registro} registro de vendas...")
    produtos = {
    'Laptop gamer' : {'categoria': 'Eletrônicos', 'preco': 7500.00},
    'Mouse vertical' : {'categoria': 'Acessorios', 'preco': 2500.00},
    'Teclado mecanico': {'categoria': 'Acessorios', 'preco': 550.00},
    'Monitor Ultrawide': {'categoria': 'Eletronicos', 'preco': 2800.00},
    'Cadeira Gamer' : {'categoria': 'Moveis', 'preco': 1200.00},
    'Headset 7,1' : {'categoria': 'Acessorios', 'preco': 800.00},
    'Placa de Video' : {'categoria': 'Hardware', '´preco': 4500.00},
    'SSD 1TB': {'categoria': 'Hardware', 'preco': 600.00}
}
    lista_produtos = list (produtos.keys())

    cidades_estados = {
      'São paulo': 'SP', 'Rio de Janeiro': 'RJ', 'Belo horizonte': 'MG',
      'Porto Alegre': 'RS', 'Salvador': 'BA', 'Curitiba': 'PR', 'Fortaleza': 'CE'
 }

    lista_cidades = list (cidades_estados.keys()
 )
    dados_vendas = []
    data_inicial = datetime (2026, 1, 1)

    for i in range(num_registro):   
        produto_nome = random.choice(lista_produtos)
        cidade = random.choice(lista_cidades)
        quantidade = np.random.randint(1, 8)
        data_pedido = data_inicial + timedelta(days = int(i/5), hours = random.randint (0, 23))

    if produto_nome in ['Mouse vertical',' Teclado mecanico']:
        preco_unitario = produtos[produto_nome] ['preco'] * np.random.uniform(0.9, 1.0)
    else:
        preco_unitario = produtos[produto_nome] ['preco'] 

    dados_vendas.append({
    'ID_Pedido' : 1000 + i,
    'Data_Pedido': data_pedido,
    'Nome_Produto': produto_nome,
    'Categoria' : produtos[produto_nome] ['Categoria'],
    'Preco_unitario': round(preco_unitario, 2),
    'Quantidade' : quantidade,
    'ID_Cliente' : np.random.randint (100, 150), 
    'Cidade' : cidade,
    'Estado' : cidades_estados [cidade]  
})    

    print ("Geração de dados concluida.\n")

    return pd.DataFrame(dados_vendas)


