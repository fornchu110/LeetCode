#
# @lc app=leetcode id=1534 lang=python3
#
# [1534] Count Good Triplets
#

# @lc code=start
# 給一陣列arr和三整數a、b、c, 找出arr中三個漸進的index i、j、k
# 使得|arr[i]-arr[j]|<=a、|arr[j]-arr[k]|<=b、|arr[i]-arr[k]]<=c
# return符合條件的三index組數量

# By triple for loop(simulation), time: O(n^3), space: O(1)
# 由小至大的index一個個檢查找出符合條件的
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        res = 0
        # index不會重複, i後面至少還有j和k所以做到倒數第三個就可
        for i in range(len(arr)-2):
            for j in range(i+1, len(arr)-1):
                # 優化避免做完全部三迴圈的方式
                # 已經有index i、j, 因為條件要全符合
                # 所以先判斷跟i、j有關的條件是否符合, 不符合就不用看跟k有關的條件了, 有符合再做for迴圈
                if abs(arr[i]-arr[j])<=a:
                    for k in range(j+1, len(arr)):
                        if abs(arr[j]-arr[k])<=b and abs(arr[i]-arr[k])<=c:
                            res += 1
        return res
                                                    
# @lc code=end

