#
# @lc app=leetcode id=2418 lang=python3
#
# [2418] Sort the People
#

# @lc code=start
# By zip and 列表生成式, time: O(n), space: O(1)
# 要求return照身高由高到低排序後的對應人名
# 用zip()將身高和名字一一走訪, 只加入人名
# zip後的list也可以排序
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        tmp = sorted(zip(heights, names), reverse = True)
        # res = [*zip(*tmp)][1]
        res = [name for height, name in tmp]
        return res
        
# By zip , time: O(n), space: O(1)
# class Solution:
#     def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
#         res = []
#         tmp = list(zip(heights, names))
#         # 將zip後的list排序, 因為sorted()是從小到大排序, reverse = True參數變從大到小排序
#         tmp  = sorted(tmp, reverse = True)
#         # 找排序過後的name
#         for height, name in tmp:
#             res.append(name)
#         return res

# @lc code=end

