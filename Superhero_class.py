class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.__origin = origin  # Encapsulated

    def show_identity(self):
        print(f"{self.name} possesses the power of {self.power}.")

    def get_origin(self):  # Accessor for encapsulated attribute
        return self.__origin


class FlyingHero(Superhero):  # Inherited from Superhero
    def __init__(self, name, power, origin, flight_speed):
        super().__init__(name, power, origin)
        self.flight_speed = flight_speed

    def show_identity(self):
        print(f"{self.name} flies at {self.flight_speed} km/h with {self.power} power.")


# Instantiate objects
hero1 = Superhero("ShadowStrike", "Invisibility", "Moon City")
hero2 = FlyingHero("SkyFlash", "Speed", "Cloud Realm", 800)

hero1.show_identity()
print(f"Origin: {hero1.get_origin()}")  # Accessing encapsulated data
hero2.show_identity()
