#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# By head insert, time: O(n), space: O(1)
# head insert�k�O�������J�̧��ݪ�node, �A���Y�ݤ@�ӭӴ��J���ݫe��node, �`�Φb����
# Ex: NULL->3, NULL->2->3, NULL->1->2->3
# �@��إ�link list�Otail insert, �]�N�O�q�Y�}�l�@������ݴ��J���U�Ӫ�node
# �D�حn�D���O�Nleft�Mright������node����½��, left�Mright�����i�ण�u�@��node
# �@�����X�ϥ�head insert�Q�k���I��queue��@stack
# ���left�}�l��head insert(left��ڤW�|�O����᪺����), �����q���൲��
# �o���D�س��n�ǳ�dummy node
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode(next = head)
        pre = dummy
        # ��range(left-1)�|�qdummy����left�e�@���I
        for i in range(left-1):
            pre = pre.next
        # cur�qleft�}�l������
        # �`�Npre = 1, cur = left = 2�b����L�{�����|��
        # �u�Ocur���۹��m�|�@���@������, �]�e�����_��node���J
        cur = pre.next
        # right-left�N��n����node������
        # �H�D��1->2->3->4->5, ����2~4����, 
        for i in range(right-left):
            # ����3, ����next
            next = cur.next
            # 2�n���V4
            # �]�N�O���L��U�̧���node, �]��n�Q���J���Y��
            cur.next = next.next
            # �ǳƦn�Nnext(��U�̧�node)���V�쥻���Y��node
            # 3�n���V2
            next.next = pre.next
            # 1�n���V3
            # �Nnext����pre���᭱, �]�N�O�N��U�̧���node�����Y��
            pre.next = next
            # �����Ĥ@����1->3->2->4, 
            # �����ĤG����1->4->3->2
        # �]�N�O�쥻��head
        return dummy.next

# @lc code=end

