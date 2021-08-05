import unittest
from sort import sort
from ddt import ddt,data,unpack

@ddt
class SortTestCase(unittest.TestCase):
   def setUp(self):
      print("test method start……")

   @data([0, 0, 0], [1, 0, 2], [1, 1, 10], [1, 2, 20])
   @unpack
   def test_sort(self, x, y, expect_value):
      result = sort(x, y)
      self.assertEqual(result, expect_value, msg=result)

   def tearDown(self):
      print("test method end ……")


if __name__ == '__main__':
 unittest.main(verbosity=2)