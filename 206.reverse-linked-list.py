#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# By iterative, time: O(n), space: O(1)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # prev目的是讓node知道反轉後要指向誰, 原本指向後一個node的會指向前一個node
        # cur目的是知道目前處理的node是哪個
        prev, cur = None, head
        # 當目前的確有nod3在處理時
        while cur is not None:
            # next目的是紀錄後一個node是哪個
            # 避免反轉後失去下一個要處理node的位置
            next = cur.next
            # 把目前的node從指向後一個node改為指向前一個node(反賺)
            cur.next = prev
            # 對下個node而言就是要改為指向目前的node, 記錄下來
            prev = cur
            # 改為處理下一個node
            cur = next
        # 最後prev就是反轉後的head
        return prev

# By recursive, time: O(n), space: O(n)
# 要注意不要將node互相指向形成cycle
# 這邊newHead雖然一直回傳但其實並沒用於在recursive內的判斷, 只是為了return
# 只有在反轉完畢時return的那次newHead才代表已結束反轉的linklist
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         if head==None or head.next==None:
#             return head
#         newHead = self.reverseList(head.next)
#         # 將原本的下個node指向自己(前一個), 也就是反轉
#         head.next.next = head
#         # 注意將自己指向NULL, 避免head和head.next互相指向造成cycle
#         head.next = None
#         # newHead一直都是原本linklist最後一個node
#         return newHead

# @lc code=end
