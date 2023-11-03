<<<<<<< HEAD
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

# By simulation, time: O(max(m, n)), space: O(1), m�Bn�O��linklist������
# �]input����linklist�w�g�O�f��(reverse order), �ҥH���ίS�Oreverse
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        # cur�Mdummy�q�P�ˤ@��node�}�l
        cur = dummy = ListNode()
        # �p�Gcur���ܥثe�o��node�����e, dummy���V���ثe�o��node���e�]�|����
        # �q����dummy.next����
        # ����cur���V�O��node��, dummy���V��node���S��
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

=======
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

# By simulation, time: O(max(m, n)), space: O(1), m�Bn�O��linklist������
# �]input����linklist�w�g�O�f��(reverse order), �ҥH���ίS�Oreverse
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        # cur�Mdummy�q�P�ˤ@��node�}�l
        cur = dummy = ListNode()
        # �p�Gcur���ܥثe�o��node�����e, dummy���V���ثe�o��node���e�]�|����
        # �q����dummy.next����
        # ����cur���V�O��node��, dummy���V��node���S��
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

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
