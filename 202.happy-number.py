#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start

#By hashtable
class Solution:
    #找整數之各個位數平方和
    def getNext(self, num):
        happy_sum = 0
        while num:
            happy_sum += (num % 10) ** 2
            num = num // 10
        return happy_sum

    #使用雜湊表確認是否在循環
    def isHappy(self, n: int) -> bool:
        hashTable = dict()
        while True:
            n = self.getNext(n)
            if n == 1:
                return True
            if n in hashTable:
                return False
            else:
                hashTable[n] = 1
        
# @lc code=end
