import requests
from bs4 import BeautifulSoup

from constants import TABLE_TASK5


class TableParsesGreenElements:
    def send_get_requst(self, link):
        """
        Отправка запроса и получение содержимого ответа
        """
        self.current_url = link
        response = requests.get(url=self.current_url)
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text, "lxml")
        return soup

    def searching_green_elements_in_the_table(self, link):
        elements = [float(find_element.text) for find_element in self.send_get_requst(link).find_all('td', class_='green')]
        return elements

    def sum_elements(self, link):
        sum_all_elements = sum(self.searching_green_elements_in_the_table(link))
        return sum_all_elements

a = TableParsesGreenElements()
print(a.sum_elements(TABLE_TASK5))