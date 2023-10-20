#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
# 給羅馬數字串, 轉換成十進位數字

# By hash table ,time: O(n), space: O(k), k = 7, 就是羅馬數字基本元素數量
# 建立出hash後照著規則模擬即可
# 這題其實從右到左走訪更好, 這樣不用走訪第二次
class Solution:
    def romanToInt(self, s: str) -> int:
        hash = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0
        # 先走訪一次做加總
        for i in s:
            res += hash[i]
        # 把加過頭的扣回去
        for i in range(1, len(s)):
            # I是1但後面如果接V或X, 則代表將V或X-1, Ex: I = 1, V = 5, IV = 4
            if (s[i]=="V" or s[i]=="X") and s[i-1]=="I":
                res -= 2*hash["I"]
            # 與上面同理
            elif(s[i]=="L" or s[i]== "C") and s[i-1]=="X":
                res -= 2*hash["X"]
            elif(s[i]=="D" or s[i]== "M") and s[i-1]=="C":
                res -= 2*hash["C"]
        return res

# @lc code=end

