#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# By double pointer, time: O(n), space: O(n)
# ���Xlinklist�N�`�I���O���U�ӫ�, �ݬ����O�_�j��
# �j��n�O�o�ΦP���Y�����e�ݳ̾A�X
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode(next = head)
        cur = dummy
        palin = list()
        while cur.next is not None :
            palin.append(cur.next.val)
            cur.next = cur.next.next
        # boolin�bpython����return ==
        # �P�_���X�����G�O�_�j��, [::-1]�N��ѥk�����@�Ӥ@�Ӭ�
        return palin==palin[::-1]

# By recursive, time: O(n), space: O(n)
# recursive�]���O��stack���O�Ŷ������Y�q�`������
# class Solution:
#     def isPalindrome(self, head: ListNode) -> bool:

#         self.front_pointer = head

#         def recursively_check(current_node=head):
#             if current_node is not None:
#                 if not recursively_check(current_node.next):
#                     return False
#                 if self.front_pointer.val != current_node.val:
#                     return False
#                 self.front_pointer = self.front_pointer.next
#             return True

#         return recursively_check()

# @lc code=end

