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
# 透過dummy node指向head的方式讓移除head不用額外判斷, 也不怕head遺失
# leetcode回傳head後他會自動走訪整個linklist得到剩下node
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # 虛擬節點指向head, 避免head遺失, 也方便刪除head時不用額外做判斷
        dummyNode = ListNode(next=head) 
        cur = dummyNode
        # 這樣在while先判斷了head是否為空, 若head為空直接回傳空head
        while(cur.next!=None):
            if(cur.next.val == val):
                cur.next = cur.next.next #跳過原本val==目標的cur.next 
            else:
                cur = cur.next
        # 實際上就是linklist之head
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
# 透過dummy node指向head的方式讓移除head不用額外判斷, 也不怕head遺失
# leetcode回傳head後他會自動走訪整個linklist得到剩下node
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # 虛擬節點指向head, 避免head遺失, 也方便刪除head時不用額外做判斷
        dummyNode = ListNode(next=head) 
        cur = dummyNode
        # 這樣在while先判斷了head是否為空, 若head為空直接回傳空head
        while(cur.next!=None):
            if(cur.next.val == val):
                cur.next = cur.next.next #跳過原本val==目標的cur.next 
            else:
                cur = cur.next
        # 實際上就是linklist之head
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
