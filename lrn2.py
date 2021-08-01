class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')


player1 = PlayerCharacter('Tom', 33)

print(player1.name)
print(player1.age)
print(player1)
