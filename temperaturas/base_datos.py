import pandas as pd
import numpy as np

# Lee el archivo que tiene los datos

temperatures_df = pd.read_csv('./GlobalLandTemperaturesByCountry.csv')

# Coloca todos los paises que hay en la base de datos
print(temperatures_df['Country'].unique())

# Hace un filtro para ver la temperatura desde cierta fecha
filtered_df = temperatures_df[temperatures_df['dt'] >= '1970-01-01']
print(filtered_df)

# Se usa para colocar que la fecha no sea un objeto su no un datetime
filtered_df['year'] = pd.to_datetime(filtered_df['dt'])

print(filtered_df['year'])

# Muestra los años
idx = filtered_df['year'] > pd.to_datetime('1970-01-01')
filtered_df = filtered_df[idx]

print(filtered_df)

df_t_avg = filtered_df