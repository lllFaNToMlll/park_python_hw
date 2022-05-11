"""ТЕСТЫ"""
import unittest
from fetcher import Client


class MyTestCase(unittest.TestCase):
    """КЛАСС ДЛЯ ТЕСТОВ"""
    async def test_client(self):
        """ТЕСТ НА ПРАВИЛЬНОСТЬ РАБОТЫ"""
        client = Client(10, "urls.txt")
        self.assertEqual(len(client.results), 101)


if __name__ == '__main__':
    unittest.main()
