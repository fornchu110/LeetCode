#
# @lc app=leetcode id=1669 lang=python3
#
# [1669] Merge In Between Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# By simulation, time: O(n+m), space: O(1), 其中n是list1長度, m是list2長度
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        idx1 = list1
        for i in range(a-1):
            idx1 = idx1.next
        idx2 = idx1
        for i in range(b-a+2):
            idx2 = idx2.next
        idx1.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = idx2
        return list1
# @lc code=end

