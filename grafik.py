import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
num_samples = 100  # Количество образцов
data1 = np.random.rand(num_samples)  #  Первый набор данных
data2 = np.random.rand(num_samples)  #  Второй набор данных

# Построение диаграммы рассеяния
plt.figure(figsize=(10, 6))
plt.scatter(data1, data2, alpha=0.5)
plt.title('Scatter Plot of Two Random Data Sets')
plt.xlabel('Data Set 1')
plt.ylabel('Data Set 2')
plt.grid(True)
plt.show()

# Эта строка помогает убедиться, что график отображается, особенно в средах, которые могут не отображать графики автоматически
input("Press [enter] to finish.")

