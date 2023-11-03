<<<<<<< HEAD
#
# @lc app=leetcode id=2843 lang=python3
#
# [2843]   Count Symmetric Integers
#

# @lc code=start
# return low和high之間前n位元和和後n位元和相同的整數數量


# By simulation
# 更漂亮的寫法, 先將int轉成str計算位數
# 再用sum和切片計算前半與後半, 切片完的半邊字串用map轉換成int
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0
        for i in range(low, high + 1):
            s = str(i)
            n = len(s)
            if(n&1==0 and sum(map(int, s[:n//2]))==sum(map(int, s[n//2:]))):
               res += 1
        return res

# By simulation, time: O((low-high)log(high)), space: O(loghigh), n是high-low
# 用//=10的方式算當下的數字是幾位數, 如果是奇數位一定不對稱
# 偶數位檢查左半和右半的位數和即可
# class Solution:
#     def countSymmetricIntegers(self, low: int, high: int) -> int:
#         res = 0
#         for i in range(low, high+1):
#             now = i
#             tmp = []
#             while now!=0:
#                 tmp.append(now%10)
#                 now //= 10
            
#             if len(tmp)&1:
#                 continue
#             else:
#                 left = 0
#                 right = 0
#                 for j in range(1, len(tmp)+1):
#                     if j<=(len(tmp)/2):
#                         left += tmp[j-1]
#                     else:
#                         right += tmp[j-1]
#                 if left==right:
#                     res += 1
#         return res

# @lc code=end

=======
#
# @lc app=leetcode id=2843 lang=python3
#
# [2843]   Count Symmetric Integers
#

# @lc code=start
# return low和high之間前n位元和和後n位元和相同的整數數量


# By simulation
# 更漂亮的寫法, 先將int轉成str計算位數
# 再用sum和切片計算前半與後半, 切片完的半邊字串用map轉換成int
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0
        for i in range(low, high + 1):
            s = str(i)
            n = len(s)
            if(n&1==0 and sum(map(int, s[:n//2]))==sum(map(int, s[n//2:]))):
               res += 1
        return res

# By simulation, time: O((low-high)log(high)), space: O(loghigh), n是high-low
# 用//=10的方式算當下的數字是幾位數, 如果是奇數位一定不對稱
# 偶數位檢查左半和右半的位數和即可
# class Solution:
#     def countSymmetricIntegers(self, low: int, high: int) -> int:
#         res = 0
#         for i in range(low, high+1):
#             now = i
#             tmp = []
#             while now!=0:
#                 tmp.append(now%10)
#                 now //= 10
            
#             if len(tmp)&1:
#                 continue
#             else:
#                 left = 0
#                 right = 0
#                 for j in range(1, len(tmp)+1):
#                     if j<=(len(tmp)/2):
#                         left += tmp[j-1]
#                     else:
#                         right += tmp[j-1]
#                 if left==right:
#                     res += 1
#         return res

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
