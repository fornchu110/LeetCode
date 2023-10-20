#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# By merge two head, time: O(n), space: O(1)
# �Nlinklist��odd��������_��, even��������_��, �̫�bodd�����ݱ��Weven head
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # ��linklist����
        if not head:
            return head
        # �S�վ�head�ή�head���P�_�N���ݭndummy
        # odd���ɬ�odd��head
        odd = head
        # evenHead�@��even��head
        evenHead = odd.next
        even = evenHead
        # odd�L�צp�󳣥����n, even�s�b�~�n�~��
        # even.next�s�beven�~���~��, �_�h�������VNULL
        # ������odd���Vodd linklist�̧�node
        # �`�N�n��even�A�P�_even.next, �]even�Y�ONULL���Onode, �N�ڥ��Leven(NULL).next�i�H�P�_�|���~
        while even and even.next:
            # ��Wodd������
            odd.next = even.next
            odd = odd.next
            # ��Weven������
            even.next = odd.next
            even = even.next
        # ����cur�Oodd��������, ���Weven head
        odd.next = evenHead
        return head

# @lc code=end

