
class Vehicule:
    def move(self):
        pass

class Car(Vehicule):
    def move(self):
        print("Driving")

class Plane(Vehicule):
    def move(self):
        print("Flying")


car = Car()
car.move()

plane = Plane()
plane.move()