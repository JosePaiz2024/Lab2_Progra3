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

# Colores
colores = ["#add8e6", "#d8bfd8", "#228f3e", "#bf4b72", "#e6e6fa", "#ffdab9", "#fffacd", "#98ff98", "#b0e0e6", "#dda0dd"]

# Crear el gráfico de barras
plt.figure(figsize=(12, 6))
plt.bar(actores, cantidades, color=colores)

# Personalizar el gráfico
plt.title('Los 10 Actores que Aparecen en Más Películas')
plt.xlabel('Actor')
plt.ylabel('Número de Películas')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Mostrar el gráfico
plt.show()
