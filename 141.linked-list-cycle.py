<<<<<<< HEAD
#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# By fast-slow pointer, time: O(n), space: O(1)
# �o�Ӥ�k�Ω�P�_cycle��, fast�@������B, slow�@�����@�B
# �Y��cycle��fast�`���@�ѷ|�˰l��slow, �ҥH��fast==slow�K�N��cycle
# �Y�Scycle, fast�û���slow�֪��쨫�Xlinklist����
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        fast = slow = head
        # ��fast�٨S���X��link list
        # ����uwhile fast�]fast�@������B, �Yfast.next����
        # ��fast.next�L�k���Vfast.next.next 
        while fast and fast.next:
            # fast�@������B, slow�@�����@�B
            fast = fast.next.next
            slow = slow.next
            # �۵��N��cycle
            if fast==slow:
                return True
        return False

# By hashtable, time: O(n), space: O(n)�]n���I�n��n�Ӷi��~��d��
# �C�����X��snode�h�d�O�_�s�������node
# ���s������N��cycle, return True 
# ���X���F���Scycle return false
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         # linklist���e���|���ƥ�set, �|���ƥ�list
#         res = set()
#         curr = head
#         while(curr!=None):
#             if curr.next in res:
#                 return True
#             res.add(curr)
#             curr = curr.next
#         return False

        
# @lc code=end

=======
#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# By fast-slow pointer, time: O(n), space: O(1)
# �o�Ӥ�k�Ω�P�_cycle��, fast�@������B, slow�@�����@�B
# �Y��cycle��fast�`���@�ѷ|�˰l��slow, �ҥH��fast==slow�K�N��cycle
# �Y�Scycle, fast�û���slow�֪��쨫�Xlinklist����
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        fast = slow = head
        # ��fast�٨S���X��link list
        # ����uwhile fast�]fast�@������B, �Yfast.next����
        # ��fast.next�L�k���Vfast.next.next 
        while fast and fast.next:
            # fast�@������B, slow�@�����@�B
            fast = fast.next.next
            slow = slow.next
            # �۵��N��cycle
            if fast == slow:
                return True
        return False

# By hashtable, time: O(n), space: O(n)�]n���I�n��n�Ӷi��~��d��
# �C�����X��snode�h�d�O�_�s�������node
# ���s������N��cycle, return True 
# ���X���F���Scycle return false
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         # linklist���e���|���ƥ�set, �|���ƥ�list
#         res = set()
#         curr = head
#         while(curr!=None):
#             if curr.next in res:
#                 return True
#             res.add(curr)
#             curr = curr.next
#         return False

        
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
