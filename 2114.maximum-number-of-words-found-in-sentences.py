#
# @lc app=leetcode id=2114 lang=python3
#
# [2114] Maximum Number of Words Found in Sentences
#

# @lc code=start
# By for loop, time: O(m), space: O(1), m是指所有sentences之字符總數
# 會把所有字符都看一遍, python用max()和count()能更快
# 找出給定sentences中單字數最多的那個並回傳值
# 其實可以找每具sentence的空白數, 再+1就是單字數
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res = 0
        for i in sentences:
            cnt = 0
            # python可以只用下面這句count來計算空白數
            # cnt = i.count(' ') + 1
            # 對sentence[i]中每個字符j判斷是否為空白
            for j in i:
                if j==" ":
                    cnt += 1
            # python可以直接max(cnt, res)來看哪個比較大
            if cnt>res:
                res = cnt
        res += 1
        return res
        
# @lc code=end

