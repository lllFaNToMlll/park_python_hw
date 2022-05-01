"""Класс клиента. Параметры запуска:  количество потоков, имя файла"""
import sys
import socket
import threading
import argparse
import json


class Client:
    """Класс клиента"""
    @staticmethod
    def get_url_info(urls):
        for url in urls:
            while True:
                try:
                    print(f"Клиент отправил серверу: {url}")
                    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    client_sock.connect(('127.0.0.1', 9090))
                    byte_url = bytes(url, encoding='utf-8')
                    client_sock.sendall(byte_url)
                    data = client_sock.recv(1024)
                except ConnectionResetError:
                    print("Все worker заняты :(")
                except socket.error:
                    print("Сервер умер :(")
                else:
                    print(f'Клиент получил от сервера: '
                          f'{url}', json.loads(data.decode("utf-8")))
                    client_sock.close()
                    break

    @staticmethod
    def create_butches(urls, number_of_butches):
        urls_butches = []
        for i in range(number_of_butches):
            urls_butches.append(
                urls[int(i * len(urls) / number_of_butches):
                     int((i + 1) * len(urls) / number_of_butches)])

        return urls_butches


    def __init__(self, number_of_threads: int, file_name: str):
        with open(file_name) as file:
            urls = file.readlines()
        urls = [string.strip() for string in urls]

        urls_butches = self.create_butches(urls, number_of_threads)

        threads = [
            threading.Thread(target=self.get_url_info,
                             name=f"Client thread №{i}",
                             args=(url_butch, ))
            for i, url_butch in enumerate(urls_butches)
        ]

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()


def create_parser():
    arg_conf = argparse.ArgumentParser()
    arg_conf.add_argument('-nt', '--number_of_threads', default='4')
    arg_conf.add_argument('-f', '--file_name', default='urls.txt')
    return arg_conf


if __name__ == '__main__':
    arg_config = create_parser()
    namespace = arg_config.parse_args(sys.argv[1:])
    client = Client(int(namespace.number_of_threads), str(namespace.file_name))
