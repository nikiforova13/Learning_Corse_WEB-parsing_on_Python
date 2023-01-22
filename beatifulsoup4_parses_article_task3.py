from bs4 import BeautifulSoup
import requests

from constants import TABLE_TASK1


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

    def search_tr_td(self, link):
        elements = [i.text for i in self.send_get_requst(link).find_all('td')]
        return set(elements)

    def sum_tr_td(self, link):
        sum = 0
        for i in self.search_tr_td(link):
            sum += float(i)
        return sum


a = TableParses()
print(a.sum_tr_td(TABLE_TASK1))
