import requests
from bs4 import BeautifulSoup

from constants import TABLE_TASK6


class TableParsesGreenandBlueElements:
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
        orange_elements = [float(find_element.text) for find_element in
                           self.send_get_requst(link).find_all('td', class_='orange')]
        return orange_elements

    def searching_blue_elements_in_the_table(self, link):
        count = 0
        new_blue_elements = []
        blue_elements = [float(find_element.text) for find_element in self.send_get_requst(link).find_all('td')]
        for current_element in blue_elements:
            count += 1
            if count == 15:
                new_blue_elements.append(int(current_element))
                count = 0
        return new_blue_elements

    def multiplication_and_sum_elements(self, link):
        multiplication_elements = []
        for orange, blue in zip(self.searching_green_elements_in_the_table(link), self.searching_blue_elements_in_the_table(link)):
            multiplication_elements.append(orange*blue)
        return sum(multiplication_elements)


a = TableParsesGreenandBlueElements()
# print(a.searching_green_elements_in_the_table(TABLE_TASK6))
print(a.multiplication_and_sum_elements(TABLE_TASK6))
