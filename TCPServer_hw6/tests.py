"""
Юнит тесты
"""
import unittest
import collections
from faker import Faker
from html_parser import HtmlParser
from client import Client
from master_worker_server import MasterWorkerServer


class MyTestCase(unittest.TestCase):
    """ Класс для юнит тестов"""
    def test_init(self):
        """Тест на правильную работу конструктора"""
        parser = HtmlParser()
        self.assertEqual(parser.list_of_data, [])

    def test_parse_html(self):
        """Тест на правильный парсинг"""
        parser = HtmlParser()
        fake = Faker(locale="Ru_ru")
        test_list_of_data = [fake.name() for i in range(10)]
        html = ["<person>" + "<name>" + test_list_of_data[i] + "</name>" + "</person>"
                for i in range(10)]
        html = "".join(html)
        html = '<html>' + "<persons>" + html + "</persons>" + '</html>'
        result = parser.parse_html(html, parser.data_callback)
        self.assertEqual(result, test_list_of_data)

    def test_remove_punctuation_marks(self):
        """Тест функции для удаления пунктуации"""
        parser = HtmlParser()
        result = parser.remove_punctuation_marks("Привет! Как дела, Геннадий?")
        self.assertEqual(result, "Привет Как дела Геннадий")

    def test_find_text(self):
        """Тест функции для предобработки результатов парсинга
           html, а также формирования топа слов"""
        parser = HtmlParser()
        fake = Faker(locale="Ru_ru")
        test_list_of_data = [fake.name() + fake.name() for i in range(10)]
        word_counter = {}
        for sentence in test_list_of_data:
            for word in sentence.split():
                if word.lower() in word_counter:
                    word_counter[word.lower()] += 1
                else:
                    word_counter[word.lower()] = 1

        counter_test_list_of_data = dict(collections.Counter(word_counter).most_common(3))
        html = ["<person>" + "<name>" + test_list_of_data[i] + "</name>" + "</person>"
                for i in range(10)]
        html = "".join(html)
        html = '<html>' + "<persons>" + html + "</persons>" + '</html>'
        result = parser.parse_html(html, parser.data_callback)
        result = parser.find_text(result, 3)
        self.assertEqual(result, counter_test_list_of_data)

    def test_create_butches(self):
        strings = ["string" + str(i) for i in range(20)]
        result_strings = [["string" + str(j + i) for i in range(5)] for j in [0, 5, 10, 15]]
        strings_butches = Client.create_butches(strings, 4)
        self.assertEqual(strings_butches, result_strings)

if __name__ == '__main__':
    unittest.main()
