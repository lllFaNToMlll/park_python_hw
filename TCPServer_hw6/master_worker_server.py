"""
Класс master-worker сервера
"""
import sys
import threading
import urllib
from urllib.request import urlopen
import socket
import argparse
import json
from html_parser import HtmlParser


class MasterWorkerServer:
    """Класс master-worker сервера"""
    counter_of_url = 0

    def run_server(self, port: int, num_of_workers: int, top_k: int):
        """Фукнция запуска сервера"""
        server_socket = self.create_server_socket(port, num_of_workers)
        client_id = 1
        while True:
            try:
                client_socket = self.accept_client_connection(server_socket,
                                                              client_id)
                client_socket.setblocking(False)

                thread = threading.Thread(target=self.server_client_interaction,
                                          name=f"Worker thread for client № {client_id}",
                                          args=(client_socket, client_id, top_k, ))
                thread.start()

            except socket.error:
                print("Все worker заняты :(")

            else:
                client_id += 1

    def server_client_interaction(self, client_socket, client_id, top_k):
        """Функция для взаимодействия сервера с клиентом"""
        request = self.read_request(client_socket)
        if request is None:
            print(f'Клиент №{client_id} неожиданно отключился :(')
        else:
            self.handle_and_send_request(client_socket, client_id, request, top_k)

    @staticmethod
    def create_server_socket(server_port, num_of_workers):
        """Функция создания соккета TCP сервера"""
        server_socket = socket.socket(socket.AF_INET,
                                      socket.SOCK_STREAM,
                                      proto=0)
        server_socket.setsockopt(socket.SOL_SOCKET,
                                 socket.SO_REUSEADDR, 1)
        server_socket.bind(('127.0.0.1', server_port))
        server_socket.listen(num_of_workers)
        return server_socket

    @staticmethod
    def accept_client_connection(server_socket, client_id):
        """Функция для подключения клиента
           Возвращает соккет клиента"""
        client_socket, client_address = server_socket.accept()
        print(f'Клиент №{client_id} подключился к серверу: '
              f'{client_address[0]}: {client_address[1]}')
        return client_socket

    @staticmethod
    def read_request(client_socket):
        """Функция чтения запроса клиента"""
        request = bytearray()
        try:
            while True:
                client_request = client_socket.recv(1024)
                if not client_request:
                    # Клиент преждевременно отключился
                    return None

                request += client_request
                return request

        except ConnectionResetError:
            # Соединение было неожиданно разорвано
            return None

    def handle_and_send_request(self, client_socket, client_id, request, top_k):
        """Функция обработки запроса клиента
           и отправки результата клиенту"""
        parser = HtmlParser()
        url = request.decode('utf-8')
        try:
            with urlopen(url) as resp:
                result = parser.parse_html(resp.read().decode('utf-8'),
                                           parser.data_callback)
                result = parser.find_text(result, top_k)


        except urllib.error.HTTPError as e:
            result = {"message": str(e)}

        except Exception as e:
            print("Что-то пошло не так :(")
            result = {"message": str(e)}

        self.counter_of_url += 1
        print(f"Сервер обработал {self.counter_of_url} урлов")
        client_socket.sendall(json.dumps(result).encode("utf-8"))
        client_socket.close()
        print(f'Клиенту №{client_id} был отправлен ответ'
              f' на его запрос. Он отключен от сервера.')


def create_parser():
    arg_conf = argparse.ArgumentParser()
    arg_conf.add_argument('-p', '--port', default=9090)
    arg_conf.add_argument('-w', '--number_of_workers', default=4)
    arg_conf.add_argument('-k', '--top_k', default=3)
    return arg_conf


if __name__ == '__main__':
    arg_config = create_parser()
    namespace = arg_config.parse_args(sys.argv[1:])
    server = MasterWorkerServer()
    server.run_server(port=int(namespace.port),
                      num_of_workers=int(namespace.number_of_workers),
                      top_k=int(namespace.top_k))
