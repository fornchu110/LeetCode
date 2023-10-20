#
# @lc app=leetcode id=1828 lang=python3
#
# [1828] Queries on Number of Points Inside a Circle
#

# @lc code=start
# By enumerate, time: O(m*n), space: O(1), m是圓心數量, n是點數量
# 這題給圓心和圓半徑, 求給定n的points位於不同圓內的數量
class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = list()
        # python可以直接用相對應的格式獲得數據, 更直觀
        for (cx, cy, cr) in queries:
            tmp = 0
            for (px, py) in points:
                if(cx-px)**2+(cy-py)**2<=cr**2:
                    tmp += 1
            res.append(tmp)
        # 再優化可以把res = [0]*len(queries)
        # 然後就能省下tmp空間, 直接for i, (cx, cy, cr) in enumerate(queries):
        # 同時獲得index i和迭代(cx, cy, cr), 這樣在if成立時res[i] += 1即可

        # 一開始的做法, 用i去迭代圓心, 用j迭代點, index來存取內容
        # 更像c語言寫法
        # for i in queries:
        #     tmp = 0
        #     for j in points:
        #         if (i[0]-j[0])**2+(i[1]-j[1])**2<=i[2]**2:
        #             tmp += 1
        #     res.append(tmp)
        return res

# @lc code=end

