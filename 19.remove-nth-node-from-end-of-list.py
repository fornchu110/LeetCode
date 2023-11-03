<<<<<<< HEAD
#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# By dummy node and reverse, time: O(n), space: O(1)
# �n�R���˼Ʋ�n��node, ��ı�N�O������n�ӧR��, �A����^�h
class Solution:
    def reverse(self, head):
        # ����linklist�n�ǳ�prev��node����ᦳ�a�����V
        prev = None
        cur = head
        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # ����head����Nlinklist����, newHead�O����᪺head
        newHead = self.reverse(head)
        # �Ndummy���VnewHead
        # �o���R��node�����n�ǳ�dummy, �קK�n�R��head�����p�X���λݭn�S��P�_
        dummy = ListNode(next = newHead)
        i = 0
        cur = dummy
        while cur.next is not None:
            i += 1
            if i==n:
                # ��J���n��node�N��R��, �]�N�O���Llink�L
                cur.next = cur.next.next
                # �R�����\�N���ݭn�~��while�F
                break
            # �S�J��ݭn�R�����ؼдN�ݤU��node
            cur = cur.next
        # �R��������A�Nlinklist½��^�h, return���T��head
        # �`�N�nreturn����᪺dummy.next, cur��newHead������
        # newHead���M�@�}�l�Odummy.next, ������
        # ��]�O�R�����ʧ@�O�z�L���link�ӫDnode����, �p�G�u���@��node��head���M�s�b
        # �b[1], n = 1�����pnewHead = 1�B�R����, �u��z�L�Ncur.next(dummy.next) = None�ӧR��
        return self.reverse(dummy.next)
        
# By double pointer, time: O(n), space: O(1)
# �o�Ӱ��k�n�B�O�u�ݭn���Xlinklist�@��
# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         # dummy���Vhead
#         dummy = ListNode(0, head)
#         # first�qhead�}�l
#         first = head
#         second = dummy
#         # first�qhead����n��, �]�N�O��F��n+1��node
#         # �P��second���bdummy�]�N�O��0��node, �o�ˬۮtn+1��node
#         # ��first�Ө�second�����˼�n+1��
#         for i in range(n):
#             first = first.next
        
#         # �Afirst����None�e, first�Msecond�����e
#         while first is not None:
#             first = first.next
#             second = second.next
#         # ��first����None, �]�N��second����˼Ʋ�n+1��node
#         # second��next�N�O�˼Ʋ�n��node, �N����L
#         second.next = second.next.next
#         # �R�����\return���G
#         return dummy.next

# @lc code=end

=======
#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# By dummy node and reverse, time: O(n), space: O(1)
# �n�R���˼Ʋ�n��node, ��ı�N�O������n�ӧR��, �A����^�h
class Solution:
    def reverse(self, head):
        # ����linklist�n�ǳ�prev��node����ᦳ�a�����V
        prev = None
        cur = head
        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # ����head����Nlinklist����, newHead�O����᪺head
        newHead = self.reverse(head)
        # �Ndummy���VnewHead
        # �o���R��node�����n�ǳ�dummy, �קK�n�R��head�����p�X���λݭn�S��P�_
        dummy = ListNode(next = newHead)
        i = 0
        cur = dummy
        while cur.next is not None:
            i += 1
            if i==n:
                # ��J���n��node�N��R��, �]�N�O���Llink�L
                cur.next = cur.next.next
                # �R�����\�N���ݭn�~��while�F
                break
            # �S�J��ݭn�R�����ؼдN�ݤU��node
            cur = cur.next
        # �R��������A�Nlinklist½��^�h, return���T��head
        # �`�N�nreturn����᪺dummy.next, cur��newHead������
        # newHead���M�@�}�l�Odummy.next, ������
        # ��]�O�R�����ʧ@�O�z�L���link�ӫDnode����, �p�G�u���@��node��head���M�s�b
        # �b[1], n = 1�����pnewHead = 1�B�R����, �u��z�L�Ncur.next(dummy.next) = None�ӧR��
        return self.reverse(dummy.next)
        
# By double pointer, time: O(n), space: O(1)
# �o�Ӱ��k�n�B�O�u�ݭn���Xlinklist�@��
# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         # dummy���Vhead
#         dummy = ListNode(0, head)
#         # first�qhead�}�l
#         first = head
#         second = dummy
#         # first�qhead����n��, �]�N�O��F��n+1��node
#         # �P��second���bdummy�]�N�O��0��node, �o�ˬۮtn+1��node
#         # ��first�Ө�second�����˼�n+1��
#         for i in range(n):
#             first = first.next
        
#         # �Afirst����None�e, first�Msecond�����e
#         while first is not None:
#             first = first.next
#             second = second.next
#         # ��first����None, �]�N��second����˼Ʋ�n+1��node
#         # second��next�N�O�˼Ʋ�n��node, �N����L
#         second.next = second.next.next
#         # �R�����\return���G
#         return dummy.next

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
