<<<<<<< HEAD
#
# @lc app=leetcode id=2391 lang=python3
#
# [2391] Minimum Amount of Time to Collect Garbage
#

# @lc code=start
# By string processing, time: O(n), space: O(1), n為garbage內字元數量
# 找出從頭(index = 0)處理G、P、M所花費時間, 只要字串內有其一就花1時間, 從garbage內index移動到index+1花費travel[index的時間]
# 求出處理完G、P、M花費總時間
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        res, g, m, p, idx = 0, 0, 0, 0, 0
        for idx , i in enumerate(garbage):
            res += len(i)
            # 找字元是否存在字串內不要用in, 用迴圈走訪比較準
            for j in i:
                if "M"==j:
                    m = idx
                elif "G"==j:
                    g = idx
                elif "P"==j:
                    p = idx
        for i in range(m):
            res += travel[i]
        for i in range(g):
            res += travel[i]
        for i in range(p):
            res += travel[i]
        return res
        
# @lc code=end

=======
#
# @lc app=leetcode id=2391 lang=python3
#
# [2391] Minimum Amount of Time to Collect Garbage
#

# @lc code=start
# By string processing, time: O(n), space: O(1), n為garbage內字元數量
# 找出從頭(index = 0)處理G、P、M所花費時間, 只要字串內有其一就花1時間, 從garbage內index移動到index+1花費travel[index的時間]
# 求出處理完G、P、M花費總時間
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        res, g, m, p, idx = 0, 0, 0, 0, 0
        for idx , i in enumerate(garbage):
            res += len(i)
            # 找字元是否存在字串內不要用in, 用迴圈走訪比較準
            for j in i:
                if "M"==j:
                    m = idx
                elif "G"==j:
                    g = idx
                elif "P"==j:
                    p = idx
        for i in range(m):
            res += travel[i]
        for i in range(g):
            res += travel[i]
        for i in range(p):
            res += travel[i]
        return res
        
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
