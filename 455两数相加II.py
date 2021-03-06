# Leetcode-Python-Soultion
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a, b = [], []
        while l1:
            a.append(l1.val)
            l1 = l1.next
        while l2:
            b.append(l2.val)
            l2 = l2.next
        p = None
        ans = 0
        while a or b or ans != 0:
            v1 = 0 if not a else a.pop()
            v2 = 0 if not b else b.pop()
            v = v1 + v2 + ans
            ans = v // 10
            v %= 10
            curnode = ListNode(v)
            curnode.next = p
            p = curnode
        return p
