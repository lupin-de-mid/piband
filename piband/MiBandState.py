"""Contains public stuff fore mi band"""
import enum


class ChargingState(enum.Enum):
    """
    Possible state of mi band charging
    """
    LOW = 1
    CHARGING = 2
    FULL = 3
    NOT_CHARGING = 4
    UNKNOWN = 5


class MiBandState:
    """
    State of mi band battery
    """
    def __init__(self, mac, data):
        """
        Create new state
        :type data: bytearray
        :type mac: str
        :param mac:
        :param data:
        """
        self._data = data
        self.battery = data[0]
        self.mac = mac
        if 1 <= data[9] <= 4:
            self.charging = ChargingState(data[9])
        else:
            self.charging = ChargingState.UNKNOWN
