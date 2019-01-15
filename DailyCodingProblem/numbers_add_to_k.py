# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?


class Solution:

    def numbers_add_to_k(self, seq, k):

        seen = set()
        for val in seq:
            candidate = k - val
            if candidate in seen:
                return candidate, val
            seen.add(val)

        return None

print(Solution().numbers_add_to_k([10, 15, 3, 7], 17))
