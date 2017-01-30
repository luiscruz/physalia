import unittest
from physalia.models import Measurement
import os


class TestMeasurement(unittest.TestCase):
    TEST_CSV_STORAGE = "./test_db.csv"

    def test_persist(self):
        Measurement.csv_storage = self.TEST_CSV_STORAGE
        self.addCleanup(self.clearDatabase)
        measurement = Measurement(
            1485634263.096069,
            'login',
            'Nexus5X',
            1000,
            1000,
            2,
            30
        )
        measurement.persist()
        with open(self.TEST_CSV_STORAGE, 'r') as f:
            content = f.read()
        self.assertTrue(
            """1485634263.096069,login,Nexus5X,1000,1000,2,30""" in content)

    def clearDatabase(self):
        os.remove(self.TEST_CSV_STORAGE)