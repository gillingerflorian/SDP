#!/usr/bin/env python3
import unittest
import app

class TestScript(unittest.TestCase):
    def test_get_cpu_temp(self):
        temp, _ = app.get_both()
        self.assertIsInstance(temp, float)
        self.assertGreaterEqual(temp, 0)

    def test_get_disk_usage(self):
        _, disk_usage = app.get_both()
        self.assertIsInstance(disk_usage, str)
        

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestScript)
    unittest.TextTestRunner(verbosity=2).run(suite)
