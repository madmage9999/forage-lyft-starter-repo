import unittest

from datetime import date

from nubbin_battery_test import NubbinBattery

class TestNubbinBattert(unittest.TestCase):
    def test_true(self):
        today = date.today()
        prev = date.fromisoformat("2016-01-01")
        bat = NubbinBattery(today, prev)
        self.assertTrue(battery.needs_service())
    