<<<<<<< HEAD
#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# By reverse and fast-slow pointer, time: O(n), space: O(1)
# �n�Nlink list�̧��Y�����s�Ƨ� 
# �쥻�Q����������tail�A�Q��tail.next���e
# ���o�˰�����]�S����, tail.next��ڤW�N�ONone
# �n����Xlist�����I, �N�����H�᪺list����
# �Q��fast-slow pointer���覡��mid
# ��list�쥻��head�M����ᨺ�qlist��head��, �N�L�̥���X�֧Y�i
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if head is None:
            return
        mid = self.middleNode(head)
        l1 = head
        l2 = mid.next
        mid.next = None
        l2 = self.reverseList(l2)
        self.mergeList(l1, l2)
    # �Q��fast slow pointer��mid
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        # �`�N����u�P�_fast.next.next�O�]�Yfast.next��None, �L�k�P�_fast.next.next����
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        # fast����Bslow���@�B, fast���ਫ��slow��n�bmid
        return slow
    # �����b����link list
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        while cur is not None:
            nextTemp = cur.next
            cur.next = prev
            prev = cur
            cur = nextTemp
        return prev

    def mergeList(self, l1: ListNode, l2: ListNode):
        while l1 and l2:
            cur1 = l1.next
            cur2 = l2.next
            l1.next = l2
            l1 = cur1
            l2.next = l1
            l2 = cur2
        

# @lc code=end

=======
#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# By reverse and fast-slow pointer, time: O(n), space: O(1)
# �n�Nlink list�̧��Y�����s�Ƨ� 
# �쥻�Q����������tail�A�Q��tail.next���e
# ���o�˰�����]�S����, tail.next��ڤW�N�ONone
# �n����Xlist�����I, �N�����H�᪺list����
# �Q��fast-slow pointer���覡��mid
# ��list�쥻��head�M����ᨺ�qlist��head��, �N�L�̥���X�֧Y�i
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if head is None:
            return
        mid = self.middleNode(head)
        l1 = head
        l2 = mid.next
        mid.next = None
        l2 = self.reverseList(l2)
        self.mergeList(l1, l2)
    # �Q��fast slow pointer��mid
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        # �`�N����u�P�_fast.next.next�O�]�Yfast.next��None, �L�k�P�_fast.next.next����
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        # fast����Bslow���@�B, fast���ਫ��slow��n�bmid
        return slow
    # �����b����link list
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        while cur is not None:
            nextTemp = cur.next
            cur.next = prev
            prev = cur
            cur = nextTemp
        return prev

    def mergeList(self, l1: ListNode, l2: ListNode):
        while l1 and l2:
            cur1 = l1.next
            cur2 = l2.next
            l1.next = l2
            l1 = cur1
            l2.next = l1
            l2 = cur2
        

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
