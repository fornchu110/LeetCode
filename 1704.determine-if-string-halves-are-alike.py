#
# @lc app=leetcode id=1704 lang=python3
#
# [1704] Determine if String Halves Are Alike
#

# @lc code=start
# 給一字串, 將字串從中切一半後看兩邊的aeiou, AEIOU這些母音的數量是否相同, 相同return true, 否則false

# By string proccessing, time: O(n), space: O(n)), n是給定字串長度
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # 直接建立一個查找母音用的字串, 判斷切一半的字串之字元是否存在內即可
        # 不需要使用hash, 但應該是同理
        # c語言可以用strchr()達到類似效果, 先建一個VOWELS字串做為查找用的hash
        # strchr(s, ch)代表ch位於s中第一次出現的位置, 若有找到會回傳位址沒找到回傳NULL, 因此可以用來做判斷ch是否存在s中
        VOWELS = "aeiouAEIOU"
        # list切片s[a:b], a是起點b是終點, 沒參數就默認index 0開始, 尾端結束
        a, b = s[:len(s)//2], s[len(s)//2:]
        return sum(c in VOWELS for c in a) == sum(c in VOWELS for c in b)
        
# @lc code=end

