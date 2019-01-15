# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def advanceNode(self, node):
        if node == None:
            return None
        else:
            return node.next

    def createAndAdvance(self, node, val=None):
        node.next = ListNode(val)
        return node.next

    def createNode(self, val=None):
        return ListNode(val)

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        current_l1 = l1
        current_l2 = l2
        
        carry = 0
        sum_list = None
        current_sum_list = None
        
        while current_l1 != None or current_l2 != None:
            if current_sum_list == None:
                sum_list = self.createNode()
                current_sum_list = sum_list
            else:
                current_sum_list = self.createAndAdvance(current_sum_list)

            if current_l1 == None:
                l1_val = 0
            else:
                l1_val = current_l1.val

            if current_l2 == None:
                l2_val = 0
            else:
                l2_val = current_l2.val

            s = l1_val + l2_val + carry
            carry = s // 10
            val = s % 10

            current_sum_list.val = val
            current_l1 = self.advanceNode(current_l1)
            current_l2 = self.advanceNode(current_l2)

        if carry > 0:
            current_sum_list = self.createAndAdvance(current_sum_list, carry)
        
        return sum_list
        
