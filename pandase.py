import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Crear un DataFrame
df = pd.DataFrame({'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]})
df = df.rename(columns= {"X": "Columna 1"})

# Mostrar las columnas del DataFrame
print(df.columns)

# Crear un DataFrame aleatorio para mostrar otro ejemplo
da = pd.DataFrame(np.random.randint(400, 500, size=(5,4)))

# Mostrar el DataFrame aleatorio
print(da)

# Gráfico de barras del DataFrame df
df.plot(kind='bar')
plt.title('Gráfico de barras de DataFrame df')
plt.xlabel('Índice')
plt.ylabel('Valores')
plt.show()
    