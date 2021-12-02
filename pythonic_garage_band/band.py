class Band:
    instances = []

    def __init__(self, name, members) -> None:
        self.name = name
        self.members = members
        self.__class__.instances.append(self)


    def play_solos(self):
        all_solos = []
        for member in self.members:
            all_solos.append(member.play_solo())
        return all_solos

    @classmethod
    def to_list(cls):
        return cls.instances


class Musician:

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} instance. Name = {self.name}"

class Guitarist(Musician):
    def __init__(self, name) -> None:
        self.name = name


    def __str__(self) -> str:
        return f'My name is {self.name} and I play guitar'

    def play_solo(self):
        return "face melting guitar solo"

    @staticmethod
    def get_instrument():
        return 'guitar'


class Bassist(Musician):
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"My name is {self.name} and I play bass"

    def play_solo(self):
        return "bom bom buh bom"


    @staticmethod
    def get_instrument():
        return 'bass'

class Drummer(Musician):
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"My name is {self.name} and I play drums"

    @staticmethod
    def play_solo():
        return 'rattle boom crash'
    
    @staticmethod
    def get_instrument():
        return 'drums'