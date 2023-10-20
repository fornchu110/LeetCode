#
# @lc app=leetcode id=1769 lang=python3
#
# [1769] Minimum Number of Operations to Move All Balls to Each Box
#

# @lc code=start

# By divide array and dp, time: O(n), space: O(1)
# 求將index以外所有1移動到index所要花的次數, 一次只能移動1個index
# 這種題目可以想要看左側和右側, 先求出以0為index的右側再邊走訪邊算出左側
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # 當下index左側有left個1, 右側有right個1
        left, right, operations = int(boxes[0]), 0, 0
        # 先走訪一次知道index 0(起始位置)右邊有幾個1
        for i in range(1, len(boxes)):
            if boxes[i] == '1':
                # 看到一個1就+1
                right += 1
                # 實際上移動到0的次數就是index步
                # Ex: 4走到0要花4步
                operations += i
        # res[0]就是剛剛算出的operations
        res = [operations]
        # 再走訪一次
        for i in range(1, len(boxes)):
            # 每走訪一個index, 所花的步數就會-右邊1的數量+左邊1的數量
            operations += left - right
            res.append(operations)
            if boxes[i] == '1':
                # 每走一個index遇到1, 代表下一個index右側會少一個1, 左側會多一個1
                left += 1
                right -= 1
        return res

# By for loop, time: O(n^2), space: O(1)
# 暴力解, 每走到一個index都從頭算
# class Solution:
#     def minOperations(self, boxes: str) -> List[int]:
#         res = list()
#         for i in range(len(boxes)):
#             s = sum(abs(j - i) for j, c in enumerate(boxes) if c == '1')
#             res.append(s)
#         return res
# @lc code=end

