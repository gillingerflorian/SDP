import unittest
import SensorNodes


class TestScript(unittest.TestCase):
    def test_get_cpu_temp(self):
        temp = SensorNodes.get_cpu_temp()
        self.assertIsInstance(temp, float)
        self.assertGreaterEqual(temp, 0)

    def test_get_disk_usage(self):
        disk_usage = SensorNodes.get_disk_usage()
        self.assertIsInstance(disk_usage, str)
        self.assertIn("%", disk_usage)

    def test_cpu_temp_under_40(self):
        SensorNodes.cpu_temp = 30
        self.assertEqual(SensorNodes.main(), "I'm cold")

    def test_cpu_temp_between_40_60(self):
        SensorNodes.cpu_temp = 50
        self.assertEqual(SensorNodes.main(), "All good, working temp")

    def test_cpu_temp_between_60_80(self):
        SensorNodes.cpu_temp = 70
        self.assertEqual(SensorNodes.main(), "Getting a little warm")

    def test_cpu_temp_over_80(self):
        SensorNodes.cpu_temp = 90
        self.assertEqual(SensorNodes.main(), "OVERHEATING!")


if __name__ == '__main__':
    unittest.main()