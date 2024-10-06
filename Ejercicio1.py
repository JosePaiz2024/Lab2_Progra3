import pandas as pd
import matplotlib.pyplot as plt
import ast

# Cargar el dataset
df = pd.read_csv('tmdb_5000_credits.csv') 

# Función para extraer nombres de actores
def extraer_actores(cast_str):
    cast = ast.literal_eval(cast_str)
    return [actor['name'] for actor in cast[:5]]  # Tomamos solo los primeros 5 actores

# Aplicar la función para extraer actores
df['actores'] = df['cast'].apply(extraer_actores)

# Contar la frecuencia de cada actor
actores_count = {}
for actores in df['actores']:
    for actor in actores:
        if actor in actores_count:
            actores_count[actor] += 1
        else:
            actores_count[actor] = 1

# Ordenar los actores por frecuencia
actores_ordenados = sorted(actores_count.items(), key=lambda x: x[1], reverse=True)

# Preparar datos para el gráfico
actores = [x[0] for x in actores_ordenados[:10]]  # Top 10 actores
cantidades = [x[1] for x in actores_ordenados[:10]]

# Crear el gráfico de barras
plt.figure(figsize=(12, 6))
plt.bar(actores, cantidades)

# Personalizar el gráfico
plt.title('Los 10 Actores que Aparecen en Más Películas')
plt.xlabel('Actor')
plt.ylabel('Número de Películas')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Mostrar el gráfico
plt.show()

"""ENLACE: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_credits.csv"""

"""Este ejercicio analiza un conjunto de datos de películas, identifica los actores que aparecen con más frecuencia, 
y crea un gráfico de barras que muestra los 10 actores que aparecen en más películas. Es una herramienta útil para
 visualizar qué actores están más presentes en este conjunto de datos de películas."""