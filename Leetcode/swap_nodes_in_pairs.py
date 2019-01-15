# https://leetcode.com/problems/swap-nodes-in-pairs/
#
# Given a linked list, swap every two adjacent nodes and return its head.
#
# Example:
#
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#
# Note:
# Your algorithm should use only constant extra space.
# You may not modify the values in the list's nodes, only nodes itself may be changed.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is not None and head.next is not None:
            first = head
            second = head.next
            third = head.next.next
            second.next = first

            if third is not None:
                first.next = self.swapPairs(third)
            else:
                first.next = None

            return second

        else:
            return head


def print_list(head):
    curr = head
    while curr is not None:
        print(curr.val)
        curr = curr.next

nodes1 = ListNode(1)
nodes2 = ListNode(2)
nodes3 = ListNode(3)
nodes4 = ListNode(4)

nodes1.next = nodes2
nodes2.next = nodes3
nodes3.next = nodes4

result = Solution().swapPairs(nodes1)
print_list(result)

