"""
Тесты к классу LRUCache и Node
"""
import unittest
from lru_cache_class import LRUCache, Node


class MyTestCase(unittest.TestCase):
    """ Класс для юнит тестов"""
    def test_node_init(self):
        """Тест на проверку работы инициализации"""
        node = Node()
        self.assertEqual(node.key, None)
        self.assertEqual(node.data, None)
        self.assertEqual(node.next, None)
        self.assertEqual(node.prev, None)

        node = Node("k1", "val1")
        self.assertEqual(node.key, "k1")
        self.assertEqual(node.data, "val1")
        self.assertEqual(node.next, None)
        self.assertEqual(node.prev, None)

    def test_node_str(self):
        """Тест на правильную работу функции str()"""
        node = Node("k1", "val1")
        self.assertEqual(str(node), "[k1: val1]")

    def test_lru_cache_init(self):
        """Тест на проверку работы инициализации"""
        cache = LRUCache()
        self.assertEqual(cache.limit, 42)
        self.assertEqual(cache.current_size_of_hash_table, 0)
        self.assertEqual(cache.hash_table, {})
        self.assertEqual(cache.head, None)
        self.assertEqual(cache.tail, None)

        cache = LRUCache(6)
        self.assertEqual(cache.limit, 6)
        self.assertEqual(cache.current_size_of_hash_table, 0)
        self.assertEqual(cache.hash_table, {})
        self.assertEqual(cache.head, None)
        self.assertEqual(cache.tail, None)

        with self.assertRaises(ValueError):
            cache = LRUCache(-41)

    def test_set_head(self):
        """Тест функции добавления нового элемента в начало списка"""
        cache = LRUCache()
        new_node = Node("k1", "val1")
        cache.set_head(new_node)
        self.assertEqual(cache.head, new_node)
        new_node = Node("k2", "val2")
        cache.set_head(new_node)
        self.assertEqual(cache.head, new_node)

    def test_delete_node(self):
        """Тест функции удаления элемента из списка"""
        cache = LRUCache(3)
        self.assertEqual(cache.delete_node(Node("k3", "val3")), None)
        cache.set("k1", "val1")
        self.assertEqual(cache.delete_node(Node("k1", "val1")), 1)
        self.assertEqual(cache.current_size_of_hash_table, 0)
        cache.set("k1", "val1")
        cache.set("k2", "val2")
        self.assertEqual(cache.delete_node(Node("k1", "val1")), 1)
        self.assertEqual(cache.current_size_of_hash_table, 1)
        cache.set("k1", "val1")
        cache.set("k2", "val2")
        cache.set("k3", "val3")
        self.assertEqual(cache.delete_node(Node("k2", "val2")), 1)
        self.assertEqual(cache.current_size_of_hash_table, 2)

    def test_get(self):
        """Тест функции получения элемента"""
        cache = LRUCache(3)
        cache.set("k1", "val1")
        cache.set("k2", "val2")
        cache.set("k3", "val3")
        self.assertEqual(cache.get("k4"), None)
        self.assertEqual(cache.get("k3"), "val3")
        self.assertEqual(cache.get("k2"), "val2")
        self.assertEqual(cache.get("k1"), "val1")

    def test_set(self):
        """Тест функции добавления нового элемента"""
        cache = LRUCache(3)
        cache.set("k1", "val1")
        self.assertEqual(str(cache), "[k1: val1]")
        cache.set("k2", "val2")
        self.assertEqual(str(cache), "[k2: val2] "
                                     "<==> [k1: val1]")
        cache.set("k1", "val1")
        self.assertEqual(str(cache), "[k1: val1] "
                                     "<==> [k2: val2]")
        cache.set("k3", "val3")
        self.assertEqual(str(cache), "[k3: val3] "
                                     "<==> [k1: val1] "
                                     "<==> [k2: val2]")

    def test_lru_cache_str(self):
        """Тест на правильную работу функции str()"""
        cache = LRUCache(2)
        cache.set("k1", "val1")
        cache.set("k2", "val2")
        self.assertEqual(str(cache), "[k2: val2] "
                                     "<==> [k1: val1]")

    def test_logic_lru_cache(self):
        """Тест логики класса LRUCache"""
        cache = LRUCache(2)
        self.assertEqual(cache.current_size_of_hash_table, 0)
        self.assertEqual(cache.limit, 2)
        cache.set("k1", "val1")
        self.assertEqual(cache.current_size_of_hash_table, 1)
        self.assertEqual(cache.limit, 2)
        cache.set("k2", "val2")
        self.assertEqual(cache.current_size_of_hash_table, 2)
        self.assertEqual(cache.limit, 2)
        self.assertEqual(str(cache), "[k2: val2] "
                                     "<==> [k1: val1]")
        self.assertEqual(cache.get("k3"), None)
        self.assertEqual(cache.current_size_of_hash_table, 2)
        self.assertEqual(cache.limit, 2)
        self.assertEqual(cache.get("k2"), "val2")
        self.assertEqual(cache.current_size_of_hash_table, 2)
        self.assertEqual(cache.limit, 2)
        self.assertEqual(cache.get("k1"), "val1")
        self.assertEqual(cache.current_size_of_hash_table, 2)
        self.assertEqual(cache.limit, 2)
        self.assertEqual(str(cache), "[k1: val1] "
                                     "<==> [k2: val2]")
        cache.set("k3", "val3")
        self.assertEqual(cache.current_size_of_hash_table, 2)
        self.assertEqual(cache.limit, 2)
        self.assertEqual(str(cache), "[k3: val3] "
                                     "<==> [k1: val1]")
        self.assertEqual(cache.get("k3"), "val3")
        self.assertEqual(cache.current_size_of_hash_table, 2)
        self.assertEqual(cache.limit, 2)
        self.assertEqual(cache.get("k2"), None)
        self.assertEqual(cache.current_size_of_hash_table, 2)
        self.assertEqual(cache.limit, 2)
        self.assertEqual(cache.get("k1"), "val1")
        self.assertEqual(cache.current_size_of_hash_table, 2)
        self.assertEqual(cache.limit, 2)
        self.assertEqual(str(cache), "[k1: val1] "
                                     "<==> [k3: val3]")

    def test_logic_lru_cache_limit_1(self):
        """Тест логики класса LRUCache"""
        cache = LRUCache(1)
        self.assertEqual(cache.current_size_of_hash_table, 0)
        self.assertEqual(cache.limit, 1)
        cache.set("k1", "val1")
        self.assertEqual(cache.current_size_of_hash_table, 1)
        self.assertEqual(cache.limit, 1)
        cache.set("k2", "val2")
        self.assertEqual(cache.current_size_of_hash_table, 1)
        self.assertEqual(cache.limit, 1)
        self.assertEqual(str(cache), "[k2: val2]")
        self.assertEqual(cache.get("k3"), None)
        self.assertEqual(cache.current_size_of_hash_table, 1)
        self.assertEqual(cache.limit, 1)
        self.assertEqual(cache.get("k2"), "val2")
        self.assertEqual(cache.current_size_of_hash_table, 1)
        self.assertEqual(cache.limit, 1)
        self.assertEqual(cache.get("k1"), None)
        self.assertEqual(cache.current_size_of_hash_table, 1)
        self.assertEqual(cache.limit, 1)
        self.assertEqual(str(cache), "[k2: val2]")
        cache.set("k3", "val3")
        self.assertEqual(cache.current_size_of_hash_table, 1)
        self.assertEqual(cache.limit, 1)
        self.assertEqual(str(cache), "[k3: val3]")
        self.assertEqual(cache.get("k3"), "val3")
        self.assertEqual(cache.current_size_of_hash_table, 1)
        self.assertEqual(cache.limit, 1)
        self.assertEqual(cache.get("k2"), None)
        self.assertEqual(cache.current_size_of_hash_table, 1)
        self.assertEqual(cache.limit, 1)
        self.assertEqual(cache.get("k1"), None)
        self.assertEqual(cache.current_size_of_hash_table, 1)
        self.assertEqual(cache.limit, 1)
        self.assertEqual(str(cache), "[k3: val3]")

    def test_logic_lru_cache_del_all(self):
        """Тест логики класса LRUCache"""
        cache = LRUCache(2)
        self.assertEqual(cache.current_size_of_hash_table, 0)
        self.assertEqual(cache.limit, 2)
        cache.set("k1", "val1")
        self.assertEqual(cache.current_size_of_hash_table, 1)
        self.assertEqual(cache.limit, 2)
        cache.set("k2", "val2")
        self.assertEqual(cache.current_size_of_hash_table, 2)
        self.assertEqual(cache.limit, 2)
        self.assertEqual(str(cache), "[k2: val2] "
                                     "<==> [k1: val1]")
        self.assertEqual(cache.get("k3"), None)
        self.assertEqual(cache.get("k4"), None)
        cache.set("k3", "val3")
        cache.set("k4", "val4")
        self.assertEqual(cache.current_size_of_hash_table, 2)
        self.assertEqual(cache.limit, 2)
        self.assertEqual(str(cache), "[k4: val4] "
                                     "<==> [k3: val3]")
        self.assertEqual(cache.get("k3"), "val3")
        self.assertEqual(cache.current_size_of_hash_table, 2)
        self.assertEqual(cache.limit, 2)
        self.assertEqual(cache.get("k2"), None)
        self.assertEqual(cache.get("k1"), None)
        self.assertEqual(cache.current_size_of_hash_table, 2)
        self.assertEqual(cache.limit, 2)


if __name__ == '__main__':
    unittest.main()
