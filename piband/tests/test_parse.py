import unittest

from piband.MiBandState import MiBandState, ChargingState


class TestParser(unittest.TestCase):

    def test_parsing_wrong_state(self):
        data = [0x4e, 0x11, 0x00, 0x0c, 0x0d, 0x27, 0x29, 0x10,
                0x00, 0x05]
        state = MiBandState(None, data)
        self.assertEqual(ChargingState.UNKNOWN, state.charging)
        data = [0x4e, 0x11, 0x00, 0x0c, 0x0d, 0x27, 0x29, 0x10,
                0x00, 0x06]
        state = MiBandState(None, data)
        self.assertEqual(ChargingState.UNKNOWN, state.charging)
        data = [0x4e, 0x11, 0x00, 0x0c, 0x0d, 0x27, 0x29, 0x10,
                0x00, 0x00]
        state = MiBandState(None, data)
        self.assertEqual(ChargingState.UNKNOWN, state.charging)

    def test_parsing(self):
        data = [0x4e, 0x11, 0x00, 0x0c, 0x0d, 0x27, 0x29, 0x10,
                0x00, 0x04]
        state = MiBandState(None, data)
        self.assertEqual(78, state.battery)
        self.assertEqual(ChargingState.NOT_CHARGING, state.charging)

    def test_parsing2(self):
        data = [0x4e, 0x11, 0x00, 0x0c, 0x0d, 0x27, 0x29, 0x10,
                0x00, 0x04]
        state = MiBandState(None, data)
        self.assertEqual(78, state.battery)
        self.assertEqual(ChargingState.NOT_CHARGING, state.charging)

if __name__ == '__main__':
    unittest.main()
