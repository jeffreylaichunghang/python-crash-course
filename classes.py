# class
""" class TestClass:
    test_var = 'hello'
    another_var = 'something'

    def test_function(self):
        print('function in a class')
        print(self.test_var)
        self.another_func('123')

    def another_func(self, test_param):
        print(test_param)

# create an instance
test = TestClass()
test2 = TestClass()

test.another_var = 'new value'
print(test.test_var, test.another_var)
test2.test_function() """

# Dunder methods, (__init__ , __len__)
# mage class
""" class Mage:

    # similar to constructor
    def __init__(self, health, mana):
        self.health = health
        self.mana = mana
        print('mage class is created', self.health)

    def __len__(self):
        return self.health

    def attack(self, target):
        target.health -= 10

class Monster:
    health = 40

mage = Mage(100, 200)
monster = Monster()

print(monster.health)
mage.attack(monster)
print(monster.health) """


# inheritance

class Character:
    def __init__(self, health):
        self.health = health

    def attack(self):
        print('attack')

class Warrior(Character):
    def __init__(self, health, defense):
        super().__init__(health)
        self.defense = defense


class Barbarian(Character):
    def __init__(self, health, damage):
        super().__init__(health)
        self.damage = damage

class Monster(Character):
    def __init__(self, health):
        super().__init__(health)
        self.get_health()

    def get_health(self):
        print(f'a monster with {self.health} hp')

warrior = Warrior(50, 5.5)
barbarian = Barbarian(100, 8.1)
monster = Monster(100)
# warrior.attack()
# barbarian.attack()
