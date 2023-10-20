#
# @lc app=leetcode id=2194 lang=python3
#
# [2194] Cells in a Range on an Excel Sheet
#

# @lc code=start
# By ord() and chr(), time: O(m*n), space: O(1), m為row數, n為column數
# 給起點和終點, 依序印出[起點, 終點]中所有元素
# 一個col走訪完再走訪下一格
class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        res = []
        # ord()用來獲得字符的ascii碼
        # 對起始ascii和終點ascii做for迴圈, 即可依序加入字符
        # 從起始col開始
        for i in range(ord(s[0]), ord(s[3]) + 1):
            # 同col下從起始row走訪到終點row
            for j in range(ord(s[1]), ord(s[4]) + 1):
                # 用+將字符連結起來
                # chr把ascii轉字符
                res.append(chr(i) + chr(j))
        return res

# @lc code=end

