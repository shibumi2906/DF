import pandas as pd
import numpy as np

# Создаем DataFrame с оценками учеников
data = {
    'Имя': ['Вася', 'Петя', 'Сережа', 'Лена', 'Аня', 'Лида', 'Марина', 'Галя', 'Костя', 'Света'],
    'Математика': [8, 7, 6, 9, 10, 7, 8, 6, 7, 9],
    'Физика': [7, 8, 7, 6, 9, 8, 7, 6, 7, 8],
    'Биология': [9, 6, 8, 7, 10, 8, 7, 6, 9, 7],
    'Литература': [8, 9, 7, 8, 10, 9, 8, 7, 8, 9],
    'История': [7, 8, 7, 9, 10, 8, 7, 6, 8, 9]
}

df = pd.DataFrame(data)

# Вывод первых нескольких строк DataFrame
print(df.head())

mean_scores = df.mean(numeric_only=True)  # средняя оценка по каждому предмету
print("Средние оценки по предметам:\n", mean_scores)

median_scores = df.median(numeric_only=True)  # медиальная оценка по каждому предмету
print("Медианные оценки по предметам:\n", median_scores)

Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IQR_math = Q3_math - Q1_math

print(f"Q1 (25-й процент) для математики: {Q1_math}")  #Вычисление Q1 и Q3 для оценок по математике
print(f"Q3 (75-й процент) для математики: {Q3_math}")
print(f"IQR для математики: {IQR_math}")

std_deviation = df.std(numeric_only=True)  # Вычисление стандартного отклонения
print("Стандартное отклонение по предметам:\n", std_deviation)







