import requests
from bs4 import BeautifulSoup

from constants import ARTICLES_TASK1


class ArticleProduct:
    """
    Поиск артиклов всех товаров и их сумма
    """

    def __init__(self, link=None):
        self.current_url = link

    def send_get_requst(self, link):
        """
        Отправка запроса и получение содержимого ответа
        """
        self.current_url = link
        response = requests.get(url=self.current_url)
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text, "lxml")
        return soup

    def get_part_link_on_page(self, link):
        """
        Получение части ссылки на каждую страницу
        """
        part_link_on_page = [
            link_page["href"]
            for link_page in self.send_get_requst(link)
            .find("div", class_="pagen")
            .find_all("a")
        ]
        return part_link_on_page

    def get_part_link_on_mouse(self, link):
        """
        Получение части ссылки на каждую мышь
        """
        part_link_on_mouse = [
            link_mouse_current["href"]
            for link_mouse_current in self.send_get_requst(link).find_all(
                "a", class_="name_item"
            )
        ]
        return part_link_on_mouse

    def get_all_articles(self, link):
        """
        Получение артиклов всех элементов
        """
        article_all = [
            int(article.text[9::])
            for article in self.send_get_requst(link).find_all("p", class_="article")
        ]
        return article_all

    def link_bulding_on_pages_and_mouses(self, link, page=None):
        """
        Построение ссылок на страницы и мыши
        """
        current_link = []
        if page:
            for link_page in self.get_part_link_on_page(link):
                current_link.append(self.current_url[:26] + link_page)
            return current_link
        else:
            for link_mouse in self.get_part_link_on_mouse(link):
                current_link.append(self.current_url[:26] + link_mouse)
            return current_link

    def go_on_links(self, link):
        link_on_mouses = []
        for current_link_on_page in self.link_bulding_on_pages_and_mouses(link, True):
            for link_on_mouse in self.link_bulding_on_pages_and_mouses(
                current_link_on_page, False
            ):
                link_on_mouses.append(link_on_mouse)
        return link_on_mouses

    def sum_all_articles(self, link):
        """
        Нахождение суммы артиклей элементов
        """
        sum_all_articles = 0
        for i in self.go_on_links(link):
            current = self.get_all_articles(i)[0]
            sum_all_articles += current
        return sum_all_articles

    def find_sum_article(self, link):
        """
        Функция для поиска суммы артиклей всех элементов
        """
        return self.sum_all_articles(link)


if __name__ == "__main__":
    a = ArticleProduct()
    print(a.find_sum_article(ARTICLES_TASK1))
