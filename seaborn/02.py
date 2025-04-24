# Import seaborn e matplotlib
import seaborn as sns
import matplotlib.pyplot as plt

# Apply the default theme
sns.set_theme()

# Load an example dataset
tips = sns.load_dataset("tips")

# Exibir o dataset tips
print(tips)

# Create a visualization
sns.relplot(
    data=tips,
    x="total_bill", y="tip", col="time",
    hue="smoker", style="smoker", size="size",
    sizes=(50, 300),  # Define o tamanho dos marcadores
    palette="viridis",  # Define a paleta de cores
)

# Show the plot
plt.show()