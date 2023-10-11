from abc import ABC


class Engine(ABC):
    def __init__(self, needs_service) -> None:
        self.needs_service = needs_service
    

