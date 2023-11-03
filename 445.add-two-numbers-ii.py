#
# @lc app=leetcode id=445 lang=python3
#
# [445] Add Two Numbers II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# By reverse linklist, time: O(max(m,n)), space: O(1), m、n代表兩linklist之長度
# 通常space的空間複雜度講的是得到結果過程中花費的額外空間
# 雖然res很長但中間都沒創建額外空間所以O(1), 不反轉用stack做就是space: O(m+n)
# 將兩個linklist各作為一個數看待, 把兩數向右對齊相加後的結果一樣用linklist表現出來
# 原本想說值更新在較長的linklist中就好, 但要考慮或許會有兩個二位數相加=三位數這種狀況
# 所以還是要建一個新的linklist專門接收比較好
class Solution:
    def reverse(self, head):
        cur = head
        prev = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        newHead = prev
        return newHead

    # 會從低位數往高位數做兩linklist的加法直到結束
    # 因為不是in-place所以不需知道l1、l2的長度, 都丟到res即可
    def plus(self, l1, l2):
        curL1 = l1
        curL2 = l2
        # res最後會做為加完結果之linklist的head
        # 一開始為None讓創建node時有地方可以指向
        res = None
        # carry代表要進位的數值
        carry = 0
        # 只要有個個linklist還沒到None就要繼續
        # 注意當還有需要進位的數時也要繼續
        while curL1 is not None or curL2 is not None or carry!=0:
            # 因None沒有.val無法相加, 所以當None時給0
            if curL1 is None:
                curL1Val = 0
            else:
                curL1Val = curL1.val
            if curL2 is None:
                curL2Val = 0
            else:
                curL2Val = curL2.val
            # 將該位數的總和加起來
            tmp = curL1Val+curL2Val+carry
            # 要進位的數值
            carry = tmp//10
            # 實際上在這位數的數值
            tmp %= 10
            # 創建一個resNode用來放置tmp, 也就是resNode.val = tmp
            resNode = ListNode(tmp)
            # 創建完這位數後, 指向前面一個位數
            resNode.next = res
            # 目前這個位數變成下一個更高位數所指向的目標
            res = resNode
            # 因None沒有.next, 所以判斷當非None的node才要繼續
            if curL1 is not None:
                curL1 = curL1.next
            if curL2 is not None:
                curL2 = curL2.next
        # 結果會是一個由高位數往低位數指向的linklist, 剛好等同題目要求
        return res

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 為了從低位數開始對齊做家法, 所以先將linklist反轉並從低位->高位
        newL1 = self.reverse(l1)
        newL2 = self.reverse(l2)
        # 因res剛好是高位->低位, 不用再反轉
        return self.plus(newL2, newL1)

# By stack, time: O(max(m, n)), space: O(m+n)
# 好處是基本上不會動到原本的linklist結構, 但花費額外空間
# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         s1, s2 = [], []
#         while l1:
#             s1.append(l1.val)
#             l1 = l1.next
#         while l2:
#             s2.append(l2.val)
#             l2 = l2.next
#         ans = None
#         carry = 0
#         while s1 or s2 or carry != 0:
#             a = 0 if not s1 else s1.pop()
#             b = 0 if not s2 else s2.pop()
#             cur = a + b + carry
#             carry = cur // 10
#             cur %= 10
#             curnode = ListNode(cur)
#             curnode.next = ans
#             ans = curnode
#         return ans

# @lc code=end