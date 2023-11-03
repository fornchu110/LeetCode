#
# @lc app=leetcode id=1791 lang=python3
#
# [1791] Find Center of Star Graph
#

# @lc code=start

# By math, time: O(1), space: O(1)
# 原本想說出現最多次的那點, 但其實因題目是給星形圖, 只有中心才會出現兩次以上, 其他點都只會出現一次
# 因此取兩條edge找出共同的點就是答案
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # if edges[0][0]==edges[1][0] or edges[0][0]==edges[1][1]:
        #     return edges[0][0]
        # else:
        #     return edges[0][1] 
        # 上面那段的一行版
        return edges[0][0] if edges[0][0]==edges[1][0] or edges[0][0]==edges[1][1] else edges[0][1]


# By hash, time: O(n), space: O(n), n是點的數量
# # 給多組邊, 找中心點, 其實就是找出現最多次的那一點
# class Solution:
#     def findCenter(self, edges: List[List[int]]) -> int:
#         res = 0
#         max = 0
#         hash = dict()
#         for i in range(len(edges)):
#             for j in range(2):
#                 if edges[i][j] not in hash:
#                     hash[edges[i][j]] = 1
#                 else:
#                     hash[edges[i][j]] += 1
#         # 用hash.items()來同時走訪hash的key和value
#         for i, j in hash.items():
#             # 當找到val值最大的, 將其key記下來
#             if j>max:
#                 max = j
#                 res = i
#         return res
        
# @lc code=end

