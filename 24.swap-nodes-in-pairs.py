#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# 給一個link list, 將內容每兩個node倆倆交換(不只value)並return head

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# By iterative, time: O(n), space: O(1)
# 對linklist內兩兩node做交換, 找不到相鄰的node能交換就維持原樣
# 也會有空linklist所以必須使用dummy
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(next = head)
        cur = dummy
        # 每次有兩個可交換的node才成立
        while cur.next and cur.next.next:
            # 對兩node做交換, node1和node2
            node1 = cur.next
            node2 = cur.next.next
            # 重點在這句, 一開始cur = dummy這輪
            # cur.next = noede2等同把dummy.next = node2, 讓最後dummy.next沒出問題
            cur.next = node2
            # 第一個node接上原本第二個node的next
            node1.next = node2.next
            # 第二個node接上第一個node
            node2.next = node1
            # cur變成目前位於後方的node1
            # 這題cur本來是dummy這種兩node前一個prev的腳色
            cur = node1
        return dummy.next

# By recursive, time: O(n), space: O(n), 貌似比較快
# 用recursive的話沒有dummy概念
# recursive注意從尾看終止條件和從頭看每一輪需要的回傳值
# class Solution:
#     def swapPairs(self, head: ListNode) -> ListNode:
#         # 終止條件當不到兩個node時結束
#         if head is None or head.next is None:
#             # return head而不是return None避免只有一個node時回傳空陣列
#             return head
#         # 這邊是觀察交換後第二個節點會做為新的第一個節點
#         newHead = head.next
#         # 原本第一個節點要接上原本第二個節點的next遞迴下去的回傳值
#         # 其實就是下一輪所return的newHead, 也就是下一輪之原本第二個node
#         # 接上自己能在linklist的node總數只有1時保留那一個node而不像return None
#         head.next = self.swapPairs(newHead.next)
#         # 新的第一個節點要接上原本第一個節點
#         newHead.next = head
#         return newHead

# @lc code=end

