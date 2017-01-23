from __future__ import print_function

import sys
from bluetooth.ble import GATTRequester
import codecs

from piband.MiBandState import MiBandState

BatteryUUID = "0000ff0c-0000-1000-8000-00805f9b34fb"


def read_MiBand(mac):
    """
    Read mi band state bu mac
    :type mac: str
    :rtype: MiBandState
    :param mac: bluetouth mac of miband
    :return: state of mi band
    """
    requester = GATTRequester(mac, False)
    requester.connect(True)
    data = requester.read_by_uuid(
        BatteryUUID)
    print("Device name: ")
    return MiBandState(mac, data[0].encode())
