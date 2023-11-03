#
# @lc app=leetcode id=445 lang=python3
#
# [445] Add Two Numbers II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# By reverse linklist, time: O(max(m,n)), space: O(1), m�Bn�N���linklist������
# �q�`space���Ŷ������������O�o�쵲�G�L�{����O���B�~�Ŷ�
# ���Mres�ܪ����������S�Ы��B�~�Ŷ��ҥHO(1), �������stack���N�Ospace: O(m+n)
# �N���linklist�U�@���@�ӼƬݫ�, ���ƦV�k����ۥ[�᪺���G�@�˥�linklist��{�X��
# �쥻�Q���ȧ�s�b������linklist���N�n, ���n�Ҽ{�γ\�|����ӤG��Ƭۥ[=�T��Ƴo�ت��p
# �ҥH�٬O�n�ؤ@�ӷs��linklist�M����������n
class Solution:
    def reverse(self, head):
        cur = head
        prev = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        newHead = prev
        return newHead

    # �|�q�C��Ʃ�����ư���linklist���[�k���쵲��
    # �]�����Oin-place�ҥH���ݪ��Dl1�Bl2������, �����res�Y�i
    def plus(self, l1, l2):
        curL1 = l1
        curL2 = l2
        # res�̫�|�����[�����G��linklist��head
        # �@�}�l��None���Ы�node�ɦ��a��i�H���V
        res = None
        # carry�N��n�i�쪺�ƭ�
        carry = 0
        # �u�n���ӭ�linklist�٨S��None�N�n�~��
        # �`�N���٦��ݭn�i�쪺�Ʈɤ]�n�~��
        while curL1 is not None or curL2 is not None or carry!=0:
            # �]None�S��.val�L�k�ۥ[, �ҥH��None�ɵ�0
            if curL1 is None:
                curL1Val = 0
            else:
                curL1Val = curL1.val
            if curL2 is None:
                curL2Val = 0
            else:
                curL2Val = curL2.val
            # �N�Ӧ�ƪ��`�M�[�_��
            tmp = curL1Val+curL2Val+carry
            # �n�i�쪺�ƭ�
            carry = tmp//10
            # ��ڤW�b�o��ƪ��ƭ�
            tmp %= 10
            # �Ыؤ@��resNode�Ψө�mtmp, �]�N�OresNode.val = tmp
            resNode = ListNode(tmp)
            # �Ыا��o��ƫ�, ���V�e���@�Ӧ��
            resNode.next = res
            # �ثe�o�Ӧ���ܦ��U�@�ӧ󰪦�Ʃҫ��V���ؼ�
            res = resNode
            # �]None�S��.next, �ҥH�P�_��DNone��node�~�n�~��
            if curL1 is not None:
                curL1 = curL1.next
            if curL2 is not None:
                curL2 = curL2.next
        # ���G�|�O�@�ӥѰ���Ʃ��C��ƫ��V��linklist, ��n���P�D�حn�D
        return res

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # ���F�q�C��ƶ}�l������a�k, �ҥH���Nlinklist����ñq�C��->����
        newL1 = self.reverse(l1)
        newL2 = self.reverse(l2)
        # �]res��n�O����->�C��, ���ΦA����
        return self.plus(newL2, newL1)

# By stack, time: O(max(m, n)), space: O(m+n)
# �n�B�O�򥻤W���|�ʨ�쥻��linklist���c, ����O�B�~�Ŷ�
# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         s1, s2 = [], []
#         while l1:
#             s1.append(l1.val)
#             l1 = l1.next
#         while l2:
#             s2.append(l2.val)
#             l2 = l2.next
#         ans = None
#         carry = 0
#         while s1 or s2 or carry != 0:
#             a = 0 if not s1 else s1.pop()
#             b = 0 if not s2 else s2.pop()
#             cur = a + b + carry
#             carry = cur // 10
#             cur %= 10
#             curnode = ListNode(cur)
#             curnode.next = ans
#             ans = curnode
#         return ans

# @lc code=end