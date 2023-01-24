import subprocess
import unittest

class TestScriptIntegration(unittest.TestCase):
    def test_script_output(self):
        process = subprocess.Popen(['python', 'script.py'], stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        stdout_str = stdout.decode("utf-8")

        self.assertIn("CPU Temperature", stdout_str)
        self.assertIn("Disk Usage", stdout_str)
        self.assertIn("%", stdout_str)
        self.assertRegex(stdout_str, r'\d+(\.\d+)? (°C|%)')

if __name__ == '__main__':
    unittest.main()