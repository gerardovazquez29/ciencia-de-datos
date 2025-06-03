
import csv

with open('ventas.csv', mode='r') as file:
    reader = csv.reader(file)
    datos = [tuple(row) for row in reader]

print(datos)
print(len(datos))
print(datos[5])

col = [fil[2] for fil in datos]
print(col)

def extraer_columna(data, index):
    col = [fil[index] for fil in data]
    del col[0:2]
    col = [float(item) for item in col]
    return col

def extraer_fila(data, index):
    fil = data[index]
    fila = [fil[0]] + [float(item) for item in fil[1:]]
    return fila

columna = extraer_columna(datos, 5)
fila = extraer_fila(datos, 4)
print(columna)
print(fila)


# 2. Por cada mes extraer la columna correspondiente de "datos",
#    calcular la suma de las ventas y almacenar el resultado
meses = []
ventas_mensuales = []
for col in range(2,25,2):
    mes = datos[0][col]
    columna = extraer_columna(datos, col+1)
    ventas_mensuales.append(sum(columna))
    meses.append(mes)

for mes, ventas in zip(meses, ventas_mensuales):
    print(f"{mes} - Ventas: ${ventas:.2f}")

# 2.1 Calcular los meses con ventas máximas y mínimas
# El mes con más ventas
max_ventas = max(ventas_mensuales)
idx_max = ventas_mensuales.index(max_ventas)
mes_max_ventas = meses[idx_max]
print(f"El mes con mas ventas fue: {mes_max_ventas} (${max_ventas:.2f})")
# El mes con menos ventas
min_ventas = min(ventas_mensuales)
idx_min = ventas_mensuales.index(min_ventas)
mes_min_ventas = meses[idx_min]
print(f"El mes con menos ventas fue: {mes_min_ventas} (${min_ventas:.2f})")

# 3. Por cada producto extraer la fila correspondiente de "datos",
#    calcular la suma anual ventas y almacenar los resultados
productos = []
prod_ventas = []
# por cada producto y por cada mes
for fil in range(2,10):
    fila = extraer_fila(datos, fil)
    productos.append(fila[0])

    monto_ventas = []
    for col in range(2,25,2):
        monto_ventas.append(fila[col+1])

    prod_ventas.append(sum(monto_ventas))
for producto, monto in zip(productos, prod_ventas):
    print(f"{producto}: ${monto:.2f} en ventas")

#    3.1 Organizar de forma descendente los listados de productos
#    usando como criterio el monto total de las ventas anuales, y
#    tomar el top-3

ventas_y_prods = list(zip(prod_ventas, productos))
print(ventas_y_prods)

ventas_y_prods.sort(reverse=True, key=lambda x: x[0])
print(ventas_y_prods)

print("Top 3 productos con más ventas:")
for item in ventas_y_prods[0:3]:
    print(f"{item[1]} (${item[0]:.2f})")

# Generar reporte

with open('reporte_ventas.txt', mode='w') as file:
    file.write('Meses con mayores y menores ventas:\n')
    file.write('-'*50 + '\n')
    file.write(f"  - Mes con mejores ventas: {mes_max_ventas} (${max_ventas:.2f})\n")
    file.write(f"  - Mes con peores ventas: {mes_min_ventas} (${min_ventas:.2f})\n")
    file.write('\nProductos con mayores ventas:\n')
    file.write('-'*50 + '\n')
    for item in ventas_y_prods[0:3]:
        file.write(f"  - {item[1]} (${item[0]:.2f})\n")
file.close()
print("Reporte generado exitosamente en 'reporte_ventas.txt'")
# Fin del script

