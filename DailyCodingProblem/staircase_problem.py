# https://www.dailycodingproblem.com/blog/staircase-problem/

class Solution:

    # If can we only take 1 or 2 steps up
    def solve_staircase_recursive(self, n):

        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.solve_staircase_recursive(n-1) + self.solve_staircase_recursive(n-2)

    # If we can only take 1 or 2 steps up
    def solve_staircase_dp(self, n):

        sums = [0, 1, 2]
        for i in range(0, n+1):
            if i > 2:
                sums.append(sums[i-1] + sums[i-2])

        return sums[-1]

    # Now we can take an arbitrary list of possible step values
    def solve_staircase_dp_2(self, n, X):

        sums = [0]*(n+1)
        for i in range(0, n+1):
            for j in X:
                if j < i:
                    sums[i] += sums[i - j]
            if i in X:
                sums[i] += 1

        return sums[-1]

assert(Solution().solve_staircase_recursive(5) == 8)
assert(Solution().solve_staircase_dp(5) == 8)
assert(Solution().solve_staircase_dp_2(5, [1, 2]) == 8)
assert(Solution().solve_staircase_dp_2(8, [1, 3, 5]) == 19)