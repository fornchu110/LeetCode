#
# @lc app=leetcode id=1290 lang=python3
#
# [1290] Convert Binary Number in a Linked List to Integer
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# By simulation and bitwise, time: O(n), space: O(1)
# 靠模擬binary轉decimal過程計算, 注意不需要先走訪一次list把node都記錄下來
# 當走到新node, 代表前面的值左移過去, 也就是*2, 而結果就是再加上當下node.val
# 這樣做不用走訪就省時間, 也省下將node.val記錄下來的空間
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        cur = head
        res = 0
        while(cur!=None):
            #res = res*2+cur.val, 最直觀的做法
            #但binary可以做位運算, bitwise操作更加省時間
            #<<1代表左移也就是*2效果, |來加上cur.val
            res = (res<<1)|cur.val 
            cur = cur.next
        return res
        
# @lc code=end

