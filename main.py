# import Spaceship class
from spaceship import SpaceShip
from character import Character, People, Quarian, Krogan, Azari, Turians

def main():
    print("Создаем корабль")

    ship = SpaceShip("Normandy SR-1", "Human and Turians", "Federation", "Experimental reconnaissance frigate", "2183", "2183", "David Anderson Shepard")
    print(ship.__str__())
    # create an instance of the Crew class
    captain = People("David Anderson Shepard", "Human", "Captain")
    first_officer = Quarian("Tali'Zora", "Quarian", "First Officer")
    first_pilot = People("Kaidan Alenko", "Human", "First Pilot")
    second_pilot = Turians("Garrus Vakarian", "Turians", "Second Pilot")
    second_officer = Azari("Liara T'Soni", "Azari", "Second Officer")
    third_officer = Krogan("Wrex", "Krogan", "Third Officer")
    print("Создаем команду")
    crew = [captain, first_officer, first_pilot, second_pilot, second_officer, third_officer]
    for member in crew:
        print(member.__str__())

    print("Повышение от капитана")
    third_officer.change_rank("Best Officer")
    third_officer.space_message("I am the best officer")


if __name__ == '__main__':
    main()