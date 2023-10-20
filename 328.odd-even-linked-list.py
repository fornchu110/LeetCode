#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# By merge two head, time: O(n), space: O(1)
# 將linklist中odd的部分串起來, even的部分串起來, 最後在odd的尾端接上even head
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # 當linklist為空
        if not head:
            return head
        # 沒調整head或拿head做判斷就不需要dummy
        # odd此時為odd的head
        odd = head
        # evenHead作為even的head
        evenHead = odd.next
        even = evenHead
        # odd無論如何都先接好, even存在才要繼續接
        # even.next存在even才能繼續接, 否則直接指向NULL
        # 結束時odd指向odd linklist最尾node
        # 注意要先even再判斷even.next, 因even若是NULL不是node, 就根本無even(NULL).next可以判斷會錯誤
        while even and even.next:
            # 串上odd的部分
            odd.next = even.next
            odd = odd.next
            # 串上even的部分
            even.next = odd.next
            even = even.next
        # 此時cur是odd部分尾端, 接上even head
        odd.next = evenHead
        return head

# @lc code=end

