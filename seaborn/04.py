# Import seaborn e matplotlib
import seaborn as sns
import matplotlib.pyplot as plt

# Apply the default theme
sns.set_theme()

# Load an example dataset
tips = sns.load_dataset("tips")

# Renomear as colunas para português
tips.rename(columns={
    'total_bill': 'total_conta',
    'tip': 'gorjeta',
    'size': 'tamanho_mesa',
    'time': 'hora',
    'smoker': 'fumante',
    'sex': 'sexo'  # Adicionando a coluna sexo
}, inplace=True)

# Exibir o dataset tips
print(tips)

# Create a visualization
sns.relplot(
    data=tips,
    x="total_conta", y="gorjeta", col="hora",weights='fumante',
    hue="sexo", style="sexo", size="tamanho_mesa",  # Usar sexo para estilo também
    sizes=(50, 300),  # Define o tamanho dos marcadores
    palette="Set1",  # Paleta de cores com bom contraste
)

# Show the plot
plt.show()