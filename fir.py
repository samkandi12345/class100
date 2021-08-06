class Car(object):
    def __init__(self, safety, speed, milage ,cost ,brand):
        self.safety = safety,
        self.speed = speed,
        self.milage = milage,
        self.cost = cost,
        self.brand = brand

    def start(self):
        print("the car has started")

    def stop(self):
        print("the car has stopped")

Audi = Car("good",300,"10 kilometer per litre",100000,"audi")
print(Audi.stop())