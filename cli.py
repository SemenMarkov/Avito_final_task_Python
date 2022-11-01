from abc import ABC, abstractmethod
import click
from random import randint

class Pizza(ABC):
    """Абстрактный класс, который будут наследовать все потомки пиццы"""
    def __init__(self, size: str):
        self.size = size
        condition = size in ('L', 'XL') # проверка корректного ввода размера пиццы клиентом
        assert condition, 'The available sizes are L and XL'

    @abstractmethod
    def dict(self):
        """Абстрактный метод, который публикует список ингредиентов для каждого вида пиццы"""
        pass

class Margherita(Pizza):
    """Класс для пиццы с названием Маргарита, который наследует абстрактный класс Pizza"""
    @classmethod
    def dict(self):
        """Выводит список ингридиентов пиццы Маргарита"""
        return 'tomato_sauce, mozzarella, tomatoes'


    def __eq__(self, other):
        """Проверка являются ли экземпляры класса представителями одного и того же класса Margherita"""
        print('margherita eq')
        return self is other

class Pepperoni(Pizza):
    """Класс для пиццы с названием Маргарита, который наследует абстрактный класс Pizza"""
    @classmethod
    def dict(self):
        """Выводит список ингридиентов пиццы Пеперони"""
        return 'tomato_sauce, mozzarella, pepperoni'


    def __eq__(self, other):
        print('pepperoni eq')
        return self is other

class Hawaiian(Pizza):
    """Класс для пиццы с названием Гавайская, который наследует абстрактный класс Pizza"""
    @classmethod
    def dict(self):
        """Выводит список ингридиентов пиццы Гавайская"""
        return 'tomato_sauce, mozzarella, chicken, pineapples'


    def __eq__(self, other):
        print('hawaiian eq')
        return self is other


def outer_pattern(arg):
    """Декоратор декоратара, принимающий шаблон, в который возвращается результат функции"""
    def name_time_of_function(function):
        def wrapped(*args):
            res = function(*args)
            print(arg.format(randint(1, 10)))
            return res
        return wrapped
    return name_time_of_function

@click.group()
def cli():
    pass

@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool):
    """Готовит и доставляет пиццу"""
    bake({pizza})
    if delivery:
        deliver({pizza})


@cli.command()
def menu():
    """Выводит меню"""
    click.echo(f'— {Margherita.__name__} 🧀: {Margherita.dict()}')
    click.echo(f'— {Pepperoni.__name__} 🍕: {Pepperoni.dict()}')
    click.echo(f'— {Hawaiian.__name__} 🍍: {Hawaiian.dict()}')
#
#
@outer_pattern('👨‍🍳 Приготовили за {}с!')
def bake(pizza):
    """Готовит пиццу"""
    pass

@outer_pattern('🛵 Доставили за {}с!')
def deliver(pizza):
    """Доставляет пиццу"""
    pass

@outer_pattern('🏠 Забрали за {}с!')
def pickup(pizza):
    """Самовывоз"""
    pass




if __name__ == '__main__':
    cli()
