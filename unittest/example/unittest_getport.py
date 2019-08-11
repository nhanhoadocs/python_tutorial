import unittest
from getport import get_port

class TestgetPort(unittest.TestCase):
    def test_no_error(self):
        """
        Test co return lai port
        """
        data="8.8.8.8"
        result = get_port(data)
        self.assertEqual(result, "53:dns-udp")

    def test_error(self):
        data="11111"
        result = get_port(data)
        self.assertEqual(result, "Error!!!")

if __name__ == '__main__':
    unittest.main()