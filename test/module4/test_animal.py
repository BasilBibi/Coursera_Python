import unittest
import sys
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

        print(dir(a))
        print(type(a))

        print(sys.getrefcount(a))

        l = [a]
        print(sys.getrefcount(a))

        l = [1,2,3]
        print(sys.getrefcount(a))

        self.assertNotEqual( anotherAnimal, a)

        print('here')


if __name__ == '__main__':
    unittest.main()
