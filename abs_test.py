import unittest
from abs import abs
from ddt import ddt,data,unpack

@ddt
class AbsTestCase(unittest.TestCase):

    def setUp(self):
        print("test method start ……>")

    @data([-1,1],[1,1],[0,0])
    @unpack
    def test_abs(self, n, expect_value):
        result = abs(n)
        self.assertEqual(result, expect_value, msg = result)

    def tearDown(self):
        print("test method end ……")

if __name__ == '__main__':
    unittest.main(verbosity=2)