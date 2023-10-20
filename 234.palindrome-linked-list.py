#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# By double pointer, time: O(n), space: O(n)
# 走訪linklist將節點都記錄下來後, 看紀錄是否迴文
# 迴文要記得用同時頭尾往前看最適合
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode(next = head)
        cur = dummy
        palin = list()
        while cur.next is not None :
            palin.append(cur.next.val)
            cur.next = cur.next.next
        # boolin在python善用return ==
        # 判斷走訪的結果是否迴文, [::-1]代表由右往左一個一個看
        return palin==palin[::-1]

# By recursive, time: O(n), space: O(n)
# recursive因為是用stack浪費空間的關係通常不推薦
# class Solution:
#     def isPalindrome(self, head: ListNode) -> bool:

#         self.front_pointer = head

#         def recursively_check(current_node=head):
#             if current_node is not None:
#                 if not recursively_check(current_node.next):
#                     return False
#                 if self.front_pointer.val != current_node.val:
#                     return False
#                 self.front_pointer = self.front_pointer.next
#             return True

#         return recursively_check()

# @lc code=end

