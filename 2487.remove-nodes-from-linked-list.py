#
# @lc app=leetcode id=2487 lang=python3
#
# [2487] Remove Nodes From Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# By iterative, time: O(n), space: O(1)
# 要求當cur右方存在node.val>cur.val時, 將cur刪除
# 要先反轉linklist, 反轉後從頭開始看
# 這樣變成只要比cur.val>node.val就將node刪除, 而非cur
class Solution:
    # 先反轉linklist, 存好next位置後, 將目前cur指向prev, 更新prev為cur並往next node繼續
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev
    # 開始做刪除, 一直從cur往next看
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head = self.reverseList(head)
        while cur.next:
            # cur.val>node.val時將其刪除
            # 注意刪除node後不能cur = cur.next, 否則會跳過cur.next被刪除的機會
            if cur.val>cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        # 注意現在head是反轉過的, 但要node照原本順序, 所以還要再反轉回去
        return self.reverseList(head)

# By recursive, time: O(n), space: O(n)
# 刪除後每個node都大於等於自己右邊的node
# class Solution:
#     def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         # 終止條件
#         if head.next is None:
#             return head
#         # 利用傳入head.next做走訪, 到了最尾端才開始做比較並return
#         # 每次return的結果一定是cur右邊最大的
#         # com是compare(比較), 代表的是cur右邊val最大的的node
#         com = self.removeNodes(head.next)  
#         # 根據下面判斷決定return結果
#         # 當com(回傳來的)比head(cur)大, 回到com
#         if com.val > head.val:
#             return com  
#         # 當node沒比head大, 不刪除head
#         # 將head(cur)連上node, 略過介於cur右邊com左邊那些比com.val小的node
#         # 同時代表了比com.val小的那些node被刪除了
#         head.next = com 
#         return head

# @lc code=end

