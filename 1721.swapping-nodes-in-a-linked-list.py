<<<<<<< HEAD
#
# @lc app=leetcode id=1721 lang=python3
#
# [1721] Swapping Nodes in a Linked List
#

# ���@��link list�Mk, �Nlink list����k�Ӥ������Ʋ�k�Ӥ������e�洫


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# By math and while, time: O(n), space: O(1)
# ���O���n�Ĥ@��node�M��k��node, �Q�άۮtk-1���ʽ�
# �N���pointer�P�ɥk������쥻���V��k�ӫ��Ъ�pointer���V�̫�@��
# ���ɭ쥻���V�Ĥ@��node��pointer�K�۵M���V�˼Ʋ�k��node, �A�N���val�洫�Y�i
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # ��left�Mright��ӫ��Ъ�l�ƫ��Vhead
        left = right = head
        # �Nright���ʨ�link list����k��node�Ҧb��m, ���pk=5�n���ʨ즹�ݭn����4��
        for i in range(k-1):
            right = right.next
        # �N��k��node����m�O���_��
        forward = right
        # right�Mleft�P�ɥk�������, �o�˳̫�right����ݮ�, left�Ҧb�N�O�˼Ʋ�k��node
        # �]��̳��ۮtk-1���Z��
        while right.next:
            left = left.next
            right = right.next
        # �˼Ʋ�k��node����m�O���_��
        reverse = left
        # �洫��̪�value
        forward.val,reverse.val = reverse.val,forward.val
        return head

# @lc code=end

=======
#
# @lc app=leetcode id=1721 lang=python3
#
# [1721] Swapping Nodes in a Linked List
#

# ���@��link list�Mk, �Nlink list����k�Ӥ������Ʋ�k�Ӥ������e�洫


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# By math and while, time: O(n), space: O(1)
# ���O���n�Ĥ@��node�M��k��node, �Q�άۮtk-1���ʽ�
# �N���pointer�P�ɥk������쥻���V��k�ӫ��Ъ�pointer���V�̫�@��
# ���ɭ쥻���V�Ĥ@��node��pointer�K�۵M���V�˼Ʋ�k��node, �A�N���val�洫�Y�i
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # ��left�Mright��ӫ��Ъ�l�ƫ��Vhead
        left = right = head
        # �Nright���ʨ�link list����k��node�Ҧb��m, ���pk=5�n���ʨ즹�ݭn����4��
        for i in range(k-1):
            right = right.next
        # �N��k��node����m�O���_��
        forward = right
        # right�Mleft�P�ɥk�������, �o�˳̫�right����ݮ�, left�Ҧb�N�O�˼Ʋ�k��node
        # �]��̳��ۮtk-1���Z��
        while right.next:
            left = left.next
            right = right.next
        # �˼Ʋ�k��node����m�O���_��
        reverse = left
        # �洫��̪�value
        forward.val,reverse.val = reverse.val,forward.val
        return head

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
