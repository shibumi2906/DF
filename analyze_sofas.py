import pandas as pd
import matplotlib.pyplot as plt

def analyze_data():
    # Обработка данных и построение гистограммы
    try:
        df = pd.read_csv('sofa_prices.csv')

        # Очистка данных
        df = df.dropna(subset=['price'])  # Удаление строк без цены
        df['price'] = df['price'].apply(pd.to_numeric, errors='coerce')  # Преобразование цен в числа, пропуская ошибки
        df = df.dropna(subset=['price'])  # Удаление строк с некорректными ценами
        df['price'] = df['price'].astype(int)  # Преобразование цен в целые числа

        # Вычисление средней цены
        average_price = df['price'].mean()
        print(f'Средняя цена на диваны: {average_price} ₽')

        # Построение гистограммы цен
        plt.figure(figsize=(10, 6))
        plt.hist(df['price'], bins=30, edgecolor='black')
        plt.title('Гистограмма цен на диваны')
        plt.xlabel('Цена (₽)')
        plt.ylabel('Частота')
        plt.grid(True)
        plt.show()
    except FileNotFoundError:
        print("CSV файл не найден.")
    except pd.errors.EmptyDataError:
        print("CSV файл пустой.")

if __name__ == "__main__":
    analyze_data()
