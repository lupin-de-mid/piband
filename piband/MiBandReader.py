from bluetooth.ble import GATTRequester

from piband.MiBandState import MiBandState

BatteryUUID = "0000ff0c-0000-1000-8000-00805f9b34fb"

def read_MiBand(mac):
    """
    Read mi band state by mac.

    :type mac: str
    :rtype: MiBandState
    :param mac: bluetouth mac of miband
    :return: state of mi band
    """
    requester = GATTRequester(mac, False)
    requester.connect(True)
    data = requester.read_by_uuid(
        BatteryUUID)
    return MiBandState(mac, data[0].encode())
