import unittest

from ddt import ddt, data, unpack


@ddt
class MyTestCase2(unittest.TestCase):
    @data((1, 2), (2, 3))
    @unpack
    def test_tuple(self, value1, value2):
        print(value1, value2)
        print(value1 + 1, value2)
        self.assertEqual(value2, value1 + 1)

    @data([1, 2], [2, 3])
    @unpack
    def test_list(self, value1, value2):
        print(value1, value2)
        self.assertEqual(value2, value1 + 1)

    @data({'value1': 1, 'value2': 2}, {'value1': 1, 'value2': 2})
    @unpack
    def test_dict(self, value1, value2):
        print(value1, value2)
        self.assertEqual(value2, value1 + 1)


if __name__ == '__main__':
    unittest.main()
