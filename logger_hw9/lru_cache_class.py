"""
Файл с классом LRUCache
"""
import sys
import argparse
import logging


class Node:
    """Класс элемента двусвязного списка"""
    def __init__(self, key=None, data=None):
        """Конструктор по умолчанию"""
        logging.info("Создается новый елемент двусвязного списка")
        self.key = key
        self.data = data
        self.next = None
        self.prev = None
        logging.info("Новый елемент двусвязного списка создан")

    def __str__(self):
        """Переопределение str"""
        return f"[{self.key}: {self.data}]"


class LRUCache:
    """Класс LRU кэширования, снованный на
    двусвязном списке и словаре (хеш-таблице)"""
    def __init__(self, limit=42):
        """Конструктор по умолчанию"""
        logging.info("Создается LRUCache")
        if limit <= 0:
            raise ValueError("limit должен быть > 0")
        self.limit = limit
        self.current_size_of_hash_table = 0
        self.hash_table = {}
        self.head = None
        self.tail = None
        logging.info("LRUCache создан")

    def set_head(self, node):
        """Функция добавления нового элемента в начало списка"""
        logging.info("Добавляем новый элемент в начало списка LRUCache")
        if not self.head:
            self.head = node
            self.tail = node
            self.current_size_of_hash_table += 1

        else:
            node.prev = None
            node.next = self.head
            self.head.prev = node
            self.head = node
            self.current_size_of_hash_table += 1
        logging.info("Новый элемент в начало списка LRUCache добавлен")

    def delete_node(self, node):
        """Функция удаления элемента из списка"""
        logging.info("Удаляем элемент из списка LRUCache")
        # если нет ни одного элемента в списке
        if not self.head:
            logging.info("Нет ни одного элемента в списке LRUCache")
            return None

        # удаляем голову
        if not node.prev:
            self.head = None
            self.tail = None
            self.current_size_of_hash_table -= 1
            logging.info("Удалили голову списка LRUCache")
            return 1

        # удаляем хвост
        if not node.next:
            self.tail = self.tail.prev
            self.tail.next = None
            self.current_size_of_hash_table -= 1
            logging.info("Удаляем хвост списка LRUCache")
            return 1

        # удаляем из середины
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
        self.current_size_of_hash_table -= 1
        logging.info("Удаляем из середины списка LRUCache")
        return 1

    def get(self, key):
        """Функция получения элемента"""
        logging.info("Пытаемся получить элемент из списка LRUCache")
        if key not in self.hash_table:
            logging.info("Такого элемента в списке LRUCache нет")
            return None

        node = self.hash_table[key]
        if not node.prev:
            logging.info("Вернули голову из списка LRUCache")
            return node.data

        self.delete_node(node)
        self.set_head(node)
        logging.info(
            "Вернули элемент из середины и назначили его головой списка LRUCache"
        )
        return node.data

    def set(self, key, value):
        """Функция добавления нового элемента"""
        logging.info("Добавляем элемент в список LRUCache")
        if key in self.hash_table:
            logging.info("Этот элемент уже есть в LRUCache")
            node = self.hash_table[key]
            node.data = value
            if node != self.head:
                self.delete_node(node)
                self.set_head(node)

        else:
            new_node = Node(key, value)
            if self.current_size_of_hash_table == self.limit:
                # удаляем из хеш-таблицы
                del self.hash_table[self.tail.key]
                # удаляем из списка
                self.delete_node(self.tail)
            self.set_head(new_node)
            self.hash_table[key] = new_node
            logging.info("Добавили новый элемент в LRUCache")

    def __str__(self):
        """Переопределение str"""
        current_node = self.head
        result = ""
        while current_node:
            if current_node.next:
                result += f"{current_node} <==> "
            else:
                result += f"{current_node}"
            current_node = current_node.next
        return result


def create_parser():
    arg_conf = argparse.ArgumentParser()
    arg_conf.add_argument('-s', '--log_to_console', default=False)
    return arg_conf


if __name__ == '__main__':
    arg_config = create_parser()
    namespace = arg_config.parse_args(sys.argv[1:])
    logging.basicConfig(
        filename="cache.log",
        level=logging.INFO,
        format="%(asctime)s\t%(levelname)s\t%(message)s",
        filemode='w',
    )
    if bool(namespace.log_to_console):
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] => %(message)s')
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)

    cache = LRUCache(2)

    cache.set("k1", "val1")
    cache.set("k2", "val2")

    print(cache.get("k3"))  # None
    print(cache.get("k2"))  # "val2"
    print(cache.get("k1"))  # "val1"

    cache.set("k3", "val3")

    print(cache.get("k3"))  # "val3"
    print(cache.get("k2"))  # None
    print(cache.get("k1"))  # "val1"

if __name__ == "__main__":
    pass
