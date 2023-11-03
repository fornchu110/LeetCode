#
# @lc app=leetcode id=319 lang=python3
#
# [319] Bulb Switcher
#

# @lc code=start
# 給n個燈泡一開始是關閉, 第1輪打開所有, 第2輪每2個關閉, 也就是說第i輪要切換i倍數燈泡的開關, return n輪後有多少燈泡亮著

# By math, time: O(1), space: O(1)
# 觀察規律發現, 第i個燈泡被切換的次數就是其因數個數
# 所以有偶數個因數的燈泡最後會暗, 有奇數個因數的燈泡最後會亮
# 因為因數兩兩成對, Ex: 2是8的因數, 那8/2 = 4也是8個因數, 這種原因, 可以發現只有一種情況因數不成對
# 那就是完全平方數, Ex: 3是9的因數, 但9/3 = 3已經算過了
# 所以只有當i是完全平方數才會有奇數個因數, 因此檢查n個燈泡完全平方數的數量就是答案
# n以內完全平方數的個數就是根號n
class Solution:
    def bulbSwitch(self, n: int) -> int:
        # +0.5是為了在浮點運算時向下取整, 這題不加也會過
        return int(sqrt(n+0.5))

# @lc code=end

