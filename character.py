class Character:
    def __init__(self, name, race, rank):
        self.name = name
        self.race = race
        self.rank = rank

    def say(self):
        print("Hello, my name is " + self.name)

    def change_rank(self, rank):
        self.rank = rank
        print("Поздравляем! Теперь вы " + self.rank)

    def space_message(self, message):
        print(self.name + ": " + message)

    def __str__(self):
        return self.name + " " + self.race + " " + self.rank


class People(Character):
    def say(self):
        print("Hello, my name is " + self.name + " and I am a people.")


class Quarian(Character):
    def say(self):
        print("Hello, my name is " + self.name + " and I am a quarian.")


class Krogan(Character):
    def say(self):
        print("Hello, my name is " + self.name + " and I am a krogan.")


class Azari(Character):
    def say(self):
        print("Hello, my name is " + self.name + " and I am an azari.")


class Turians(Character):
    def say(self):
        print("Hello, my name is " + self.name + " and I am a turian.")