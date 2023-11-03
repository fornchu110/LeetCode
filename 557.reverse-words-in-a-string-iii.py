#
# @lc app=leetcode id=557 lang=python3
#
# [557] Reverse Words in a String III
#

# @lc code=start
# By string processing, time: O(n), space = O(1), n = len(s)
# 要將給定多個單字順序不變下, 反轉單字的內容
# 利用reversed()將字串內容反轉, 注意reversed()回傳值是一個list
class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        # 字串也可以反轉, reversed()返回值是list, .reverse()則只能用在list不可用在字串
        # split()的原因是這題並非完全從尾反轉至頭, 而是單字順序不變只反轉每個單字內容
        # 因此split()將單字成為list中不同元素後, 再依序對這些元素做反轉
        s = s.split()
        for i in s:
            # 寫成i = "".join(i[::-1])也可以, [::-1]是反轉切片
            i = "".join(reversed(i))
            res.append(i)
        return " ".join(res)
        
# @lc code=end

