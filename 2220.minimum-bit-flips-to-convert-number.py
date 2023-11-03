#
# @lc app=leetcode id=2220 lang=python3
#
# [2220] Minimum Bit Flips to Convert Number
#

# @lc code=start
# By XOR and bitwise, time: O(log(n)), space: O(1), n是start和goal較大那值, log(n)即是走訪位數的複雜度
# 要把start經過一一翻轉二進位的bit轉換成goal, 問最少翻轉次數
# 也就是說只要看start和goal在二進位下不同bit的數量即可
# 利用XOR的性質, 1^1 = 0, 1^0 = 1, 將strat和goal做XOR就知道不同bit數量
# 再來從右一一看個位數的bit是否為1, 是1代表不同bit, res+1
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        res = 0
        tmp = start^goal
        # 0是終止條件的情況不用再寫!=0, while(0)自然會跳出
        while tmp:
            # if tmp&1:
            #     res += 1
            # 這樣寫上面那段更簡潔
            res += tmp&1
            tmp >>= 1
        return res
                
# @lc code=end

