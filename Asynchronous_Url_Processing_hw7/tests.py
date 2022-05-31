"""ТЕСТЫ"""
import unittest
import asyncio
from unittest.mock import patch
import aiohttp
from fetcher import full_queue


async def mock_full_queue(urls, url_queue):
    for url in urls:
        await url_queue.put(url[:-1])


class MyTestCase(unittest.IsolatedAsyncioTestCase):
    """Класс для тестов"""
    async def test_full_queue(self):
        """Тест функции создания очереди из url"""
        with open('urls.txt') as file:
            expected_urls = file.readlines()
        expected_urls = [string[:-1].strip() for string in expected_urls]

        url_queue = asyncio.Queue(maxsize=4)
        task = asyncio.create_task(full_queue(url_queue, 'urls.txt'))

        for url in expected_urls:
            self.assertEqual(await url_queue.get(), url)
            url_queue.task_done()
        task.cancel()

    @patch("fetcher.parse_urls", return_value=True)
    async def test_parse_urls(self, parse_urls_mock):
        """Тест функции парсинга url"""
        f = asyncio.Future()
        f.set_result(True)
        urls = ['https://habr.com/ru/post/3232/', 'https://habr.com/ru/post/3233/',
                'https://habr.com/ru/post/3234/']
        url_queue = asyncio.Queue(maxsize=len(urls)*2)
        queue_task = asyncio.create_task(mock_full_queue(urls, url_queue))

        async with aiohttp.ClientSession() as session:
            self.assertEqual(await parse_urls_mock(session, url_queue, queue_task), True)


if __name__ == '__main__':
    unittest.main()

