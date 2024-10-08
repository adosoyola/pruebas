import unittest
from mcd import mcd, mcd_four

class TestMCD(unittest.TestCase):

    def test_mcd(self):
        self.assertEqual(mcd(48, 18), 6)
        self.assertEqual(mcd(100, 75), 25)
        self.assertEqual(mcd(54, 24), 6)
        self.assertEqual(mcd(7, 1), 1)
        self.assertEqual(mcd(0, 5), 5)
     

    def test_mcd_four(self):
        self.assertEqual(mcd_four(48, 18, 24, 30), 6)
        self.assertEqual(mcd_four(100, 75, 25, 50), 25)
        self.assertEqual(mcd_four(54, 24, 18, 12), 6)
        self.assertEqual(mcd_four(7, 1, 0, 0), 1)
        self.assertEqual(mcd_four(0, 0, 0, 0), 0)

if __name__ == '__main__':
    unittest.main()


