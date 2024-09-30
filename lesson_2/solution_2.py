import json
from collections import defaultdict

def counting_stocks(json_file):
    # Инициализируем словарь для хранения данных о количестве категорий
    stocks = defaultdict(float)

    # Читаем данные из json-файла
    
    with open(json_file, 'r', encoding='utf-8') as file:  
        data = json.load(file)
        for inventory in data['inventory']:
            item = inventory['item']
            quantity = inventory['quantity']
            minimum_required = inventory['minimum_required']
            
            if quantity < minimum_required:
                stocks[item] = minimum_required - quantity

    return stocks

def main():
    json_file = 'inventory.json'  
    stocks_quantity = counting_stocks(json_file)

    # Выводим результаты
    print("Необходимо закупить:")
    for item, quantity in stocks_quantity.items():
        print(f"{item}: {quantity} шт.")

if __name__ == "__main__":
    main()