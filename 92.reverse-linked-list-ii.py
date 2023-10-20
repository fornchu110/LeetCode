#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# By head insert, time: O(n), space: O(1)
# head insert法是指先插入最尾端的node, 再於頭端一個個插入尾端前的node, 常用在反轉
# Ex: NULL->3, NULL->2->3, NULL->1->2->3
# 一般建立link list是tail insert, 也就是從頭開始一直於尾端插入接下來的node
# 題目要求的是將left和right之間的node全部翻轉, left和right之間可能不只一個node
# 一次走訪使用head insert想法有點像queue實作stack
# 到需left開始做head insert(left實際上會是反轉後的尾端), 直到整段反轉結束
# 這類題目都要準備dummy node
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode(next = head)
        pre = dummy
        # 做range(left-1)會從dummy走到left前一個點
        for i in range(left-1):
            pre = pre.next
        # cur從left開始做反轉
        # 注意pre = 1, cur = left = 2在反轉過程都不會變
        # 只是cur的相對位置會一直一直往後, 因前面不斷有node插入
        cur = pre.next
        # right-left代表要反轉node的次數
        # 以題目1->2->3->4->5, 反轉2~4為例, 
        for i in range(right-left):
            # 紀錄3, 紀錄next
            next = cur.next
            # 2要指向4
            # 也就是跳過當下最尾的node, 因其要被插入到頭端
            cur.next = next.next
            # 準備好將next(當下最尾node)指向原本最頭的node
            # 3要指向2
            next.next = pre.next
            # 1要指向3
            # 將next插到pre的後面, 也就是將當下最尾的node插到頭端
            pre.next = next
            # 做完第一輪變1->3->2->4, 
            # 做完第二輪變1->4->3->2
        # 也就是原本的head
        return dummy.next

# @lc code=end

