from abc import ABC, abstractmethod
from engine import engine

class Car(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        pass

class Calliope(Car):
    self.engine = 

class CarFactory():
    def create_car(self, model):
        target_class = model
        return globals()[target_class]()