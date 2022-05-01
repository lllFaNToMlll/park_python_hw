"""
Класс для парсинга html
"""
import re
import collections


class HtmlParser:
    """Класс парсинга html """
    def __init__(self):
        """конструктор"""
        self.list_of_data = []

    def data_callback(self, data):
        """функция-обработчик тегов: текст между тегами
           Принимает текст и добавляет его в список всех
           текстов между тегами"""
        if "<" not in data and ">" not in data:
            self.list_of_data.append(data)
            return True
        return False

    def parse_html(self, html_str: str, data_callback):
        """функция парсинга html строки.
           Возвращает результаты работы
           функций-обработчиков"""
        for sequence in html_str.split("\n"):
            list_of_tag = re.split('(<|>)', sequence)
            list_of_tag_clear = []
            for idx, element in enumerate(list_of_tag):
                if list_of_tag[idx] == "<":
                    list_of_tag[idx+1] = list_of_tag[idx] + list_of_tag[idx+1]
                elif list_of_tag[idx] == ">":
                    list_of_tag[idx-1] = list_of_tag[idx-1] + list_of_tag[idx]

            for element in list_of_tag:
                if not ("<" in element and len(element) == 1)\
                        and not (">" in element and len(element) == 1)\
                        and element != "":
                    list_of_tag_clear.append(element)
                    data_callback(element)

        return self.list_of_data

    @staticmethod
    def remove_punctuation_marks(string):
        """Функция для удаления пунктуации"""
        string = re.sub(r'[^\w\s]', '', string)
        return string

    def find_text(self, result_of_parse_html, top_k):
        """Функция для предобработки результатов парсинга
           html, а также формирования топа слов"""
        reg_exp = re.compile("[а-яА-Я]+")
        rus = list(filter(reg_exp.match, result_of_parse_html))
        clear_russian = list(map(self.remove_punctuation_marks, rus))
        clear_russian = list(map(str.lower, clear_russian))

        word_counter = {}
        for sentence in clear_russian:
            for word in sentence.split():
                if word in word_counter:
                    word_counter[word] += 1
                else:
                    word_counter[word] = 1

        return dict(collections.Counter(word_counter).most_common(top_k))
