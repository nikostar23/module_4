import csv
csv_file = "client.csv"
print("Добрый день!")
with open(csv_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Surname", "Birthday", "Bonuses"])
    while True:
        print("Вводите данные: ")
        name = input("Имя: ")
        if name == "stop":
            break
        surname = input("Фамилия: ")
        birthday = input("День рождения: ")
        bonuses = input("Баланс бонусов: ")
        writer.writerow([name, surname, birthday, bonuses])
        print(f"Спасибо! Клиент {name} добавлен!")