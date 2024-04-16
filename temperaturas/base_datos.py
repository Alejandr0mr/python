import pandas as pd
import numpy as np

# # Lee el archivo que tiene los datos
# temperatures_df = pd.read_csv('temperaturas/GlobalLandTemperaturesByCountry.csv')


# # Coloca todos los paises que hay en la base de datos
# print(temperatures_df['Country'].unique())

# # Hace un filtro para ver la temperatura desde cierta fecha
# filtered_df = temperatures_df[temperatures_df['dt'] >= '1970-01-01']
# print(filtered_df)

# # Se usa para colocar que la fecha no sea un objeto su no un datetime
# filtered_df['year'] = pd.to_datetime(filtered_df['dt'])
# print(filtered_df['year'])

# # Muestra los años
# idx = filtered_df['year'] > pd.to_datetime('1970-01-01')
# filtered_df = filtered_df[idx]

# print(filtered_df)

# df_t_avg = filtered_df


import pandas as pd
import matplotlib.pyplot as plt
# nba
nba_df = pd.read_csv('temperaturas/nba_all_seasons.csv')

# Imprime los nombres únicos de los jugadores
print(nba_df['player_name'].unique())

#-------------
sorted_df = nba_df.sort_values(by='player_weight', ascending=False)
# Selecciona los primeros jugadores con mayor peso
jugadores_mayor_peso = sorted_df.head()
# Imprime los jugadores con mayor peso
print("\nJugadores con mayor peso:")
print(jugadores_mayor_peso[['player_name', 'player_weight']])
jugadores_mayor_peso['player_weight'].plot(kind="bar", title="Jugadores con mayor peso")
plt.xlabel("Nombre del jugador")
plt.ylabel("Peso")
plt.xticks(range(len(jugadores_mayor_peso)), jugadores_mayor_peso['player_name'])
plt.show()



#-------------
# Ordena el DataFrame por edad en orden ascendente
sorted_df = nba_df.sort_values(by='age')

# Selecciona los primeros jugadores más jóvenes
jugadores_mas_jovenes = sorted_df.head()

# Imprime los nombres de los jugadores más jóvenes
print("\nJugadores más jóvenes:")
print(jugadores_mas_jovenes[['player_name', 'age']])

#-------------
# Encuentra el jugador con el mayor puntaje entre los jugadores más jóvenes
jugador_max_pts = jugadores_mas_jovenes.loc[jugadores_mas_jovenes['pts'].idxmax()]

# Imprime la información del jugador con el mayor puntaje
print("\nJugador con el mayor puntaje entre los más jóvenes:")
print(jugador_max_pts[['player_name', 'pts']])

#-------------
promedio_edad = nba_df['age'].mean()

# Imprime el promedio de edad
print("El promedio de edad de los jugadores de la NBA es:", promedio_edad)

#_____________
# Encuentra el jugador más alto
jugador_mas_alto = nba_df.loc[nba_df['player_height'].idxmax()]

# Imprime la información del jugador más alto
print("El jugador más alto es:", jugador_mas_alto['player_name'], "con una altura de", jugador_mas_alto['player_height'], "cm.")

# Encuentra el jugador más bajo
jugador_mas_bajito = nba_df.loc[nba_df['player_height'].idxmin()]

# Imprime la información del jugador más bajo
print("El jugador más bajo es:", jugador_mas_bajito['player_name'], "con una altura de", jugador_mas_bajito['player_height'], "cm.")

# Calcula el número de jugadores por universidad
jugadores_por_universidad = nba_df['college'].value_counts()

# Encuentra la universidad con el mayor número de jugadores
universidad_mas_jugadores = jugadores_por_universidad.idxmax()
numero_jugadores_mas_jugadores = jugadores_por_universidad.max()

# Imprime la universidad con más jugadores y su número
print("La universidad que ha producido más jugadores es", universidad_mas_jugadores, "con un total de", numero_jugadores_mas_jugadores, "jugadores.")

print(nba_df.columns)
nba_df = nba_df.drop('Unnamed: 0', axis=1)

print(nba_df.columns)