#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#

# @lc code=start
# 給兩字串word1和word2, 以word1開始return將兩字串字元一一交錯後的字串

# By double pointer and string processing, time: O(m+n), space: O(1), m = len(word1), n = len(word2)
# time = O(m+n)是因仍是走訪兩個不同字串
# 用while迴圈從index 0開始先加入word1[idx]再加入word2[idx]
# 在字串還有內容時才加入, 長度為2的字串idx只能到1, 避免index out of range
# python用切片也能做到, 不需要list
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        idx = 0
        # while會做跟更長的字串長度相同的次數
        n = max(len(word1), len(word2))
        res = []
        while(n>0):
            if idx<len(word1):
                res.append(word1[idx])
            if idx<len(word2):
                res.append(word2[idx])
            idx += 1
            n -= 1
        # list轉字串
        return "".join(res)
# @lc code=end

