# https://leetcode.com/problems/product-of-array-except-self/

# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# Example:

# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Note: Please solve it without division and in O(n).

# Follow up:
# Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

# # Initial solution
# class Solution:

#     def productExceptSelf(self, nums):
#         self.products = {}
#         return self.product_array(nums)

#     def product_array(self, nums):

#         product_array = [0]*len(nums)

#         for idx in range(0, len(nums)):
#             current_product = 1
#             for product_idx, product_val in enumerate(nums):
#                 if idx != product_idx:
#                     current_product = self.product(current_product, product_val)
#             product_array[idx] = current_product
            
#         return product_array

#     def product(self, left, right):
#         if (left, right) not in self.products:
#             product = left*right
#             self.products[(left, right)] = product
#             self.products[(right, left)] = product
        
#         return self.products[(left, right)]

# Second solution (copied)
class Solution:
    def productExceptSelf(self, nums):
        p = 1
        n = len(nums)
        output = []
        for i in range(0,n):
            output.append(p)
            p = p * nums[i]
        p = 1
        for i in range(n-1,-1,-1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output

arr = [1,2,3,4]
s = Solution()
print(s.productExceptSelf(arr))