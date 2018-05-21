import unittest
from coursera_python.module4.AnimalClass import Animal

from test.TestBase import *


class AnimalTests(unittest.TestCase):

    def test_length_results_list(self):
        a = Animal(sex='M')
        print(a)
        anotherAnimal = Animal(colour='blue', sex='M')
        print(anotherAnimal)

        a.move()
        a.move()
        a.move()
        a.eat()

        print(a.__hash__())

        for k,v in a.__dict__.items():
            print(f'{k}, {v}')

        self.assertNotEqual( anotherAnimal, a)


if __name__ == '__main__':
    unittest.main()
