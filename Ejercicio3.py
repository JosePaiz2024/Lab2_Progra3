import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("gym.csv")

# Tomar las primeras 25 personas
dfFirst = df.head(25)

# Agrupar los datos por género y tipo de Workout
workout_counts = dfFirst.groupby(['Gender', 'Workout_Type']).size().unstack()

# Seleccionar un tipo de Workout, por ejemplo 'Cardio'
workout_selected = 'Cardio'  # puede cambiar el tipo de Workout que quiera ver

# Contar cuántas personas de cada género hacen el tipo de Workout seleccionado
cantidad = dfFirst[dfFirst['Workout_Type'] == workout_selected]['Gender'].value_counts()

# Definir los colores 
colors = ['#add8e6', '#d291bc']  

# Crear la gráfica circular
cantidad.plot(kind='pie', autopct='%1.1f%%', colors=colors)

# Título y etiquetas
plt.title(f"Distribución de Género para {workout_selected}")
plt.ylabel("")

# Mostrar la gráfica
plt.show()
