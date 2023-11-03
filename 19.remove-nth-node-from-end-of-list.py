#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# By dummy node and reverse, time: O(n), space: O(1)
# 要刪除倒數第n個node, 直覺就是反轉後數n個刪掉, 再反轉回去
class Solution:
    def reverse(self, head):
        # 反轉linklist要準備prev使node反轉後有地方能指向
        prev = None
        cur = head
        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 收到head之後將linklist反轉, newHead是反轉後的head
        newHead = self.reverse(head)
        # 將dummy指向newHead
        # 這類刪除node的都要準備dummy, 避免要刪除head的情況出錯或需要特殊判斷
        dummy = ListNode(next = newHead)
        i = 0
        cur = dummy
        while cur.next is not None:
            i += 1
            if i==n:
                # 當遇到第n個node將其刪除, 也就是跳過link他
                cur.next = cur.next.next
                # 刪除成功就不需要繼續while了
                break
            # 沒遇到需要刪除的目標就看下個node
            cur = cur.next
        # 刪除完畢後再將linklist翻轉回去, return正確的head
        # 注意要return反轉後的dummy.next, cur或newHead都不行
        # newHead雖然一開始是dummy.next, 但不行
        # 原因是刪除的動作是透過更改link而非node本身, 如果只有一個node那head仍然存在
        # 在[1], n = 1的情況newHead = 1且刪不掉, 只能透過將cur.next(dummy.next) = None來刪除
        return self.reverse(dummy.next)
        
# By double pointer, time: O(n), space: O(1)
# 這個做法好處是只需要走訪linklist一次
# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         # dummy指向head
#         dummy = ListNode(0, head)
#         # first從head開始
#         first = head
#         second = dummy
#         # first從head移動n次, 也就是到達第n+1個node
#         # 同時second正在dummy也就是第0個node, 這樣相差n+1個node
#         # 對first而言second正式倒數n+1個
#         for i in range(n):
#             first = first.next
        
#         # 再first走到None前, first和second都往前
#         while first is not None:
#             first = first.next
#             second = second.next
#         # 當first走到None, 也代表second走到倒數第n+1個node
#         # second的next就是倒數第n個node, 將其跳過
#         second.next = second.next.next
#         # 刪除成功return結果
#         return dummy.next


# @lc code=end

