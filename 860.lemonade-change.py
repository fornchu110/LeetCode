#
# @lc app=leetcode id=860 lang=python3
#
# [860] Lemonade Change
#

# @lc code=start

# By Greedy, time: O(n), space: O(1)
# 只用兩個變量存five和ten的做法, greedy在要找15時優先選擇找10+5而非5*3
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        for i in range(len(bills)):
            if bills[i]==5:
                five += 1
            elif bills[i]==10:
                if five>=1:
                    five -= 1
                    ten += 1
                else:
                    return False
            elif bills[i]==20:
                if ten>=1 and five>=1:
                    five -= 1
                    ten -= 1
                elif five>=3:
                    five -= 3
                else:
                    return False
        return True

# By Greedy hashtable, time: O(n), space: O(1)
# 總之就是遇到5元直接收, 遇到10元看有沒有5能找, 遇到20看有沒有15能找
# 但實際上不該用hasttable存5元和10元數量, 20也不用存, 直接兩個變量即可
# class Solution:
#     def lemonadeChange(self, bills: List[int]) -> bool:
#         change = dict([(5, 0), (10, 0), (20, 0)])
#         for i in range(len(bills)):
#             if bills[i]==5:
#                 change[5] += 1
#             elif bills[i]==10:
#                 if change[5]>=1:
#                     change[5] -= 1
#                     change[10] += 1
#                 else:
#                     return False
#             elif bills[i]==20:
#                 if change[10]>=1 and change[5]>=1:
#                     change[5] -= 1
#                     change[10] -= 1
#                     change[20] += 1
#                 elif change[5]>=3:
#                     change[5] -= 3
#                     change[20] += 1
#                 else:
#                     return False
#         return True


        
# @lc code=end

