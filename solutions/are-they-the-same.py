import unittest


def comp(array1, array2):
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False


class Test(unittest.TestCase):
    def test(self):
        a1 = [121, 144, 19, 161, 19, 144, 19, 11]
        a2 = [11 * 11, 121 * 121, 144 * 144, 19 * 19,
              161 * 161, 19 * 19, 144 * 144, 19 * 19]
        self.assertTrue(comp(a1, a2))

        a = [121, 144, 19, 161, 19, 144, 19, 11]
        b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
        self.assertFalse(comp(a, b))


if __name__ == '__main__':
    unittest.main()
