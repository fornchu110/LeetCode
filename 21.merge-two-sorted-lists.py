#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# By iterative dummy and double pointer, time: O(n+m), space: O(1), n��list1����, m��list2����
# ��Ӥw�Ѥp��j�ƧǹL��linklist, �N��Ѥp��j�X�֦��s��linklist�^��head
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1
        cur2 = list2
        dummy  = res = ListNode()
        if cur1 is None and cur2 is None:
            return None
        # ��̸ѫDNone�ɤ~���j��
        while cur1 is not None and cur2 is not None:
            if cur1.val<cur2.val:
                res.next = cur1
                cur1 = cur1.next
            else:
                res.next = cur2
                cur2 = cur2.next
            res = res.next
        # �䤤���@��None�N����while�j��, �o�ɱ��W�DNone����list�Y�i
        if cur1 is None:
            res.next = cur2
        else:
            res.next = cur1
        return dummy.next

        # �쥻�g�k, ����ꤣ�κި�@��None, �b�@��Snode�ɪ������W�t�@��N�n
        # �ӥB���ݭn�طs��tmp node, ������list1��list2��node���W�Y�i
        # while cur1 is not None or cur2 is not None:
        #     if cur1 is None:
        #         tmp = ListNode(val = cur2.val)
        #         cur2 = cur2.next
        #     elif cur2 is None:
        #         tmp = ListNode(val = cur1.val)
        #         cur1 = cur1.next
        #     else:
        #         if cur1.val<cur2.val:
        #             tmp = ListNode(val = cur1.val)
        #             cur1 = cur1.next
        #         else:
        #             tmp = ListNode(val = cur2.val)
        #             cur2 = cur2.next
        #     res.next = tmp
        #     res = res.next
        # return dummy.next

# By recursive, time: O(n+m), space: O(n+m)
# ��recursive�g
# recursive���O���������, �ҥH�n�Q���q��list���ݶ}�lreturn���u��list
# �Ӥ��_�N�e����next�Q�αq����return�����ulist(�w�ƧǦn�����G)���W, �̫ᱵ�n���linklist
# return��̫�@���~�O�̪�����merge����list
# class Solution:
#     def mergeTwoLists(self, cur1: ListNode, cur2: ListNode) -> ListNode:
#         # �פ����, ��@��None�N�^�ǥt�~�@��list�ѤU��
#         if cur1 is None:
#             return cur2
#         elif cur2 is None:
#             return cur1
#         # ���list�ҫDNone, ���val���p������list return
#         elif cur1.val < cur2.val:
#             # �]���cur1, ��cur1.next�~�򻼰j
#             cur1.next = self.mergeTwoLists(cur1.next, cur2)
#             return cur1
#         else:
#             # ���cur2, ��cur2.next�~�򻼰j
#             cur2.next = self.mergeTwoLists(cur1, cur2.next)
#             return cur2

# @lc code=end

