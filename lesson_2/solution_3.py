import csv
import json
import re
from datetime import datetime, date

class Client:
    def __init__(self, name: str, surname: str, birthday: str, bonuses: int):
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.bonuses = bonuses

    @classmethod
    def from_csv_row(cls, row):
        name, surname, birthday_str, bonuses_str = row
        bonuses = int(bonuses_str)

        # Дата рождения
        birthday = cls._validate_birthday(birthday_str)
        if not birthday:
            return None

        # Проверка имени и фамилии
        if not cls._validate_name(name) or not cls._validate_name(surname):
            return None

        # Проверка бонусов
        if not cls._validate_bonuses(bonuses):
            return None

        return cls(name, surname, birthday_str, bonuses)

    @staticmethod
    def _validate_name(name: str) -> bool:
        return bool(re.match(r'^[А-Яа-яЁё]+$', name))

    @staticmethod
    def _validate_birthday(birthday_str: str) -> datetime:
        try:
            birthday = datetime.strptime(birthday_str, "%d.%m.%Y").date()
            return birthday if date(1950, 1, 1) <= birthday <= date.today() else None
        except ValueError:
            return None

    @staticmethod
    def _validate_bonuses(bonuses: int) -> bool:
        return 0 <= bonuses <= 10_000_000


def csv_to_json(csv_file_path: str, json_file_path: str):
    processed_count = 0
    skipped_count = 0
    clients_list = []

    with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)

        for row in reader:
            client = Client.from_csv_row(row)
            if client:
                clients_list.append({
                    "name": client.name,
                    "surname": client.surname,
                    "birthday": client.birthday,
                    "Bonuses": client.bonuses,
                })
                processed_count += 1
            else:
                skipped_count += 1

    data = {
        "clients": clients_list
    }

    with open(json_file_path, mode='w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=4)

    print(f"Количество обработанных записей: {processed_count}")
    print(f"Количество пропущенных записей: {skipped_count}")


csv_file_path = 'clients.csv'
json_file_path = 'clients.json'

csv_to_json(csv_file_path, json_file_path)