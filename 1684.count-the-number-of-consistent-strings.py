<<<<<<< HEAD
#
# @lc app=leetcode id=1684 lang=python3
#
# [1684] Count the Number of Consistent Strings
#

# @lc code=start
# By hash: time: O(n), space: O(k), n = len(words), space k程穦Τ26璣ゅ 
# 耞倒﹚﹃いΤ碭パallowedず甧才篶Θ
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        hash = dict()
        res = 0
        for i in allowed:
            if i not in hash:
                hash[i] = 1
        for i in words:
            # ノflag耞琌allowedず才舱Θ
            flag = 1
            for j in i:
                if j not in hash:
                    flag = 0
                    break
            # flag = 1allowed舱Θ, 玥flag穦琌0
            if flag:
                res += 1
        return res
        
# @lc code=end

=======
#
# @lc app=leetcode id=1684 lang=python3
#
# [1684] Count the Number of Consistent Strings
#

# @lc code=start
# By hash: time: O(n), space: O(k), n = len(words), space k程穦Τ26璣ゅ 
# 耞倒﹚﹃いΤ碭パallowedず甧才篶Θ
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        hash = dict()
        res = 0
        for i in allowed:
            if i not in hash:
                hash[i] = 1
        for i in words:
            # ノflag耞琌allowedず才舱Θ
            flag = 1
            for j in i:
                if j not in hash:
                    flag = 0
                    break
            # flag = 1allowed舱Θ, 玥flag穦琌0
            if flag:
                res += 1
        return res
        
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
