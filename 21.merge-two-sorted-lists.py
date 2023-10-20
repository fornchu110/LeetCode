#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# By iterative dummy and double pointer, time: O(n+m), space: O(1), n為list1長度, m為list2長度
# 兩個已由小到大排序過的linklist, 將其由小到大合併成新的linklist回傳head
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1
        cur2 = list2
        dummy  = res = ListNode()
        if cur1 is None and cur2 is None:
            return None
        # 兩者解非None時才做迴圈
        while cur1 is not None and cur2 is not None:
            if cur1.val<cur2.val:
                res.next = cur1
                cur1 = cur1.next
            else:
                res.next = cur2
                cur2 = cur2.next
            res = res.next
        # 其中之一為None就結束while迴圈, 這時接上非None那個list即可
        if cur1 is None:
            res.next = cur2
        else:
            res.next = cur1
        return dummy.next

        # 原本寫法, 但其實不用管其一為None, 在一邊沒node時直接接上另一邊就好
        # 而且不需要建新的tmp node, 直接往list1或list2的node接上即可
        # while cur1 is not None or cur2 is not None:
        #     if cur1 is None:
        #         tmp = ListNode(val = cur2.val)
        #         cur2 = cur2.next
        #     elif cur2 is None:
        #         tmp = ListNode(val = cur1.val)
        #         cur1 = cur1.next
        #     else:
        #         if cur1.val<cur2.val:
        #             tmp = ListNode(val = cur1.val)
        #             cur1 = cur1.next
        #         else:
        #             tmp = ListNode(val = cur2.val)
        #             cur2 = cur2.next
        #     res.next = tmp
        #     res = res.next
        # return dummy.next

# By recursive, time: O(n+m), space: O(n+m)
# 用recursive寫
# recursive都是先走到尾端, 所以要想像從兩list尾端開始return較短的list
# 而不斷將前面的next利用從尾端return的較短list(已排序好的結果)接上, 最後接好整個linklist
# return到最後一次才是最長完整merge完的list
# class Solution:
#     def mergeTwoLists(self, cur1: ListNode, cur2: ListNode) -> ListNode:
#         # 終止條件, 其一為None就回傳另外一個list剩下的
#         if cur1 is None:
#             return cur2
#         elif cur2 is None:
#             return cur1
#         # 當兩list皆非None, 選擇val較小的那個list return
#         elif cur1.val < cur2.val:
#             # 因選擇cur1, 往cur1.next繼續遞迴
#             cur1.next = self.mergeTwoLists(cur1.next, cur2)
#             return cur1
#         else:
#             # 選擇cur2, 往cur2.next繼續遞迴
#             cur2.next = self.mergeTwoLists(cur1, cur2.next)
#             return cur2

# @lc code=end

