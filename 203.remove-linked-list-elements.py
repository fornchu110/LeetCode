<<<<<<< HEAD
#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# By iterative, time: O(n), space: O(1)
# �z�Ldummy node���Vhead���覡������head�����B�~�P�_, �]����head��
# leetcode�^��head��L�|�۰ʨ��X���linklist�o��ѤUnode
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # �����`�I���Vhead, �קKhead��, �]��K�R��head�ɤ����B�~���P�_
        dummyNode = ListNode(next=head) 
        cur = dummyNode
        # �o�˦bwhile���P�_�Fhead�O�_����, �Yhead���Ū����^�Ǫ�head
        while(cur.next!=None):
            if(cur.next.val == val):
                cur.next = cur.next.next #���L�쥻val==�ؼЪ�cur.next 
            else:
                cur = cur.next
        # ��ڤW�N�Olinklist��head
        return dummyNode.next

# By recursive, time: O(n), space: O(n)
# class Solution:
#     def removeElements(self, head: ListNode, val: int) -> ListNode:
#         if(head==None):
#             return head
#         head.next = self.removeElements(head.next, val)
#         if head.val==val:
#             return head.next
#         else:
#             return head

# @lc code=end

=======
#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# By iterative, time: O(n), space: O(1)
# �z�Ldummy node���Vhead���覡������head�����B�~�P�_, �]����head��
# leetcode�^��head��L�|�۰ʨ��X���linklist�o��ѤUnode
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # �����`�I���Vhead, �קKhead��, �]��K�R��head�ɤ����B�~���P�_
        dummyNode = ListNode(next=head) 
        cur = dummyNode
        # �o�˦bwhile���P�_�Fhead�O�_����, �Yhead���Ū����^�Ǫ�head
        while(cur.next!=None):
            if(cur.next.val == val):
                cur.next = cur.next.next #���L�쥻val==�ؼЪ�cur.next 
            else:
                cur = cur.next
        # ��ڤW�N�Olinklist��head
        return dummyNode.next

# By recursive, time: O(n), space: O(n)
# class Solution:
#     def removeElements(self, head: ListNode, val: int) -> ListNode:
#         if(head==None):
#             return head
#         head.next = self.removeElements(head.next, val)
#         if head.val==val:
#             return head.next
#         else:
#             return head

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
