class Vehicle:
    def run(self):
        print('Can run')


class Car(Vehicle):
    def number_of_wheels(self):
        print('Has 4 wheels')


class Bus(Vehicle):
    def carry(self):
        print('Can carry passengers')


carObject = Car()
carObject.number_of_wheels()
carObject.run()