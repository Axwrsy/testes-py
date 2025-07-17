import pandas as pd

# lê o arquivo CSV se nao tiver o arqv .csv pode criar diretamente no cdg
#df = pd.read_csv('examplo.csv')

dados = {
    'Nome': ['Ana', 'Bruno', 'Carla', 'Daniel'],
    'Idade': [18, 19, 17, 20],
    'Nota': [9.5, 7.8, 8.2, 6.5]
}

df = pd.DataFrame(dados)
print(df)


# mostra as 5 primeiras linhas
print("Tabela completa:")
print(df)

# mostra estatísticas (média, min, max, etc.)
print("\nEstatísticas:")
print(df.describe())

# filtra alunos com nota maior que 8
print("\nAlunos com nota acima de 8:")
print(df[df['Nota'] > 8])
