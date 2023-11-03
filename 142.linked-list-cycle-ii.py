<<<<<<< HEAD
#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# By fast-slow pointer, time: O(n), space: O(1)
# �o���D�جO��node.next���V����m�P�_�O�_��cycle, �]�N�O��python��node��곣�O���V�Unode��m��pointer
# ���O�^�Ǿ��linklist���������Ӥ��ݭndummy node?
# �o��linklist�۹J�������D�طPı���n���`�@a+b��node�h�Q, cycle��b��node
# fast�Mslow�۹J�ɦ���S��: �@�Ofast���w��slow�⭿�B��, �G�Ofast��slow"�h��"�Fn��cycle������b(�˰l���h�]n��)
# ����On�Ӥ��O1�O�]�Ҽ{a��b�j�����p, Ex: a = 5, b = 3���ܮڥ��٨S����a, ���i���cycle�J�f
# �`���U�ӴN�Of = 2s�Bf = s+nb, �o�X�bfast slow�۹J��, s = nb
# �C��slow����cycle�J�f����a+nb�B, �ҥH�u�nfast slow�۹J�ɦA��a�B�N�|��cycle�J�fnode
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        while fast!=None and fast.next!=None:
            # �p�Gfast����linklist�����N��Scycle
            # ���o�بҥ~�βפ���󳣭n�g�b�̫e��
            fast = fast.next.next
            slow = slow.next
            # �ĤG�ر��p, fast�Mslow�Ĥ@���۹J, �o�ɧƱ��Xindex
            if fast==slow:
                # �Ψӧ�Xcycle�J�fnode��index
                # �Nfast�qhead�}�l���slow�@�_���@�B, ��o��fast = slow�N���Fa
                # �]�N�O��Fcycle�J�f��node
                fast = head
                while fast!=slow:
                    fast = fast.next
                    slow = slow.next
                return fast
        return None
        
# @lc code=end

=======
#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# By fast-slow pointer, time: O(n), space: O(1)
# �o���D�جO��node.next���V����m�P�_�O�_��cycle, �]�N�O��python��node��곣�O���V�Unode��m��pointer
# ���O�^�Ǿ��linklist���������Ӥ��ݭndummy node?
# �o��linklist�۹J�������D�طPı���n���`�@a+b��node�h�Q, cycle��b��node
# fast�Mslow�۹J�ɦ���S��: �@�Ofast���w��slow�⭿�B��, �G�Ofast��slow"�h��"�Fn��cycle������b(�˰l���h�]n��)
# ����On�Ӥ��O1�O�]�Ҽ{a��b�j�����p, Ex: a = 5, b = 3���ܮڥ��٨S����a, ���i���cycle�J�f
# �`���U�ӴN�Of = 2s�Bf = s+nb, �o�X�bfast slow�۹J��, s = nb
# �C��slow����cycle�J�f����a+nb�B, �ҥH�u�nfast slow�۹J�ɦA��a�B�N�|��cycle�J�fnode
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        while fast!=None and fast.next!=None:
            # �p�Gfast����linklist�����N��Scycle
            # ���o�بҥ~�βפ���󳣭n�g�b�̫e��
            fast = fast.next.next
            slow = slow.next
            # �ĤG�ر��p, fast�Mslow�Ĥ@���۹J, �o�ɧƱ��Xindex
            if fast==slow:
                # �Ψӧ�Xcycle�J�fnode��index
                # �Nfast�qhead�}�l���slow�@�_���@�B, ��o��fast = slow�N���Fa
                # �]�N�O��Fcycle�J�f��node
                fast = head
                while fast!=slow:
                    fast = fast.next
                    slow = slow.next
                return fast
        return None
        
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
