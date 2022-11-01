from cli import Margherita, Pepperoni, Hawaiian
import unittest

class TestMargherita(unittest.TestCase):
    """Тесты для класса Margherita"""

    def test_print_dict(self):
        """Проверяет, что вызов метода dict() корректно выводит ингредиенты"""
        new_order = Margherita('L')
        format = new_order.dict()

        self.assertEqual(format, "tomato_sauce, mozzarella, tomatoes")


class TestPepperoni(unittest.TestCase):
    """Тесты для класса Pepperoni"""

    def test_print_dict(self):
        """Проверяет, что вызов метода dict() корректно выводит ингредиенты"""
        new_order= Pepperoni('XL')
        format = new_order.dict()

        self.assertEqual(format, "tomato_sauce, mozzarella, pepperoni")


class TestHawaiian(unittest.TestCase):
    """Тесты для класса Hawaiian"""

    def test_print_dict(self):
        """Проверяет, что вызов метода dict() корректно выводит ингредиенты"""
        new_order= Hawaiian('L')
        format = new_order.dict()

        self.assertEqual(format, "tomato_sauce, mozzarella, chicken, pineapples")


if __name__ == '__name__':
    unittest.main()
