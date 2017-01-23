from enum import Enum


class ChargingState(Enum):
    LOW = 1
    CHARGING = 2
    FULL = 3
    NOT_CHARGING = 4
    UNKNOWN = 5


class MiBandState:
    def __init__(self, mac, data):
        self._data = data
        self.battery = data[0]
        self.mac = mac
        if 1 <= data[9] <= 4:
            self.charging = ChargingState(data[9])
        else:
            self.charging = ChargingState.UNKNOWN
