import discord


class Hamster:
    def __init__(self, hunger, energy, mood):
        self.__hunger = hunger
        self.__energy = energy
        self.__mood = mood

    def set_hunger(self, hunger):
        self.__hunger = hunger

    def set_energy(self, energy):
        self.__energy = energy

    def set_mood(self, mood):
        self.__mood = mood

    def get_hunger(self):
        return self.__hunger

    def get_energy(self):
        return self.__energy

    def get_mood(self):
        return self.__mood

    def msgResponse(self, message):
        pass
