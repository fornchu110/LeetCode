#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# ���@��link list, �N���e�C���node�ǭǥ洫(���uvalue)��return head

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# By iterative, time: O(n), space: O(1)
# ��linklist�����node���洫, �䤣��۾F��node��洫�N�������
# �]�|����linklist�ҥH�����ϥ�dummy
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(next = head)
        cur = dummy
        # �C������ӥi�洫��node�~����
        while cur.next and cur.next.next:
            # ���node���洫, node1�Mnode2
            node1 = cur.next
            node2 = cur.next.next
            # ���I�b�o�y, �@�}�lcur = dummy�o��
            # cur.next = noede2���P��dummy.next = node2, ���̫�dummy.next�S�X���D
            cur.next = node2
            # �Ĥ@��node���W�쥻�ĤG��node��next
            node1.next = node2.next
            # �ĤG��node���W�Ĥ@��node
            node2.next = node1
            # cur�ܦ��ثe����誺node1
            # �o�Dcur���ӬOdummy�o�ب�node�e�@��prev���}��
            cur = node1
        return dummy.next

# By recursive, time: O(n), space: O(n), ���������
# ��recursive���ܨS��dummy����
# recursive�`�N�q���ݲפ����M�q�Y�ݨC�@���ݭn���^�ǭ�
# class Solution:
#     def swapPairs(self, head: ListNode) -> ListNode:
#         # �פ���������node�ɵ���
#         if head is None or head.next is None:
#             # return head�Ӥ��Oreturn None�קK�u���@��node�ɦ^�ǪŰ}�C
#             return head
#         # �o��O�[��洫��ĤG�Ӹ`�I�|�����s���Ĥ@�Ӹ`�I
#         newHead = head.next
#         # �쥻�Ĥ@�Ӹ`�I�n���W�쥻�ĤG�Ӹ`�I��next���j�U�h���^�ǭ�
#         # ���N�O�U�@����return��newHead, �]�N�O�U�@�����쥻�ĤG��node
#         # ���W�ۤv��blinklist��node�`�ƥu��1�ɫO�d���@��node�Ӥ���return None
#         head.next = self.swapPairs(newHead.next)
#         # �s���Ĥ@�Ӹ`�I�n���W�쥻�Ĥ@�Ӹ`�I
#         newHead.next = head
#         return newHead

# @lc code=end

