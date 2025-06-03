
import numpy as np

edades = [ 23, 45, 34, 23, 45, 67, 89, 12, 34, 56,]

media = np.mean(edades)
mediana = np.median(edades)

from scipy import stats
moda = stats.mode(edades)

try:
    valor_moda = moda.mode
    conteo_moda = moda.count
except AttributeError:
    valor_moda = moda[0]
    conteo_moda = moda[1]

print(f"media:{media}, mediana:{mediana}, moda:{valor_moda}, conteo_moda:{conteo_moda}")
# Ejercicio: Calcular media, mediana y moda de una lista de edades

# Calcula varianza y desviación estándar
varianza = np.var(edades, ddof=1)  # ddof=1 para muestra
desviasion = np.std(edades, ddof=1)  # ddof=1 para muestra

print(f"varianza:{varianza:.2f}, desviación estándar:{desviasion:.2f}")

