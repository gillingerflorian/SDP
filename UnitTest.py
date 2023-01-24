#!/usr/bin/env python3
import unittest
import SensorNodesTest

class TestScript(unittest.TestCase):
    def test_get_cpu_temp(self):
        temp, _ = SensorNodesTest.main()
        self.assertIsInstance(temp, float)
        self.assertGreaterEqual(temp, 0)

    def test_get_disk_usage(self):
        _, disk_usage = SensorNodesTest.main()
        self.assertIsInstance(disk_usage, str)
        self.assertIn("%", disk_usage)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestScript)
    unittest.TextTestRunner(verbosity=2).run(suite)