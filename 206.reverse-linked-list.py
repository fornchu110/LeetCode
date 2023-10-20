#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# By iterative, time: O(n), space: O(1)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # prev�ت��O��node���D�����n���V��, �쥻���V��@��node���|���V�e�@��node
        # cur�ت��O���D�ثe�B�z��node�O����
        prev, cur = None, head
        # ��ثe���T��nod3�b�B�z��
        while cur is not None:
            # next�ت��O������@��node�O����
            # �קK����ᥢ�h�U�@�ӭn�B�znode����m
            next = cur.next
            # ��ثe��node�q���V��@��node�אּ���V�e�@��node(����)
            cur.next = prev
            # ��U��node�Ө��N�O�n�אּ���V�ثe��node, �O���U��
            prev = cur
            # �אּ�B�z�U�@��node
            cur = next
        # �̫�prev�N�O����᪺head
        return prev

# By recursive, time: O(n), space: O(n)
# �n�`�N���n�Nnode���۫��V�Φ�cycle
# �o��newHead���M�@���^�Ǧ����èS�Ω�brecursive�����P�_, �u�O���Freturn
# �u���b���৹����return������newHead�~�N��w�������઺linklist
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         if head==None or head.next==None:
#             return head
#         newHead = self.reverseList(head.next)
#         # �N�쥻���U��node���V�ۤv(�e�@��), �]�N�O����
#         head.next.next = head
#         # �`�N�N�ۤv���VNULL, �קKhead�Mhead.next���۫��V�y��cycle
#         head.next = None
#         # newHead�@�����O�쥻linklist�̫�@��node
#         return newHead

# @lc code=end

