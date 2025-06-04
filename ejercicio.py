
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


np.arange(10)
# Genera un array de 10 números enteros aleatorios entre 0 y 100
array_aleatorio = np.random.randint(0, 100, size=10)
print("Array de números aleatorios:", array_aleatorio)

# genera una matriz de 3 filas y 4 columnas con números aleatorios
matriz_aleatoria = np.random.rand(3, 4)
print("Matriz de números aleatorios:\n", matriz_aleatoria)
# Genera una matriz de 3 filas y 4 columnas con números enteros aleatorios entre 0 y 100
matriz_aleatoria_enteros = np.random.randint(0, 100, size=(3, 4))
print("Matriz de números enteros aleatorios:\n", matriz_aleatoria_enteros)
#crea un array 2D y matrices
#Calcula su dimensión, tamaño, forma y tipo de sus elementos.
array1 = np.array([88,23,39,41])
print("Array 1D:", array1)
print("Dimensión:", array1.ndim)
print("Tamaño:", array1.size)
print("Forma:", array1.shape)
print("Tipo de datos:", array1.dtype)

array2 = np.array([[1, 2, 3], [4, 5, 6]])
print("Array 2D:\n", array2)


#array2=[76.4 21 38 ; 41.2 52 98]
#Donde el ";" nos quiere decir que a partir de ahí van los datos de la segunda fila de la matriz
array2 = np.array([[76.4, 21, 38], [41.2, 52, 98]])
print("Array 2D con datos específicos:\n", array2)  
#Calcula su dimensión, tamaño, forma y tipo de sus elementos.
print("Dimensión:", array2.ndim)
print("Tamaño:", array2.size)
print("Forma:", array2.shape)
print("Tipo de datos:", array2.dtype)

"""
array3=[12; 4; 9; 11]
Donde el ";" nos quiere decir que es un array columna con 4 filas.
"""
array3 = np.array([[12], [4], [9], [11]])
print("Array columna:\n", array3)
# Calcula su dimensión, tamaño, forma y tipo de sus elementos.
print("Dimensión:", array3.ndim)
print("Tamaño:", array3.size)
print("Forma:", array3.shape)
print("Tipo de datos:", array3.dtype)

#modificar un valor de array
