import csv

from constants import TABLE_TASK8
from parses_table_tasks_Beatiful_soup.base_class import BaseClass


class HDD(BaseClass):
    def get_part_link_on_page(self, link):
        """
        Получение части ссылки на каждую страницу
        """
        part_link_on_page = [
            link_page["href"]
            for link_page in self.send_requst_and_reply(link)
            .find("div", class_="pagen")
            .find_all("a")
        ]
        return part_link_on_page

    def link_build_on_page(self, link):
        """
        Построение ссылок на страницы
        """
        links = []
        for link_page in self.get_part_link_on_page(link):
            links.append(self.current_url[:26] + link_page)
        return links

    def search_name_product(self, link):
        """
        Поиск названия товара
        """
        name_products = [
            current_name.text.strip()
            for current_name in self.send_requst_and_reply(link).find_all(
                "a", class_="name_item"
            )
        ]
        return name_products

    def search_description(self, link):
        """
        Поиск описания товара
        """
        description_products = [
            current_description.text.split("\n")[1:]
            for current_description in self.send_requst_and_reply(link).find_all(
                "div", class_="description"
            )
        ]
        return description_products

    def search_price(self, link):
        """
        Поиск цены товара
        """
        price_products = [
            current_price.text
            for current_price in self.send_requst_and_reply(link).find_all(
                "p", class_="price"
            )
        ]
        return price_products

    def open_file(self, line, action_file):
        """
        Открытие файла и запись в него, затем закрытие
        """
        with open("task8", action_file, encoding="utf-8-sig", newline="") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(line)

    def write_lines_in_file(self, link):
        """
        Запись содержимого в файл
        """
        headers = [
            "Наименование",
            "Бренд",
            "Форм-фактор",
            "Ёмкость",
            "Объём буф. памяти",
            "Цена",
        ]
        self.open_file(headers, "w")
        for current_link in self.link_build_on_page(link):
            for name, price, description in zip(
                self.search_name_product(current_link),
                self.search_price(current_link),
                self.search_description(current_link),
            ):
                all_data_about_product = (
                    name,
                    price,
                    *[
                        current_description.split(":")[1].strip()
                        for current_description in description
                        if current_description
                    ],
                )
                print(all_data_about_product)
                self.open_file(all_data_about_product, "a")
        return "Файл успешно создан. Все данные записаны."


a = HDD()
print(a.write_lines_in_file(TABLE_TASK8))
