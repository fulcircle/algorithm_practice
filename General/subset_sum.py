# Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.

import unittest


class SubsetSumRecursive:

    def __init__(self, nums, sum):

        self.nums = nums
        self.sum = sum
        self.found = False

    def run(self):
        return self.subset_sum(self.nums)

    def subset_sum(self, curr_nums):

        found = False
        for idx, value in enumerate(curr_nums):
            copy_curr_nums = curr_nums.copy()
            del copy_curr_nums[idx]
            if len(copy_curr_nums) == 0:
                continue
            if sum(copy_curr_nums) == self.sum:
                found = True
                break
            else:
                found = self.subset_sum(copy_curr_nums)
                if found:
                    break

        return found


class TestSubsetSum(unittest.TestCase):

    def test1(self):
        self.assertEqual(SubsetSumRecursive([3, 34, 4, 12, 5, 2], 9).run(), True)

    def test2(self):
        self.assertEqual(SubsetSumRecursive([3, 34, 4, 12, 5, 2], 1).run(), False)

    def test3(self):
        self.assertEqual(SubsetSumRecursive([], 1).run(), False)

    def test4(self):
        self.assertEqual(SubsetSumRecursive([2, 2, 2, 4, 56, 756], 6).run(), True)


if __name__ == '__main__':
    unittest.main()
