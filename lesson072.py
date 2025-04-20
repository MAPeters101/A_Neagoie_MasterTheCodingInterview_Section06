#print(self)

class My_Object:
    #print(self)
    def __init__(self):
        print(self)

    def func(self):
        print(self)

obj1 = My_Object()
obj1.func()
print('-'*80)

class Player:
    def __init__(self, name, type):
        print('player', self)
        self.name = name
        self.type = type

    def introduce(self):
        print(f"Hi, I am {self.name}, I'm a {self.type}")

class Wizard(Player):
    def __init__(self, name, type):
        super().__init__(name, type)
        print('wizard', self)

    def play(self):
        print(f"WEEEEE I'm a {self.type}")

wizard1 = Wizard('Shelly', 'Healer')
wizard2 = Wizard('Shawn', 'Dark Magic')
wizard1.introduce()
wizard1.play()
wizard2.introduce()
wizard2.play()


