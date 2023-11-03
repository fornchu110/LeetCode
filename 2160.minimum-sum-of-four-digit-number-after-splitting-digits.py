#
# @lc app=leetcode id=2160 lang=python3
#
# [2160] Minimum Sum of Four Digit Number After Splitting Digits
#

# @lc code=start
# By greedy, time: O(1), space: O(1), 不知為何sort()不須增加時間複雜度
# 要將給定num每位數拆分成兩數, 並找出所有拆分組合內兩數和最小的那個和
# 注意input是1000~9999, 所以只會有四位數, 四位數拆成兩個兩位數最好(總和最小)
# 把較小的兩個位數放到兩數的十位數, 較大的兩位數放到兩數的個位數 
class Solution:
    def minimumSum(self, num: int) -> int:
        # 存放位數
        digits = list()
        # 將input的每個位數放進list
        while num:
            digits.append(num%10)
            num //= 10
        # 經過sort便得知較小和較大的位數是哪些, sort()由小到大
        digits.sort()
        return 10*(digits[0]+digits[1])+digits[2]+digits[3]

# @lc code=end

