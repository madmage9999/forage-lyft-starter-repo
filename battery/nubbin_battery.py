from battery.battery import Battery

class NubbinBattery(Battery):
    def __init__(self) -> None:
        super().__init__()

    def needs_service(self):
        return super().needs_service()