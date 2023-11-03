#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# By simulation, time: O(max(m, n)), space: O(1), m、n是兩linklist的長度
# 因input的兩linklist已經是逆序(reverse order), 所以不用特別reverse
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        # cur和dummy從同樣一個node開始
        cur = dummy = ListNode()
        # 如果cur改變目前這個node的內容, dummy指向的目前這個node內容也會改變
        # 從而讓dummy.next產生
        # 但當cur指向別的node後, dummy指向的node都沒變
        while l1 is not None or l2 is not None or carry!=0:
            if l1 is not None:
                l1val = l1.val
            else:
                l1val = 0
            if l2 is not None:
                l2val = l2.val
            else:
                l2val =  0
            tmp = l1val+l2val+carry
            carry = tmp//10
            tmp %= 10
            cur.next = ListNode(tmp) 
            cur = cur.next 
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        return dummy.next


# @lc code=end

