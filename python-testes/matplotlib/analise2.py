import pandas as pd
import matplotlib.pyplot as plt

# cria os dados
dados = {
    'Nome': ['Ana', 'Bruno', 'Carla', 'Daniel'],
    'Idade': [18, 19, 17, 20],
    'Nota': [9.5, 7.8, 8.2, 6.5]
}

df = pd.DataFrame(dados)

# cria um gráfico de barras com os nomes e notas
plt.figure(figsize=(8, 5))  # define o tamanho da figura
plt.bar(df['Nome'], df['Nota'], color='skyblue')  # gráfico de barras
plt.title('Notas dos Alunos')  # título
plt.xlabel('Aluno')            # eixo X
plt.ylabel('Nota')             # eixo Y
plt.ylim(0, 10)                # define o limite do eixo Y
plt.grid(axis='y', linestyle='--', alpha=0.5)  # grade no eixo Y
plt.tight_layout()             # ajuste de layout
plt.show()                     # exibe o gráfico
