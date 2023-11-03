<<<<<<< HEAD
#
# @lc app=leetcode id=1637 lang=python3
#
# [1637] Widest Vertical Area Between Two Points Containing No Points
#

# @lc code=start
# 以y軸無限當延伸來看, 回傳兩點之間區域沒任何點的最寬距離
# 其實就是看兩點之間x軸差距最多多少

# By sort, time: O(nlogn), space: O(logn), 排序所花費的空間
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        # 將points裡面的點根據x軸來排序, 記熟lambda用法
        # 好像默認不給參數也是照x[0]來排的
        points.sort(key = lambda x: x[0])
        res = 0
        # 一個個看兩點之間x軸差距, 最大的就是答案
        for i in range(1, len(points)):
            res = max(res, points[i][0]-points[i-1][0])
        return res
            

# @lc code=end

=======
#
# @lc app=leetcode id=1637 lang=python3
#
# [1637] Widest Vertical Area Between Two Points Containing No Points
#

# @lc code=start
# 以y軸無限當延伸來看, 回傳兩點之間區域沒任何點的最寬距離
# 其實就是看兩點之間x軸差距最多多少

# By sort, time: O(nlogn), space: O(logn), 排序所花費的空間
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        # 將points裡面的點根據x軸來排序, 記熟lambda用法
        # 好像默認不給參數也是照x[0]來排的
        points.sort(key = lambda x: x[0])
        res = 0
        # 一個個看兩點之間x軸差距, 最大的就是答案
        for i in range(1, len(points)):
            res = max(res, points[i][0]-points[i-1][0])
        return res
            

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
