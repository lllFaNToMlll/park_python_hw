"""
Файл для профилирования вызовов
"""
import cProfile
import pstats
import io
import weakref
from lru_cache_class import LRUCache


class VeryImportantClassOrdinal:
    """Очень важный класс без слотов"""
    def __init__(self, very_important_value):
        self.x_num = very_important_value
        self.y_str = str(very_important_value)
        self.z_dict = {elem: str(elem) for elem in range(1, 50)}


class VeryImportantClassSlot:
    """Очень важный класс со слотами"""
    __slots__ = ("x_num", "y_str", "z_dict")

    def __init__(self, very_important_value):
        self.x_num = very_important_value
        self.y_str = str(very_important_value)
        self.z_dict = {elem: str(elem) for elem in range(1, 50)}


def add_to_lru_cache_ordinary_object(lru_cache, num_of_elements):
    """Функция добавления элементов в очень важный класс без слотов"""
    for i in range(num_of_elements):
        lru_cache.set("k"+str(i), VeryImportantClassOrdinal(i))


def add_to_lru_cache_slot(lru_cache, num_of_elements):
    """Функция добавления элементов в очень важный класс со слотами"""
    for i in range(num_of_elements):
        lru_cache.set("k"+str(i), VeryImportantClassSlot(i))


if __name__ == "__main__":
    pr = cProfile.Profile()
    pr.enable()

    cache_ordinary = LRUCache(10_000)
    add_to_lru_cache_ordinary_object(cache_ordinary, 15_000)
    print(cache_ordinary.current_size_of_hash_table)
    print(cache_ordinary.limit)

    cache_slot = LRUCache(10_000)
    add_to_lru_cache_slot(cache_slot, 15_000)
    print(cache_slot.current_size_of_hash_table)
    print(cache_slot.limit)

    weakref.ref(cache_ordinary)
    weakref.ref(cache_slot)

    pr.disable()

    out = io.StringIO()
    ps = pstats.Stats(pr, stream=out)
    ps.print_stats()

    print(out.getvalue())
