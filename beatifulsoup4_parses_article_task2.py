import requests
from bs4 import BeautifulSoup

from constants import TABLE_TASK2


class TableParses:
    def send_get_requst(self, link):
        """
        Отправка запроса и получение содержимого ответа
        """
        self.current_url = link
        response = requests.get(url=self.current_url)
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text, "lxml")
        return soup

    def searching_elements_in_the_table(self, link):
        elements = [find_element.text for find_element in self.send_get_requst(link).find_all('b')]
        return elements

    def finding_the_sum_of_elements(self, link):
        sum_elements = 0
        for current_element in self.searching_elements_in_the_table(link):
            sum_elements += float(current_element)
        return sum_elements

a = TableParses()
print(a.finding_the_sum_of_elements(TABLE_TASK2))

