class Animal:

    def __init__(self, colour='Jazzy Red', sex='F', number_of_meals_eaten=0, distance_moved=0):
        self.colour = colour
        self.sex = sex
        self.number_of_meals_eaten = number_of_meals_eaten
        self.distance_moved = distance_moved

    def move(self):
        self.distance_moved = self.distance_moved + 1
        print(f'Animal move() method called. distance_moved {self.distance_moved}')

    def eat(self):
        self.number_of_meals_eaten = self.number_of_meals_eaten + 1
        print(f'Animal eat() method called. meals {self.number_of_meals_eaten}')

    def __eq__(self, other):
        print('__eq__ called')
        return isinstance(other, self.__class__ ) \
               and self.colour == other.colour \
               and self.sex == other.sex

    def __hash__(self):
        print('__hash__ called')
        return hash(self.colour) ^ hash(self.sex) ^ hash(self.number_of_meals_eaten) ^ hash(self.distance_moved)

    def __str__(self):
        print('__str__ called')
        return f'Animal(colour={self.colour}, sex={self.sex}, number_of_meals_eaten={self.number_of_meals_eaten}, ' +\
               f'distance_moved={self.distance_moved})'

    def __del__(self):
        print(f'__del__ called on {self}')
