#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# By fast-slow pointer, time: O(n), space: O(1)
# 這類題目是用node.next指向的位置判斷是否有cycle, 也就是說python的node其實都是指向各node位置的pointer
# 不是回傳整個linklist的類型應該不需要dummy node?
# 這種linklist相遇類型的題目感覺都要用總共a+b個node去想, cycle有b個node
# fast和slow相遇時有兩特性: 一是fast必定走slow兩倍步數, 二是fast比slow"多走"了n個cycle的長度b(倒追必多跑n圈)
# 為何是n而不是1是因考慮a比b大的狀況, Ex: a = 5, b = 3的話根本還沒走完a, 不可能到cycle入口
# 總結下來就是f = 2s且f = s+nb, 得出在fast slow相遇時, s = nb
# 每次slow走到cycle入口必走a+nb步, 所以只要fast slow相遇時再走a步就會到cycle入口node
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        while fast!=None and fast.next!=None:
            # 如果fast走到linklist結束代表沒cycle
            # 像這種例外或終止條件都要寫在最前面
            fast = fast.next.next
            slow = slow.next
            # 第二種情況, fast和slow第一次相遇, 這時希望找出index
            if fast==slow:
                # 用來找出cycle入口node之index
                # 將fast從head開始跟著slow一起走一步, 當這次fast = slow代表走了a
                # 也就是到了cycle入口的node
                fast = head
                while fast!=slow:
                    fast = fast.next
                    slow = slow.next
                return fast
        return None
        
# @lc code=end