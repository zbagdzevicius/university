from UnfairSet.UnfairSet import UnfairSet
import unittest

class TestStringMethods(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance = UnfairSet()
        self.testing_character = 'a'
        self.bad_string = 'aa'

    def test_add(self):
        self.assertNotEqual(f'character {self.testing_character} already exist', self.instance.add(self.testing_character))
        self.instance.add(self.testing_character)
        self.assertEqual(f'character {self.testing_character} already exist', self.instance.add(self.testing_character))
        with self.assertRaises(ValueError):
            self.instance.add(self.bad_string)

    def test_remove(self):
        self.instance.add(self.testing_character)
        self.assertEqual(self.instance.remove(self.testing_character), f'removed: {self.testing_character}')
        with self.assertRaises(ValueError):
            self.instance.remove(self.bad_string)

    def test_size(self):
        self.assertEqual(self.instance.size(), len(self.instance.UnfairSet))

    def test_is_in(self):
        self.instance.add(self.testing_character)
        self.assertTrue(self.instance.is_in(self.testing_character))
        self.assertFalse(self.instance.is_in('AA'))


if __name__ == '__main__':
    unittest.main()
