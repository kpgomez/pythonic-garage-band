from abc import ABC

class Band:
    """
    Band is a collection of Musician instances
    """
    def __init__(self, name="unknown", members=None):
        self.name = name
        self.members = members or []

    def play_solos(self):
        # print(type(group.members)) shows <class 'list'>
        # print("type of group", type(group)) shows type of group <class 'pythonic_garage_band.band.Band'>
        # print("group", group) shows group <pythonic_garage_band.band.Band object at 0x102a924d0>

        group_members = []
        for member in self.members:
            group_members.append(member.play_solo())
        return group_members


class Musician(ABC):
    """
    Base class for different types of musicians
    """
    instrument = "unknown"
    def __init__(self, name):
        self.name = name

    def get_instrument(self):
        return self.instrument


class Guitarist(Musician):
    instrument = "guitar"
    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    def play_solo(self):
        return f"face melting {self.instrument} solo"

class Bassist(Musician):
    instrument = "bass"
    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"


    def play_solo(self):
        return "bom bom buh bom"


class Drummer(Musician):
    instrument = "drums"
    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    # def get_instrument(self):
    #     return self.instrument

    def play_solo(self):
        return "rattle boom crash"