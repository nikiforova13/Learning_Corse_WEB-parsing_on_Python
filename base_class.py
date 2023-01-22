import requests
from bs4 import BeautifulSoup


class BaseClass:
    def send_requst_and_reply(self, link):
        """
        Отправка запроса и получение содержимого ответа
        """
        self.current_url = link
        response = requests.get(url=self.current_url)
        response.encoding = "utf-8"
        reply = BeautifulSoup(response.text, "lxml")
        return reply
