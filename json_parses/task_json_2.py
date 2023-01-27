import json

import requests
from bs4 import BeautifulSoup

from constants import JSON_TASK2


class Product:
    def send_requst_and_reply(self, link):
        self.current_url = link
        response = requests.get(url=self.current_url)
        response.encoding = "utf-8"
        reply = BeautifulSoup(response.text, "lxml")
        return reply

    def open_and_write_json_file(self, name_file):
        with open("file_task2.json", "w", encoding="utf-8") as f:
            json.dump(name_file, f, indent=4, ensure_ascii=False)
        return "Файл закрыт"

    def path_category_and_page(self, link, teg_path, teg, class_for_search, teg2):
        path = [
            current_path[teg_path]
            for current_path in self.send_requst_and_reply(link)
            .find(teg, class_=class_for_search)
            .find_all(teg2)
        ]
        return path

    def search_elem_by_all_tegs(self, link, teg, class_for_search):
        path = [
            current_path.text.strip().split("\n")
            for current_path in self.send_requst_and_reply(link).find_all(
                teg, class_=class_for_search
            )
        ]
        return path

    def build_link_category_and_build(self, link):
        link_categories = []
        link_pages_all_products = []
        for category in self.path_category_and_page(
            link, "href", "div", "nav_menu", "a"
        ):
            link_categories.append(link[:26] + category)
        for current_category in link_categories:
            for current_page in self.path_category_and_page(
                current_category, "href", "div", "pagen", "a"
            ):
                link_pages_all_products.append(current_category[:26] + current_page)
        return link_pages_all_products

    def search_data_about_products(self, link):
        result_json = []
        for current_link in self.build_link_category_and_build(link):
            print("Сейчас парсится", current_link)
            names = self.search_elem_by_all_tegs(current_link, "a", "name_item")
            prices_products = self.search_elem_by_all_tegs(current_link, "p", "price")
            current_description = self.search_elem_by_all_tegs(
                current_link, "div", "description"
            )

            for description_current_product, name, price in zip(
                current_description,
                (name for name in names),
                (price for price in prices_products),
            ):
                description_products = {}
                print("Текущий продукт и его описание", description_current_product)
                for element_description in description_current_product:
                    description_products["Наименование: "] = name[0]
                    description_products["Цена: "] = price[0]
                    element_description = element_description.split(":")
                    description_products[element_description[0]] = element_description[
                        1
                    ].strip()
                result_json.append(description_products)

        return result_json

    def create_file_json(self, link):
        self.open_and_write_json_file(self.search_data_about_products(link))
        return "Запись произведена успешно"


a = Product()
print(a.create_file_json(JSON_TASK2))
