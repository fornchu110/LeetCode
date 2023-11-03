<<<<<<< HEAD
#
# @lc app=leetcode id=1614 lang=python3
#
# [1614] Maximum Nesting Depth of the Parentheses
#

# @lc code=start
# 給字串s, 找出括號的最大層數, 題目保證括號一定成對, 不會出現"(()"

# By stack, time: O(n), space: O(1)
# 每遇到一個'('多一層, 遇到一個')'少一層
# 所以當遇到'('比較與歷史層數哪個較多, 更大的是答案
class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        cnt = 0
        for i in s:
            if i=='(':
                cnt += 1
                res = max(res, cnt)
            elif i==')':
                cnt -= 1
        return res

# @lc code=end

=======
#
# @lc app=leetcode id=1614 lang=python3
#
# [1614] Maximum Nesting Depth of the Parentheses
#

# @lc code=start
# 給字串s, 找出括號的最大層數, 題目保證括號一定成對, 不會出現"(()"

# By stack, time: O(n), space: O(1)
# 每遇到一個'('多一層, 遇到一個')'少一層
# 所以當遇到'('比較與歷史層數哪個較多, 更大的是答案
class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        cnt = 0
        for i in s:
            if i=='(':
                cnt += 1
                res = max(res, cnt)
            elif i==')':
                cnt -= 1
        return res

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
