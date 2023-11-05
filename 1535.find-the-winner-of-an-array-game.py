#
# @lc app=leetcode id=1535 lang=python3
#
# [1535] Find the Winner of an Array Game
#

# @lc code=start
# 給一數組arr和整數k, 每輪前兩個元素比大小, 大的是winner, 輸的要放到arr尾端
# return 連續獲勝k次的元素

# By simmulation, time: O(n), space: O(1)
# nums內元素必定不同
# 雖然輸的要移動到尾端, 但實際這樣操作會超時
# 觀察得出無論其實arr內每個元素都會有機會被比較
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        # 邊界條件
        if k==1:
            return max(arr[0], arr[1])
        n = len(arr)
        prev_winner = max(arr[0], arr[1])
        win_cnt = 1
        
        # 不用做刪除插入操作, 可以觀察到
        # arr內每個元素都會被比較, 比較對象是上一輪的贏家
        for i in range(2, n):
            # 當上一輪的贏家又贏了
            if prev_winner>arr[i]:
                win_cnt += 1
                # 只要連續贏到k次就return
                if win_cnt == k:
                    return prev_winner
            # 上一輪的贏家輸了, arr[i]變贏家
            elif prev_winner<arr[i]:
                prev_winner = arr[i]
                win_cnt = 1
            # 更新res為贏家
            res = max(prev_winner, arr[i])
            
        return res
    
# @lc code=end

