"""ТЕСТЫ"""
import unittest
import asyncio
from unittest.mock import patch
import aiohttp
from fetcher import full_queue, parse_urls


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
        urls = ['https://habr.com/ru/post/3232/', 'https://habr.com/ru/post/3233/',
                'https://habr.com/ru/post/3234/']
        url_queue = asyncio.Queue(maxsize=len(urls)*2)
        queue_task = asyncio.create_task(mock_full_queue(urls, url_queue))

        async with aiohttp.ClientSession() as session:
            self.assertTrue(await parse_urls_mock(session, url_queue, queue_task))

    @patch("fetcher.read_url", return_value=1234)
    async def test_parse_urls_read_url_mock(self, read_url_mock):
        """Тест функции парсинга url"""
        urls = ['https://habr.com/ru/post/3232/', 'https://habr.com/ru/post/3233/',
                'https://habr.com/ru/post/3234/']
        url_queue = asyncio.Queue(maxsize=len(urls) * 2)
        queue_task = asyncio.create_task(mock_full_queue(urls, url_queue))

        async with aiohttp.ClientSession() as session:
            self.assertTrue(await parse_urls(session, url_queue, queue_task))

    # @patch("fetcher.start_async_parse_urls", return_value=asyncio.Future())
    # async def test_start_async_parse_urls(self, start_async_parse_urls_mock):
    #     """Тест функции парсинга url"""
    #     loop = asyncio.get_event_loop()
    #     res = loop.run_until_complete(
    #         start_async_parse_urls_mock(file_name='urls.txt',
    #                                     num_of_async_requests=5,
    #                                     queue_max_size=2 * 5
    #                                     )
    #     )
    #     f = asyncio.Future()
    #     f.set_result(True)
    #     self.assertTrue(res, f)


if __name__ == '__main__':
    unittest.main()

