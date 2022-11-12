class SpaceShip:
    def __init__(self, type, race, affiliation, status, built, destroyed, captain):
        self.type = type
        self.race = race
        self.affiliation = affiliation
        self.status = status
        self.built = built
        self.destroyed = destroyed
        self.captain = captain

    def __str__(self):
        return "Новый космический корабль: " + self.type + " " + self.race + " " + self.affiliation + " " + self.status + " " + self.built + " " + self.destroyed + " " + self.captain
