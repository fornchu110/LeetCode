#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
# 給一數組height, 裡面的元素是不同高度的lines, 找出以lines當圍牆所能包圍的最多水量
# 注意這題沒有DP解, 因為沒有重複的子問題, 但可以理解為Greedy

# By double pointer, time: O(n), space: O(1)
# 兩個pointer分別指向頭尾的lines, 找出有可能的最大水量
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        res = 0
        # 因為只有一個lines沒辦法包圍, 所以當r-l==0時就終止
        while r-l!=0:
            # 這就是lines間的長度, 想成水桶寬度
            len_of_lines = r-l
            # 水量是以較低的lines決定的, 一邊就算比較高也會洩漏出來
            # 水量就是低的lines*寬度
            if min(height[l], height[r])*len_of_lines > res:
                res = min(height[l], height[r])*len_of_lines
            # 精隨在於此, 每輪選擇高度較低的lines移動
            # 為何選擇高度較低的lines移動是正確的?
            # 因為在寬度只能縮小的情況, 無論另一邊變多高, 水量仍受限在較低的lines這邊
            # Ex, 2和4, 距離10, 水量=20, 今天如果距離要變9而移動的是4, 就算4變成400, 水量仍是18(2*9)
            # 只有移動了更小的lines才有"可能"得到最大值, 今天移動2變成200, 這時水量雖然受限於4, 但變成36(4*9)
            if height[l]<height[r]:
                l += 1
            # 兩lines一樣高的話移動誰都行, 我選擇移動r
            else:
                r -= 1
        return res
        
# @lc code=end

