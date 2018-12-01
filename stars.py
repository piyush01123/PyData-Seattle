import unittest

def mySum(*args):
    return sum(args)

def mySumNew(*args, **kwargs):
    return sum(args) + sum(kwargs.values())

class SumTestCase(unittest.TestCase):
    def test_mySum(self):
        self.assertEqual(mySum(1,5,10), 16)
    def test_mySumNew(self):
        self.assertEqual(mySumNew(1, 3, x=5, y=7), 16)

if __name__=='__main__':
    unittest.main()
