#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start
# 給一個數num, 將其各個位數相加, 若相加後的結果超過二位數那就繼續做, 直到剩下一位數為止

# By math, time: O(1), space: O(1)
# 用數學的方法證明, 用映射的想法去想
# 觀察到最後的結果一定是0~9, 所以要想辦法把num映射到0~9
# 而發現0只有一種情況就是一開始為0, 所以應該分開討論, 實際上是要映射到1~9
# %10錯了所以%9試試, 但發現num%9會映射到0~8, 要讓他映射到0~9所以做num%9+1
# 但num%9+1又會發現在個位數錯誤, 所以做(num-1)%9+1
class Solution:
    def addDigits(self, num: int) -> int:
        # 當num為0, 雖然num一樣是9的倍數, 但總和必然是0
        if num==0:
            return 0
        else:
            return (num-1)%9+1
        # 下面這段等同上面else那邊
        # # 當num是9的倍數且非0時, 總和會是9
        # elif num%9==0:
        #     return 9
        # # 否則總和會是num//9的餘數, 也就是num%9
        # else:
        #     return num%9

# By simulation, time: O(lognum), space: O(1)
# 用兩層while, 一層判斷num是否超過二位數, 超過二位數就用第二層while將每個位數相加
# 這種走訪每個位數的時間複雜度就是lognum
# class Solution:
#     def addDigits(self, num: int) -> int:
#         # 當num是二位數就要不斷做
#         while num>=10:
#             # 相加後的結果
#             res = 0
#             # 將num每位數相加
#             while num:
#                 res += num%10
#                 num //= 10
#             # 最後相加完的結果變成新的num
#             num = res
#         # num剩一位那直接就是答案
#         return num
    
# @lc code=end

