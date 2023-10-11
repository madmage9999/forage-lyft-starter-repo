from battery.battery import Battery

class SpindlerBatter(Battery):
    def __init__(self) -> None:
        super().__init__()

    def needs_service(self):
        return super().needs_service()