#
# @lc app=leetcode id=382 lang=python3
#
# [382] Linked List Random Node
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# By choice, time: O(n), space: O(n)
# choice�i�H�q�}�C�������v���H����ܤ@�Ӥ���
class Solution:
    # init�|����@��linklist�Y��node��head
    # init�O�ϥΧ@����class��object���|���w����
    # �ҥH�~��������굹�wlinklist�M��head��, �I�sSolution�K�|����U�����e
    def __init__(self, head: Optional[ListNode]):
        self.head = head
        # �ϥΤ@��self.arr�s��linklist���Ҧ�node
        self.arr = list()
        # ��linklist�i�樫�X, �ç�node���arr��
        while head:
            self.arr.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        # ��~���@��Solution�o�@class��object�I�s.getRandom��
        # �K�|�ϥ�choice�q��Ҧ�node���H���D��@��node return
        return choice(self.arr)

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
# @lc code=end

