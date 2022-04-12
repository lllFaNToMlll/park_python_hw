"""
Домашнее задание к лекции #2
Написать функцию, которая в качестве аргументов принимает строку html,
3 функции-обработчика тегов: открытие тега, текст между тегами, закрытие тега
Функция, должна принимать строку, в которой содержится html, и произвести парсинг этого html
def parse_html(html_str: str, open_tag_callback, data_callback, close_tag_callback)
Использовать mock-объект при тестировании:
Использовать mock-объект, например, close_tag_callback и проверить, что заглушка
вызывалась n число раз.
Использовать factory boy:
Для генерации данных, находящихся между тегами или значения аттрибутов,
нужно использовать factory boy.
Узнать степень покрытия тестами с помощью библиотеки coverage
"""
import re
from faker import Faker


def generate_html():
    """Функция генерации html с помощью factory boy"""
    fake = Faker(locale="Ru_ru")
    html = ["<person>" + "<name>" + fake.name() + "</name>" +
            "<email>" + fake.email() + "</email>" + "</person>"
            for i in range(10)]
    html = "".join(html)
    html = '<html>' + "<persons>" + html + "</persons>" + '</html>'
    return html


class HtmlParser:
    """Класс парсинга html """
    def __init__(self):
        """конструктор"""
        self.counter_of_open_tags = {}
        self.counter_of_close_tags = {}
        self.list_of_data = []


    def open_tag_callback(self, open_tag):
        """функция-обработчик тегов: открытие тега
           Принимает на вход тег, после чего либо
           увеличивает количество этого тега в
           словаре, либо добавляет его в словарь"""
        if "<" in open_tag and ">" in open_tag and "/" not in open_tag:
            if open_tag in self.counter_of_open_tags:
                self.counter_of_open_tags[open_tag] += 1
            else:
                self.counter_of_open_tags[open_tag] = 1
            return True
        return False



    def data_callback(self, data):
        """функция-обработчик тегов: текст между тегами
           Принимает текст и добавляет его в список всех
           текстов между тегами"""
        if "<" not in data and ">" not in data:
            self.list_of_data.append(data)
            return True
        return False


    def close_tag_callback(self, close_tag):
        """функция-обработчик тегов: закрытие тега
           Принимает на вход тег, после чего либо
           увеличивает количество этого тега в
           словаре, либо добавляет его в словарь"""
        if "</" in close_tag and ">" in close_tag:
            if close_tag in self.counter_of_close_tags:
                self.counter_of_close_tags[close_tag] += 1
            else:
                self.counter_of_close_tags[close_tag] = 1
            return True
        return False


    def parse_html(self, html_str: str, open_tag_callback, data_callback, close_tag_callback):
        """функция парсинга html строки.
           Возвращает результаты работы
           функций-обработчиков"""
        for sequence in html_str.split("\n"):
            list_of_tag = re.split('(<|>)', sequence)
            list_of_tag_clear = []
            for index, element in enumerate(list_of_tag):
                if list_of_tag[index] == "<":
                    list_of_tag[index+1] = list_of_tag[index] + list_of_tag[index+1]
                elif list_of_tag[index] == ">":
                    list_of_tag[index-1] = list_of_tag[index-1] + list_of_tag[index]

            for element in list_of_tag:
                if not ("<" in element and len(element) == 1)\
                        and not (">" in element and len(element) == 1)\
                        and element != "":
                    list_of_tag_clear.append(element)
                    open_tag_callback(element)
                    close_tag_callback(element)
                    data_callback(element)

        return self.counter_of_open_tags, self.list_of_data, self.counter_of_close_tags

if __name__ == "__main__":
    parser = HtmlParser()
    result = parser.parse_html(generate_html(), parser.open_tag_callback,
                      parser.data_callback, parser.close_tag_callback)
    print(result)
