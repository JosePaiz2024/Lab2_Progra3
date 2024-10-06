import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
df = pd.read_csv('Indicators.csv')

# Seleccionar el indicador de PIB y algunos países
indicador = 'NY.GDP.MKTP.CD'  # Código para PIB (US$ a precios actuales)
paises = ['United States', 'China', 'Japan', 'Germany', 'United Kingdom']

# Filtrar el DataFrame
df_filtrado = df[(df['IndicatorCode'] == indicador) & (df['CountryName'].isin(paises))]

# Crear el gráfico de líneas
plt.figure(figsize=(12, 6))

for pais in paises:
    datos_pais = df_filtrado[df_filtrado['CountryName'] == pais]
    plt.plot(datos_pais['Year'], datos_pais['Value'], label=pais)

plt.title('PIB de países seleccionados a lo largo del tiempo')
plt.xlabel('Año')
plt.ylabel('PIB (US$ a precios actuales)')
plt.legend()
plt.grid(True)

# Mostrar el gráfico
plt.show()