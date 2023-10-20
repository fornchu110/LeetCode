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
# ���ݦ��h�֭�node, �A�qhead��n//2�B��mid 
# Ex: 5��node, head+2�B��node3, 6��node: head+3�B��4 
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
# �o�D�S���n�γo��, �h��@��pointer���Ŷ� 
# ���i�H�ǷQ�k�ӥBcode���²�� 
# slow��1�Bfast��2�B, ��fast�����Ψ���NULL��slow���w�~�줤��
# Ex: 5��node, 1 1, 2 3, 3 5, 6��node: 1 1, 2 3, 3 5, 4 7
# class Solution:
#     def middleNode(self, head: ListNode) -> ListNode:
#         slow = fast = head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#         return slow

# @lc code=end

