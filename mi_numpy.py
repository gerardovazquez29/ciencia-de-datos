
import numpy as np

mi_array = np.array([[1.2], [3.4]])

mi_array = np.append(mi_array, [[5.6]], axis=0)
print(mi_array)

m1 = np.random.randint(1,100, size=(3, 4))
m2 = np.random.randint(1,100, size=(2, 4))
print(m1)
print(m2)
m3 = np.vstack((m1, m2))
print(m3)


valor = np.array([[73,86,90,20],[96,55,15,48],[38,63,96,95],[13,87,32,96]])
print(valor)
print(np.diag(valor)) 

for k in range(1, valor.shape[0]):
    print(f'k = {k}', np.diag(valor, k=k))
     # Extracts the diagonal elements
