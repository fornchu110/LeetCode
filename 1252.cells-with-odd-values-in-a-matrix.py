#
# @lc app=leetcode id=1252 lang=python3
#
# [1252] Cells with Odd Values in a Matrix
#

# @lc code=start
# 給mxn的初始化矩陣和一陣列indices, indices內每一項[ri、ci]代表將第ri列以及第ci行所有元素+1
# 最後return矩陣中有多少odd
# By simulation, time: O(q*(m+n)+m*n), space: O(m*n), 其中q = len(indices)
# 模擬題目做的事情, 走訪indices將指定的行列一個個+1, 最後再數矩陣中的odd數
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        res = 0
        arr = [[0 for i in range(n)] for j in range(m)]
        # 走訪indices所有元素
        # q*(m+n)的部分, 記住複雜度的+是代表取較大的那個
        for [r, c] in indices:
            # r代表第r列的n個元素要+1
            for i in range(n):
                arr[r][i] += 1
            # c代表第c行的m個元素要+1
            for i in range(m):
                arr[i][c] += 1
        # 數結果
        # m*n的部分
        for i in range(m):
            for j in range(n):
                if arr[i][j]%2:
                    res += 1
        return res
    
        
# @lc code=end 

