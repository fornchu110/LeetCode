#
# @lc app=leetcode id=1921 lang=python3
#
# [1921] Eliminate Maximum Number of Monsters
#

# @lc code=start
# 給怪獸距離陣列dist和每分鐘移動速度speed陣列, 自己開場可以殺一隻, 之後每分鐘殺一隻
# 每過1分鐘第i隻怪獸會移動speed[i]的距離, 當第i隻怪獸的距離dist[i]等於0的當下就結束
# return結束之前能殺幾隻怪獸

# By sort, time: O(nlogn), space: O(n)
# 一開始以為只能照著順序從第0隻怪獸殺到第n-1隻怪獸
# 但其實這題可以不照順序殺怪獸, 找每分鐘當下距離最近的怪獸即可
# 怎麼樣可以找出每分鐘距離最近的怪獸? 其實就是根據他們的距離扣到0以下所花費的時間做排序
# 也就是根據arrival time將怪獸排序後, 找出殺怪獸的時間小於他到達時間的次數即可
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        res = 0
        n = len(dist)
        arrival_time = [0 for i in range(n)]
        # 求出每個怪獸的到達時間
        for i in range(n):
            # python //往下取整, n//m往上取的技巧就是求(n+m-1)//m
            arrival_time[i] = (dist[i]+speed[i]-1)//speed[i]
        # 依照到達時間做排序
        arrival_time.sort()
        # 起始時間
        now = 0
        # 找出每分鐘過去能殺的怪獸量
        for i in range(n):
            # 抵達之前能殺那就多一隻
            if arrival_time[i]>now:
                res += 1
            # 否則遊戲結束
            else:
                break
            now += 1
        return res

# @lc code=end

