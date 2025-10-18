import matplotlib.pyplot as plt
import numpy as np

dataset = np.load("dataset.npz")

X, y = dataset["X"], dataset["y"]
# Contar cuántas muestras hay por clase
unique_classes, counts = np.unique(y, return_counts=True)

# Crear el gráfico de barras
plt.figure(figsize=(10,5))
plt.bar(unique_classes, counts, color='skyblue', edgecolor='black')
plt.xticks(unique_classes)  # Mostrar todas las clases en el eje X
plt.xlabel('Class')
plt.ylabel('Number of images')
plt.title('Class distribution in the dataset')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()

