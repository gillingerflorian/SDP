import unittest
import app


class TestIntegration(unittest.TestCase):
    def test_integration(self):
        temp, disk_usage = app.get_both()

        self.assertIsInstance(temp, float)
        self.assertGreaterEqual(temp, 0)

        self.assertIsInstance(disk_usage, str)


if __name__ == '__main__':
    unittest.main()
