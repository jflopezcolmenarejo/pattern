
import unittest
import app

class TestClass(unittest.TestCase):

    def test_add(self):
        self.assertEquals(app.add(10, 12), 22)
        self.assertEquals(app.add(10, -12), -2)

    def test_divide(self):
        self.assertEquals(app.divide(5, 2), 2.5)
        


if __name__ == "__main__":
    unittest.main()