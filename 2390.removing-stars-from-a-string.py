<<<<<<< HEAD
#
# @lc app=leetcode id=2390 lang=python3
#
# [2390] Removing Stars From a String
#

# @lc code=start
# 給一字串s, 當走訪字串時遇到'*'要將左方一個字元消去, return處理完的字串

# By stack, time: O(n), space: O(n)


class Solution:
    def removeStars(self, s: str) -> str:
        # 利用list模擬stack     
        res = []
        # 依序將字元push進
        for i in s:
            if ord('a')<=ord(i)<=ord('z'):
                res.append(i)
            # 遇到'*'就將尾端的字元pop出來
            elif i=='*':
                res.pop()
        # 最後用"".join(res)轉換回字串
        res = "".join(res)
        return res
        
# @lc code=end

=======
#
# @lc app=leetcode id=2390 lang=python3
#
# [2390] Removing Stars From a String
#

# @lc code=start
# 給一字串s, 當走訪字串時遇到'*'要將左方一個字元消去, return處理完的字串

# By stack, time: O(n), space: O(n)


class Solution:
    def removeStars(self, s: str) -> str:
        # 利用list模擬stack     
        res = []
        # 依序將字元push進
        for i in s:
            if ord('a')<=ord(i)<=ord('z'):
                res.append(i)
            # 遇到'*'就將尾端的字元pop出來
            elif i=='*':
                res.pop()
        # 最後用"".join(res)轉換回字串
        res = "".join(res)
        return res
        
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
