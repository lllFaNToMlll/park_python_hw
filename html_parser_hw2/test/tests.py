"""
Юнит тесты
"""

import unittest
from unittest.mock import patch
from faker import Faker
from src.html_parser_class import HtmlParser, generate_html


class MyTestCase(unittest.TestCase):
    """ Класс для юнит тестов"""
    def test_generate_html(self):
        """Тест на правильную работу конструктора"""
        html = generate_html()
        self.assertTrue(len(html) != 0, True)


    def test_init(self):
        """Тест на правильную работу конструктора"""
        parser = HtmlParser()
        self.assertEqual(parser.counter_of_open_tags, {})
        self.assertEqual(parser.counter_of_close_tags, {})
        self.assertEqual(parser.list_of_data, [])


    def test_open_tag_callback(self):
        """Тест на правильную работу
        функции-обработчика тегов: открытие тега"""
        fake = Faker(locale="Ru_ru")
        parser = HtmlParser()
        test_counter_of_open_tags = {"<head>": 1}
        self.assertTrue(parser.open_tag_callback("<head>"), True)
        self.assertEqual(parser.counter_of_open_tags, test_counter_of_open_tags)
        self.assertFalse(parser.open_tag_callback("</head>"), False)
        self.assertEqual(parser.counter_of_open_tags, test_counter_of_open_tags)
        self.assertFalse(parser.open_tag_callback(fake.name()), False)
        self.assertEqual(parser.counter_of_open_tags, test_counter_of_open_tags)


    def test_close_tag_callback(self):
        """Тест на правильную работу
        функции-обработчика тегов: закрытие тега"""
        fake = Faker(locale="Ru_ru")
        parser = HtmlParser()
        test_counter_of_close_tags = {"</head>": 1}
        self.assertTrue(parser.close_tag_callback("</head>"), True)
        self.assertEqual(parser.counter_of_close_tags, test_counter_of_close_tags)
        self.assertFalse(parser.close_tag_callback("<head>"), False)
        self.assertEqual(parser.counter_of_close_tags, test_counter_of_close_tags)
        self.assertFalse(parser.close_tag_callback(fake.name()), False)
        self.assertEqual(parser.counter_of_close_tags, test_counter_of_close_tags)


    def test_data_callback(self):
        """Тест на правильную работу
        функции-обработчика тегов: текст между тегами"""
        fake = Faker(locale="Ru_ru")
        parser = HtmlParser()
        test_data = fake.name()
        test_list_of_data = [test_data]
        self.assertTrue(parser.data_callback(test_data), True)
        self.assertEqual(parser.list_of_data, test_list_of_data)
        self.assertFalse(parser.data_callback("<head>"), False)
        self.assertEqual(parser.list_of_data, test_list_of_data)
        self.assertFalse(parser.data_callback("</head>"), False)
        self.assertEqual(parser.list_of_data, test_list_of_data)


    def test_parse_html(self):
        """Тест на правильный парсинг"""
        parser = HtmlParser()
        fake = Faker(locale="Ru_ru")
        test_list_of_data = [fake.name() for i in range(10)]
        test_counter_of_open_tags = {'<html>': 1, '<persons>': 1, '<person>': 10, '<name>': 10}
        test_counter_of_close_tags = {'</name>': 10, '</person>': 10, '</persons>': 1, '</html>': 1}
        html = ["<person>" + "<name>" + test_list_of_data[i] + "</name>" + "</person>"
                for i in range(10)]
        html = "".join(html)
        html = '<html>' + "<persons>" + html + "</persons>" + '</html>'
        result = parser.parse_html(html, parser.open_tag_callback,
                                   parser.data_callback, parser.close_tag_callback)
        self.assertEqual(result[0], test_counter_of_open_tags)
        self.assertEqual(result[1], test_list_of_data)
        self.assertEqual(result[2], test_counter_of_close_tags)


    @patch("src.html_parser_class.HtmlParser.parse_html", return_value=({'<html>': 1,
    '<persons>': 1, '<person>': 10, '<name>': 10, '<email>': 10}, ['Наталья Ждановна Гордеева',
    'agafonovradovan@example.org', 'Кулагин Остромир Владиленович', 'pimen1994@example.org',
    'Белозеров Прокл Всеволодович', 'anzhelika_39@example.org', 'Стрелков Артем Анатольевич',
    'osamolov@example.net', 'Соболев Вячеслав Григорьевич', 'gkondratev@example.org',
    'Маргарита Афанасьевна Гусева', 'frolovisa@example.org', 'Анна Львовна Афанасьева',
    'ilja87@example.org', 'Юлий Устинович Петухов', 'shestakovernest@example.net',
    'Валерия Кузьминична Пестова', 'valerjan_1997@example.org', 'Смирнова Екатерина Филипповна',
    'feoktist_1987@example.org'], {'</name>': 10, '</email>': 10, '</person>': 10, '</persons>': 1,
    '</html>': 1}))
    def test_parse_html_mock(self, parse_html_mock):
        """Тест на правильный парсинг"""
        parser = HtmlParser()
        fake = Faker(locale="Ru_ru")
        test_list_of_data = [fake.name() for i in range(10)]
        test_counter_of_open_tags = {'<html>': 1, '<persons>': 1, '<person>': 10, '<name>': 10}
        test_counter_of_close_tags = {'</name>': 10, '</person>': 10, '</persons>': 1, '</html>': 1}
        html = ["<person>" + "<name>" + test_list_of_data[i] + "</name>" + "</person>"
                for i in range(10)]
        html = "".join(html)
        html = '<html>' + "<persons>" + html + "</persons>" + '</html>'
        result = parser.parse_html(html, parser.open_tag_callback,
                                   parser.data_callback, parser.close_tag_callback)
        print(result)
        self.assertEqual(parse_html_mock.call_count, 1)


    @patch("src.html_parser_class.HtmlParser.open_tag_callback", return_value=True)
    @patch("src.html_parser_class.HtmlParser.data_callback", return_value=True)
    @patch("src.html_parser_class.HtmlParser.close_tag_callback", return_value=True)
    def test_parse_html_all_tag_mock(self, open_tag_callback_mock, data_callback_mock, close_tag_callback_mock):
        """Тест на правильный парсинг"""
        parser = HtmlParser()
        fake = Faker(locale="Ru_ru")
        test_list_of_data = [fake.name() for i in range(10)]
        html = ["<person>" + "<name>" + test_list_of_data[i] + "</name>" + "</person>"
                for i in range(10)]
        html = "".join(html)
        html = '<html>' + "<persons>" + html + "</persons>" + '</html>'
        result = parser.parse_html(html, parser.open_tag_callback,
                                   parser.data_callback, parser.close_tag_callback)
        self.assertEqual(open_tag_callback_mock.call_count, 54)
        self.assertEqual(data_callback_mock.call_count, 54)
        self.assertEqual(close_tag_callback_mock.call_count, 54)


    @patch("src.html_parser_class.HtmlParser.data_callback", return_value=True)
    def test_parse_html_data_callback_mock(self, data_callback_mock):
        """Тест на правильный парсинг"""
        parser = HtmlParser()
        fake = Faker(locale="Ru_ru")
        test_list_of_data = [fake.name() for i in range(10)]
        test_counter_of_open_tags = {'<html>': 1, '<persons>': 1, '<person>': 10, '<name>': 10}
        test_counter_of_close_tags = {'</name>': 10, '</person>': 10, '</persons>': 1, '</html>': 1}
        html = ["<person>" + "<name>" + test_list_of_data[i] + "</name>" + "</person>"
                for i in range(10)]
        html = "".join(html)
        html = '<html>' + "<persons>" + html + "</persons>" + '</html>'
        result = parser.parse_html(html, parser.open_tag_callback,
                                   parser.data_callback, parser.close_tag_callback)
        self.assertEqual(result[0], test_counter_of_open_tags)
        self.assertEqual(result[2], test_counter_of_close_tags)
        self.assertEqual(data_callback_mock.call_count, 54)


    @patch("src.html_parser_class.HtmlParser.open_tag_callback", return_value=True)
    def test_parse_html_open_tag_callback_mock(self, open_tag_callback_mock):
        """Тест на правильный парсинг"""
        parser = HtmlParser()
        fake = Faker(locale="Ru_ru")
        test_list_of_data = [fake.name() for i in range(10)]
        test_counter_of_close_tags = {'</name>': 10, '</person>': 10, '</persons>': 1, '</html>': 1}
        html = ["<person>" + "<name>" + test_list_of_data[i] + "</name>" + "</person>"
                for i in range(10)]
        html = "".join(html)
        html = '<html>' + "<persons>" + html + "</persons>" + '</html>'
        result = parser.parse_html(html, parser.open_tag_callback,
                                   parser.data_callback, parser.close_tag_callback)
        self.assertEqual(result[1], test_list_of_data)
        self.assertEqual(result[2], test_counter_of_close_tags)
        self.assertEqual(open_tag_callback_mock.call_count, 54)


    @patch("src.html_parser_class.HtmlParser.close_tag_callback", return_value=True)
    def test_parse_html_close_tag_callback_mock(self, close_tag_callback_mock):
        """Тест на правильный парсинг"""
        parser = HtmlParser()
        fake = Faker(locale="Ru_ru")
        test_list_of_data = [fake.name() for i in range(10)]
        test_counter_of_open_tags = {'<html>': 1, '<persons>': 1, '<person>': 10, '<name>': 10}
        html = ["<person>" + "<name>" + test_list_of_data[i] + "</name>" + "</person>"
                for i in range(10)]
        html = "".join(html)
        html = '<html>' + "<persons>" + html + "</persons>" + '</html>'
        result = parser.parse_html(html, parser.open_tag_callback,
                                   parser.data_callback, parser.close_tag_callback)
        self.assertEqual(result[0], test_counter_of_open_tags)
        self.assertEqual(result[1], test_list_of_data)
        self.assertEqual(close_tag_callback_mock.call_count, 54)


if __name__ == '__main__':
    unittest.main()
