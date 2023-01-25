from constants import TABLE_TASK4
from parses_table_tasks_Beatiful_soup.base_class import BaseClass


class Product(BaseClass):
    def get_path_page(self, link):
        """
        Получение части ссылки на каждую страницу
        """
        path_pages = [
            link_page["href"]
            for link_page in self.send_requst_and_reply(link)
            .find("div", class_="pagen")
            .find_all("a")
        ]
        return path_pages

    def get_path_product(self, link):
        """
        Получение части ссылки на каждый продукт
        """
        path_products = [
            link_mouse_current["href"]
            for link_mouse_current in self.send_requst_and_reply(link).find_all(
                "a", class_="name_item"
            )
        ]
        return path_products

    def get_category(self, link):
        """
        Получение части ссылки на каждую категорию продукта
        """
        path_categores = [
            current_category["href"]
            for current_category in self.send_requst_and_reply(link)
            .find("div", class_="nav_menu")
            .find_all("a")
        ]
        return path_categores

    def get_price(self, link):
        """
        Получение цены на каждый товар
        """
        prices = [
            int(current_price[:-3])
            for current_price in self.send_requst_and_reply(link).find(
                "span", id="price"
            )
        ]
        return prices

    def get_count(self, link):
        """
        Кол-во каждого товара
        """
        count_products = [
            int(current_count[11:])
            for current_count in self.send_requst_and_reply(link).find(
                "span", id="in_stock"
            )
        ]
        return count_products

    def link_build_on_page_or_product(self, link, page=None):
        """
        Построение ссылок на навигационные кнопки и страницы товаров
        """
        links = []
        if page:
            for link_page in self.get_path_page(link):
                links.append(self.current_url[:26] + link_page)
        else:
            for link_mouse in self.get_path_product(link):
                links.append(self.current_url[:26] + link_mouse)

        return links

    def build_link_category(self, link):
        """
        Построение ссылок на страниуы категорий товаров
        """
        links_category = [self.current_url[:26] + i for i in self.get_category(link)]
        return links_category

    def go_on_links(self, link):
        """
        Проход по определенной категории товаров, по каждой кнопке из навигационного меню и по самому товару
        """
        link_all_products = []
        for i in self.build_link_category(link):
            for current_link_on_page in self.link_build_on_page_or_product(i, True):
                for link_on_mouse in self.link_build_on_page_or_product(
                    current_link_on_page, False
                ):
                    link_all_products.append(link_on_mouse)
        return link_all_products

    def find_sum_and_multiply_elements(self, link):
        """
        Нахождение произведения цены * товар, а затем сумма всего найденного
        """
        multiply = []
        for i in self.go_on_links(link):  # идем по какойто ссылке
            current_price = self.get_price(i)[0]
            current_count = self.get_count(i)[0]
            multiply.append(current_price * current_count)
        return sum(multiply)


a = Product()
print(a.find_sum_and_multiply_elements(TABLE_TASK4))
