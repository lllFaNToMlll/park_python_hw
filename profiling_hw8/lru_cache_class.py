"""
Домашнее задание к лекции #5
1. LRU-кеш без OrderedDict (+тесты).
"""


class Node:
    """Класс элемента двусвязного списка"""
    def __init__(self, key=None, data=None):
        """Конструктор по умолчанию"""
        self.key = key
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        """Переопределение str"""
        return f"[{self.key}: {self.data}]"

    # def __eq__(self, other):
    #     """Перегрузка оператора =="""
    #     if ((self.key == other.key) and (self.data == other.data) and
    #             (self.next == other.next) and (self.prev == other.prev)):
    #         return True
    #     return False


class LRUCache:
    """Класс LRU кэширования, снованный на
    двусвязном списке и словаре (хеш-таблице)"""
    def __init__(self, limit=42):
        """Конструктор по умолчанию"""
        if limit <= 0:
            raise ValueError("limit должен быть > 0")
        self.limit = limit
        self.current_size_of_hash_table = 0
        self.hash_table = {}
        self.head = None
        self.tail = None

    def set_head(self, node):
        """Функция добавления нового элемента в начало списка"""
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

    def delete_node(self, node):
        """Функция удаления элемента из списка"""
        # если нет ни одного элемента в списке
        if not self.head:
            return None

        # удаляем голову
        if not node.prev:
            self.head = None
            self.tail = None
            self.current_size_of_hash_table -= 1
            return 1

        # удаляем хвост
        if not node.next:
            self.tail = self.tail.prev
            self.tail.next = None
            self.current_size_of_hash_table -= 1
            return 1

        # удаляем из середины
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
        self.current_size_of_hash_table -= 1
        return 1

    def get(self, key):
        """Функция получения элемента"""
        if key not in self.hash_table:
            return None

        node = self.hash_table[key]
        if not node.prev:
            return node.data

        self.delete_node(node)
        self.set_head(node)
        return node.data

    def set(self, key, value):
        """Функция добавления нового элемента"""
        if key in self.hash_table:
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


if __name__ == "__main__":
    pass
