#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
# By sort and recursive, time: 
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 這種題目要想到先sort
        candidates.sort()
        # 創建空陣列, []效能比list()好
        res = []
        # used表示已經取到數值的列表, remain表示距離target還差的值
        def find(idx, used, remain):
            for i in range(idx, len(candidates)):
                num = candidates[i]
                # 讓recursive同一級內不會出現相同元素, 但不同級之間可以
                if i>idx and candidates[i-1]==candidates[i]:
                    continue
                # 找到符合差值的num, 將其和當下used湊成一組
                if num == remain:
                    res.append(used+[num])
                    return
                # 因為已排序過, 所以若小於差值, 直接往下繼續找
                if num<remain:
                    find(i+1, used+[num], remain-num)
                # 不用再往下找了, 現在大於差值後面一定都更大
                if num>remain:
                    return
        find(0,[], target)
        return res
        
# @lc code=end

