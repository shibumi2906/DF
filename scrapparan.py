import scrapy
import pandas as pd
import matplotlib.pyplot as plt


class SofaSpider(scrapy.Spider):
    name = 'sofa'
    allowed_domains = ['divan.ru']
    start_urls = ['https://www.divan.ru/category/divany-i-kresla']

    def parse(self, response):
        self.log(f'Parsing page: {response.url}')

        # Используем CSS селектор для извлечения данных о продуктах
        product_divs = response.css('div.lsooF')
        if not product_divs:
            self.log('No product divs found! Check the CSS selector.')
            return

        for product in product_divs:
            name = product.css('span[itemprop="name"]::text').get()
            price_text = product.css('meta[itemprop="price"]::attr(content)').get()

            # Преобразование цены в число
            if price_text:
                try:
                    price = int(price_text.replace('₽', '').replace(' ', '').strip())
                except ValueError:
                    self.log(f'Price conversion error: {price_text}')
                    price = None
            else:
                price = None

            yield {
                'name': name,
                'price': price,
                'link': response.url
            }

        # Проверяем наличие следующей страницы
        next_page = response.css('a.pagination__next::attr(href)').get()
        if next_page:
            self.log(f'Next page found: {next_page}')
            yield response.follow(next_page, self.parse)
        else:
            self.log('No next page link found!')


# Запуск парсинга и сохранение данных в CSV файл
from scrapy.crawler import CrawlerProcess

process = CrawlerProcess(settings={
    'FEEDS': {
        'sofa_prices.csv': {'format': 'csv'},
    }
})

process.crawl(SofaSpider)
process.start()

# Обработка данных и построение гистограммы
try:
    df = pd.read_csv('sofa_prices.csv')

    # Очистка данных
    df = df.dropna(subset=['price'])  # Удаление строк без цены
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



