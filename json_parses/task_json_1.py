import json

import requests
from bs4 import BeautifulSoup

from constants import JSON_TASK1


class Watch:
    def send_requst_and_reply(self, link):
        """
        Отправка запроса и получение содержимого ответа
        """
        self.current_url = link
        response = requests.get(url=self.current_url)
        response.encoding = "utf-8"
        reply = BeautifulSoup(response.text, "lxml")
        return reply

    def open_and_write_file(self, name_file):
        with open("task_json_1.json", "w", encoding="utf-8") as f:
            json.dump(name_file, f, indent=4, ensure_ascii=False)
        return "Файл закрыт"

    def get_name(self, link):
        names_watches = [
            current_name.text
            for current_name in self.send_requst_and_reply(link).find_all(
                "a", class_="name_item"
            )
        ]
        return names_watches

    def get_price(self, link):
        all_price_watches = [
            current_price.text
            for current_price in self.send_requst_and_reply(link).find_all(
                "p", class_="price"
            )
        ]
        return all_price_watches

    def get_description(self, link):
        description_watches = [
            current_description.text.strip().split("\n")
            for current_description in self.send_requst_and_reply(link).find_all(
                "div", class_="description"
            )
        ]
        return description_watches

    def full_description(self, link):
        """
        Создаем словарь для каждого товара со своим полным описанием и возвращем список из этих всех словарей
        """
        result_json = []
        all_names = self.get_name(link)
        all_prices = self.get_price(link)
        for current_description in self.get_description(link):
            current_data = {}
            if len(all_names) and len(all_prices) != 0:
                current_data["Наименование:"] = all_names.pop(0)
                current_data["Цена:"] = all_prices.pop(0)
            for current_element in current_description:
                current_data[(current_element.split(":"))[0]] = (
                    current_element.split(":")
                )[1].strip()
            result_json.append(current_data)
        return result_json

    def write_to_file(self, link):
        self.open_and_write_file(self.full_description(link))
        return "Запись произведена успешно"


a = Watch()
print(a.write_to_file(JSON_TASK1))
