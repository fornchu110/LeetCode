#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# By one pointer, time: O(n), space: O(1)
# 先看有多少個node, 再從head走n//2步到mid 
# Ex: 5個node, head+2步到node3, 6個node: head+3步到4 
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        cur = dummy
        n = 0
        while(cur.next!=None):
            n += 1
            cur = cur.next
        n = n//2
        cur = dummy.next
        while(n!=0):
            cur = cur.next
            n -= 1
        return cur

# By fast-slow pointer, time: O(n), space: O(1) 
# 這題沒必要用這招, 多花一個pointer的空間 
# 但可以學想法而且code比較簡潔 
# slow走1步fast走2步, 當fast走完或走到NULL時slow必定才到中間
# Ex: 5個node, 1 1, 2 3, 3 5, 6個node: 1 1, 2 3, 3 5, 4 7
# class Solution:
#     def middleNode(self, head: ListNode) -> ListNode:
#         slow = fast = head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#         return slow

# @lc code=end

