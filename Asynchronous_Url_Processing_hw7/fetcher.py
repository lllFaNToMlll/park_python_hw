"""Скрипт для асинхронной обкачки урлов"""
import sys
import argparse
import asyncio
import aiohttp
import aiofiles


async def read_url(url, client):
    async with client.get(url) as resp:
        data = await resp.read()
        print(f'{url} содержит {len(data)} символов')


async def parse_urls(client, url_queue, queue_task):
    """Парсинг url"""
    while True:
        url = await url_queue.get()
        try:
            await read_url(url, client)
        except Exception as message:
            print(f'Ошибка: {message}')
        finally:
            url_queue.task_done()
        if queue_task.done() and url_queue.empty():
            return True


async def full_queue(url_queue, file_name):
    """Заполнение очереди из url"""
    async with aiofiles.open(file_name, mode='r') as file:
        async for url in file:
            await url_queue.put(url[:-1])


async def start_async_parse_urls(file_name, num_of_async_requests: int, queue_max_size: int):
    """Запуск асинхронного парсинга urls"""
    url_queue = asyncio.Queue(maxsize=queue_max_size)
    queue_task = asyncio.create_task(full_queue(url_queue, file_name))

    async with aiohttp.ClientSession() as client:
        tasks = [
            asyncio.create_task(parse_urls(client, url_queue, queue_task))
            for _ in range(num_of_async_requests)
        ]

        await url_queue.join()
        await queue_task
        await asyncio.wait(tasks)


def create_parser():
    """Функция для настройки запуска скрипта из консоли"""
    arg_conf = argparse.ArgumentParser()
    arg_conf.add_argument('-c',
                          '--number_of_asynchronous_requests',
                          default='5')
    arg_conf.add_argument('-f',
                          '--file_name',
                          default='urls.txt')
    return arg_conf

if __name__ == '__main__':
    arg_config = create_parser()
    namespace = arg_config.parse_args(sys.argv[1:])
    number_of_asynchronous_requests = int(namespace.number_of_asynchronous_requests)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        start_async_parse_urls(
            file_name=namespace.file_name,
            num_of_async_requests=number_of_asynchronous_requests,
            queue_max_size=2*number_of_asynchronous_requests
        )
    )
    print(f"Обкачка завершена")
