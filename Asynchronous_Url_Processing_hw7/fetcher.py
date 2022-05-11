"""Скрипт для асинхронной обкачки урлов"""
import sys
import argparse
import asyncio
import aiohttp


class Client:
    """Класс клиента"""
    def __init__(self, num_of_async_requests: int, file_name: str):
        """Метод класса __init__"""
        self.conn = aiohttp.TCPConnector(limit_per_host=num_of_async_requests,
                                         limit=num_of_async_requests)
        self.results = []
        with open(file_name, encoding="utf-8") as file:
            urls = file.readlines()
        self.urls = [string.strip() for string in urls]
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.get_url_info(num_of_async_requests))
        self.conn.close()
        print(f"Обработано {len(self.urls)} urls")

    async def get_url_info(self, num_of_async_requests):
        """Метод класса для обкачки url"""
        semaphore = asyncio.Semaphore(num_of_async_requests)
        client_session = aiohttp.ClientSession(connector=self.conn)

        async def get(url):
            """Метод для асинхронного чтения url"""
            async with semaphore:
                async with client_session.get(url, ssl=False) as response:
                    obj = await response.read()
                    self.results.append(obj)

        await asyncio.gather(*(get(url) for url in self.urls))
        await client_session.close()


def create_parser():
    """Функция для настройки запуска скрипта из консоли"""
    arg_conf = argparse.ArgumentParser()
    arg_conf.add_argument('-c',
                          '--number_of_asynchronous_requests',
                          default='50')
    arg_conf.add_argument('-f',
                          '--file_name',
                          default='urls.txt')
    return arg_conf


if __name__ == '__main__':
    arg_config = create_parser()
    namespace = arg_config.parse_args(sys.argv[1:])
    client = Client(int(namespace.number_of_asynchronous_requests),
                    str(namespace.file_name))
