import unittest
import fibonacci

class TestCase(unittest.TestCase):
    def test_fib8(self):
        self.assertEqual(fibonacci.fib(8), 21)




if __name__ == '__main__':
    unittest.main(verbosity=2)


# 0 -> 0
# 1 -> 1
# 8 -> 21
