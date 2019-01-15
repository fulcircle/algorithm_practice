# Given a string, find the length of the longest substring without repeating characters.

# Example 1:

# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# Example 2:

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


# pseudocode
# start at i
# for i to i + 1,2,3, etc
#   if char at i + n already in set:
#       if current substring longer than last recorded longest:
#           make this longest
#       set i to next character c
#       set current_substring to ""
#       reset dictionary
#       break
#   otherwise:
#       add char at i + n to set

class Solution:
    def lengthOfLongestSubstring(self, s):

        longest = current_longest = 0

        seen = set()
        i = 0
        j = 0
        string_length = len(s)

        while i < string_length and j < string_length:

            if s[j] not in seen:
                seen.add(s[j])
                j += 1
                current_longest = j - i
                if longest < current_longest:
                    longest = current_longest

            else:
                seen.remove(s[i])
                i += 1

        return longest



assert(Solution().lengthOfLongestSubstring("abcabcbb") == 3)
assert(Solution().lengthOfLongestSubstring("bbbbb") == 1)
assert(Solution().lengthOfLongestSubstring("pwwkew") == 3)
assert(Solution().lengthOfLongestSubstring(" ") == 1)
assert(Solution().lengthOfLongestSubstring("dvdf") == 3)