import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar los datos
df = pd.read_csv('Mall_Customers.csv')

# Resumen estadístico
print(df.describe())

# Histograma de las variables
df.hist(bins=50, figsize=(20, 15))
plt.show()

# Boxplot para identificar valores atípicos
sns.boxplot(data=df)
plt.show()

# Mapa de calor de la matriz de correlación
corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.show()