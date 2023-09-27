from abc import ABC

class Band:
    """
    Band is a collection of Musician instances
    """
    def __init__(self, name="unknown", members=None):
        self.name = name
        self.members = members or []

    def play_solos(members):
        return members


class Musician(ABC):
    """
    Base class for different types of musicians
    """
    def __init__(self, name):
        self.name = name

    # def get_instrument(self):
    #     return self.instrument


class Guitarist(Musician):
    instrument = "guitar"
    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return f"face melting {self.instrument} solo"

class Bassist(Musician):
    instrument = "bass"
    def __str__(self):
        return f"My name is {self.name} and I play bass"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"


    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return "bom bom buh bom"


class Drummer(Musician):
    instrument = "drums"
    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return "rattle boom crash"