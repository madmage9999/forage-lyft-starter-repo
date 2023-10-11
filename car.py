from abc import ABC, abstractmethod
from engine import engine

class Car(ABC):
    def __init__(self, last_service_date, engine, battery):
        self.last_service_date = last_service_date
        self.engine = engine
        self.battery = battery

    @abstractmethod
    def needs_service(self):
        pass

class Calliope(Car):
    def __init__(self):
        super().__init__("Capulet Engine", "Spindler Battery")

class Glissade(Car):
    def __init__(self):
        super().__init__("Willoughby Engine", "Spindler Battery")

class Palindrome(Car):
    def __init__(self):
        super().__init__("Sternman Engine", "Spindler Battery")

class Rorschach(Car):
    def __init__(self):
        super().__init__("Willoughby Engine", "Nubbin Battery")

class Thovex(Car):
    def __init__(self):
        super().__init__("Capulet Engine", "Nubbin Battery")
class CarFactory():
    def create_car(self, model):
        target_class = model
        return globals()[target_class]()