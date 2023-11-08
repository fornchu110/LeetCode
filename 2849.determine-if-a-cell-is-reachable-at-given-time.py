# @lc code=start
# 給5個非負整數, (sx, sy)代表出發點, (fx、fy)代表終點, t代表花費時間每秒只能走一格, 可以重複走但不能原地踏步
# return 可不可以在t時間時剛剛好從出發點走到終點

# By greedy, time: O(1), space: O(1)
# 一開始可能會想說用畢式定理之類的, 但發現其實可以往斜(左上、右上、左下、右下)方向走
# 所以t時間能不能到達只跟距離比較長的那個軸有關, 畢竟可以斜走, 那距離短軸的必定能先被走完
class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        # 邊界條件, 雖然可以重複走和繞圈圈
        # 但注意只有一個情況沒辦法, 就是起始點一樣卻要求你動1步走到
        # 不能原地踏步所以必定False
        if fx==sx and fy==sy and t==1:
            return False
        xdis = abs(fx-sx)
        ydis = abs(fy-sy)
        return max(xdis, ydis)<=t
# @lc code=end
