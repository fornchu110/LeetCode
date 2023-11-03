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
        # A��a���I, B��b���I, ���]�@�q�`�I��c��
        A, B = headA, headB
        # �֤߷Q�k�O:
        # a������|��a+(b-c)��@�q, b������|��b+(a-c)��@�q
        # ����@�q�ɪ�^node�� 
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

