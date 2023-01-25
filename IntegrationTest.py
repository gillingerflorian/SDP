import unittest
import SensorNodesTest
import UnitTest

class TestIntegration(unittest.TestCase):
    def test_integration(self):
        temp, disk_usage = SensorNodesTest.main()

        self.assertIsInstance(temp, float)
        self.assertGreaterEqual(temp, 0)

        self.assertIsInstance(disk_usage, str)
        self.assertIn("%", disk_usage)

if __name__ == '__main__':
    unittest.main()