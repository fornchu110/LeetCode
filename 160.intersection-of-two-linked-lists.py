#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # A有a個點, B有b個點, 假設共通節點有c個
        A, B = headA, headB
        # 核心想法是:
        # a比較長會走a+(b-c)到共通, b比較長會走b+(a-c)到共通
        # 走到共通時返回node值 
        while A!=B:
            if(A):
                A = A.next
            else:
                A = headB
            if(B):
                B = B.next
            else:
                B = headA
        return A

            

# @lc code=end

