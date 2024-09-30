import json
from collections import defaultdict

def calculate_revenue(json_file):
    # Инициализируем словарь для хранения итоговых сумм по категориям
    category_revenue = defaultdict(float)

    # Читаем данные из json-файла
    
    with open(json_file, 'r', encoding='utf-8') as file:  
        data = json.load(file)
        for sale in data['sales']:
            category = sale['category']
            total_price = sale['total_price']
            category_revenue[category] += total_price

    return category_revenue

def main():
    json_file = 'sales.json'  
    revenue = calculate_revenue(json_file)

    # Выводим результаты
    print("Общая выручка по категориям:")
    for category, total in revenue.items():
        print(f"{category}: {total} руб.")

if __name__ == "__main__":
    main()