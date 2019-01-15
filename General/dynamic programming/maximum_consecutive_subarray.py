def max_consecutive_subarray_dp(seq):
    length = len(seq)
    sums = [seq[0]]
    sums_max = sums[0]
    left = right = 0
    subsequence = (left, right)

    for i in range(1, length):
        sum_at_i = sums[i-1] + seq[i]
        sum_max = max(sum_at_i, seq[i])

        if sum_max == seq[i]:
            left = i
            right = i
        else:
            right = i

        sums.append(sum_max)
        if sums[i] > sums_max:
            sums_max = sums[i]
            subsequence = (left, right)

    return subsequence, sums_max


def max_consecutive_subarray_kadane(seq):
    length = len(seq)
    max_global = max_current = seq[0]
    left = right = 0
    subsequence = (left, right)

    for i in range(1, length):
        max_current = max(max_current + seq[i], seq[i])
        if max_current == seq[i]:
            left = i
            right = i
        else:
            right = i

        if max_current > max_global:
            max_global = max_current
            subsequence = (left, right)

    return subsequence, max_global


test_array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

assert(max_consecutive_subarray_dp(test_array) == ((3, 6), 6))
assert(max_consecutive_subarray_kadane(test_array) == ((3, 6), 6))