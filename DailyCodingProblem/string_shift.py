# Given two strings A and B, return whether or not A can be shifted some number of times to get B.
#
# For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false.
#
# We will be sending the solution tomorrow, along with tomorrow's question. As always, feel free to shoot us an email if there's anything we can help with.
#

import unittest


def string_shift(string1, string2):

    string1_length = len(string1)
    string2_length = len(string2)

    if string1_length != string2_length:
        return False

    string1_index = 0
    string2_index = 0
    string2_counter = 0

    while string1_index < string1_length:

        if string1[string1_index] == string2[string2_index]:
            string1_index += 1
            string2_index += 1

        else:
            string1_index = 0
            string2_index += 1

            string2_counter += 1
            if string2_counter == string2_length:
                return False

        if string2_index == string2_length:
            string2_index = 0

    return True


class TestStringShift(unittest.TestCase):

    def test1(self):
        self.assertEqual(string_shift('abcde', 'cdeab'), True)

    def test2(self):
        self.assertEqual(string_shift('abc', 'acb'), False)

    def test3(self):
        self.assertEqual(string_shift('aaaaabc', 'bcaaaaa'), True)

    def test4(self):
        self.assertEqual(string_shift('aaaaabc', 'bdaaaaa'), False)

    def test5(self):
        self.assertEqual(string_shift('', ''), True)

    def test6(self):
        self.assertEqual(string_shift('asdfl', 'a'), False)


if __name__ == '__main__':
    unittest.main()

