#
# @lc app=leetcode id=1684 lang=python3
#
# [1684] Count the Number of Consistent Strings
#

# @lc code=start
# By hash: time: O(n), space: O(k), n = len(words), space k最多只會有26個英文 
# 判斷給定字串中有幾個只由allowed內容的字符構成
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        hash = dict()
        res = 0
        for i in allowed:
            if i not in hash:
                hash[i] = 1
        for i in words:
            # 用flag判斷是否全為allowed內字符組成
            flag = 1
            for j in i:
                if j not in hash:
                    flag = 0
                    break
            # flag = 1代表全為allowed組成, 否則flag會是0
            if flag:
                res += 1
        return res
        
# @lc code=end

