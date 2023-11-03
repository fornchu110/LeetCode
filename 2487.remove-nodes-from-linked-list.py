#
# @lc app=leetcode id=2487 lang=python3
#
# [2487] Remove Nodes From Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# By iterative, time: O(n), space: O(1)
# �n�D��cur�k��s�bnode.val>cur.val��, �Ncur�R��
# �n������linklist, �����q�Y�}�l��
# �o���ܦ��u�n��cur.val>node.val�N�Nnode�R��, �ӫDcur
class Solution:
    # ������linklist, �s�nnext��m��, �N�ثecur���Vprev, ��sprev��cur�é�next node�~��
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev
    # �}�l���R��, �@���qcur��next��
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head = self.reverseList(head)
        while cur.next:
            # cur.val>node.val�ɱN��R��
            # �`�N�R��node�ᤣ��cur = cur.next, �_�h�|���Lcur.next�Q�R�������|
            if cur.val>cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        # �`�N�{�bhead�O����L��, ���nnode�ӭ쥻����, �ҥH�٭n�A����^�h
        return self.reverseList(head)

# By recursive, time: O(n), space: O(n)
# �R����C��node���j�󵥩�ۤv�k�䪺node
# class Solution:
#     def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         # �פ����
#         if head.next is None:
#             return head
#         # �Q�ζǤJhead.next�����X, ��F�̧��ݤ~�}�l�������return
#         # �C��return�����G�@�w�Ocur�k��̤j��
#         # com�Ocompare(���), �N���Ocur�k��val�̤j����node
#         com = self.removeNodes(head.next)  
#         # �ھڤU���P�_�M�wreturn���G
#         # ��com(�^�ǨӪ�)��head(cur)�j, �^��com
#         if com.val > head.val:
#             return com  
#         # ��node�S��head�j, ���R��head
#         # �Nhead(cur)�s�Wnode, ���L����cur�k��com���䨺�Ǥ�com.val�p��node
#         # �P�ɥN��F��com.val�p������node�Q�R���F
#         head.next = com 
#         return head

# @lc code=end

