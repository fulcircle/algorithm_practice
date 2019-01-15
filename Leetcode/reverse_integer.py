# https://leetcode.com/problems/reverse-integer/
# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output: 321
# Example 2:

# Input: -123
# Output: -321
# Example 3:

# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

class Solution:
    def reverse(self, x):

        num = abs(x)

        place = 1
        reversed = 0

        while num >= 1:
            reversed = reversed*10 + (num % 10)
            num = num // 10
            place = place * 10

        if x < 0:
            reversed = -reversed

        if reversed < -2**31 or reversed > 2**31 - 1:
            return 0

        return reversed

print(Solution().reverse(-153))

