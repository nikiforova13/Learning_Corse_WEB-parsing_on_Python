import csv

import requests
from bs4 import BeautifulSoup

from constants import TABLE_TASK9


class Product:
    def send_requst_and_reply(self, link):
        """
        Отправка запроса и получение содержимого ответа
        """
        self.current_url = link
        response = requests.get(url=self.current_url)
        response.encoding = "utf-8"
        reply = BeautifulSoup(response.text, "lxml")
        return reply

    def open_file_and_write_data(self, attract_file, line):
        with open("task9.csv", attract_file, encoding="utf-8-sig", newline="") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(line)

    def path_for_category(self, link):
        category = [
            current_category["href"]
            for current_category in self.send_requst_and_reply(link)
            .find("div", class_="nav_menu")
            .find_all("a")
        ]
        return category

    def path_for_page(self, link):
        pages = [
            current_page["href"]
            for current_page in self.send_requst_and_reply(link)
            .find("div", class_="pagen")
            .find_all("a")
        ]
        return pages

    def link_build_on_page(self, link, category=True):
        """
        Построение ссылок на страницы и категории
        """
        links = []
        if category:
            for link_category in self.path_for_category(link):
                links.append(self.current_url[:25] + link_category)
        else:
            for link_page in self.path_for_page(link):
                links.append(self.current_url[:25] + link_page)
        return links

    def get_name(self, link):
        names_products = [
            current_name.text
            for current_name in self.send_requst_and_reply(link).find_all(
                "a", class_="name_item"
            )
        ]
        return names_products

    def get_description(self, link):
        desctiption_products = [
            current_description.text.strip().split("\n")
            for current_description in self.send_requst_and_reply(link).find_all(
                "div", class_="description"
            )
        ]
        return desctiption_products

    def get_price(self, link):
        price_products = [
            current_price.text
            for current_price in self.send_requst_and_reply(link).find_all(
                "p", class_="price"
            )
        ]
        return price_products

    def go_on_links(self, link):
        all_links_products = []
        for category in self.link_build_on_page(link):
            for page in self.link_build_on_page(category, category=False):
                all_links_products.append(page)
        return all_links_products

    def get_all_data(self, link):
        for current_link in self.go_on_links(link):
            for name, description, price in zip(
                self.get_name(current_link),
                self.get_description(current_link),
                self.get_price(current_link),
            ):
                data_about_products = (
                    name,
                    price,
                    *[
                        current_description.split(":")[1]
                        for current_description in description
                    ],
                )
                self.open_file_and_write_data("a", data_about_products)
        return "Запись данных в файл произошла успешно"


a = Product()
print(a.get_all_data(TABLE_TASK9))
