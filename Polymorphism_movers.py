class Mover:
    def move(self):
        pass  # Base behavior placeholder


class Car(Mover):
    def move(self):
        print("Driving on the highway 🚗")


class Plane(Mover):
    def move(self):
        print("Flying in the sky ✈️")


class Horse(Mover):
    def move(self):
        print("Galloping through the fields 🐎")


# Polymorphic behavior
def activate_movement(movers):
    for mover in movers:
        mover.move()


movers = [Car(), Plane(), Horse()]
activate_movement(movers)
