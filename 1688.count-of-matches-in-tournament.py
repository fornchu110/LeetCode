#
# @lc app=leetcode id=1688 lang=python3
#
# [1688] Count of Matches in Tournament
#

# @lc code=start
# By simulation, time: O(log(n)), space: O(1)
# 算出被淘汰的隊伍數, 照著題目給的做迴圈
class Solution:
    def numberOfMatches(self, n: int) -> int:
        res = 0
        while(n!=1):
            # 用n&1判斷n是否為奇數
            if n&1:
                # 用>>1代表//2
                res += (n-1)>>1
                # 注意>>運算的優先權比+=*/低所以要括號
                n = n-((n-1)>>1)
            else:
                res += n>>1
                n = n-(n>>1)
        return res

# By math, time: O(1), space: O(1)
# 實際上只會有一人獲勝, 所以n人參賽就有n-1人被淘汰
# class Solution:
#     def numberOfMatches(self, n: int) -> int:
#         return n-1

# @lc code=end

