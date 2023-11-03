#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
# 將給定的數字n, 其二進位表示法整個倒過來

# By divide and conquer, time: O(1), space: O(1)
# 不需要迴圈, 想法是切一半兩兩交換, 這兩個一半內又切一半倆倆交換, 直到一個和一個交換後剛好就會是反轉
# 32 = 2^5, 所以總共會切5次
class Solution:
    def reverseBits(self, n):
        # 低16bits和高16bits交換
        n = (n>>16)|(n<<16)
        # 每16bits中低8bits和高8bits交換...下面以此類推
        # 交換實際上是用位移達成, 而用0x...這些mask決定哪些bits要移動
        # 0xff00ff00代表左半和右半16bits中各自的左8bits, 因左右交換所以要往右8bits
        # 0x00ff00ff代表左半和右半16bits中各自的右8bits, 下面都以此類推 
        n = ((n&0xff00ff00)>>8)|((n&0x00ff00ff)<<8)
        n = ((n&0xf0f0f0f0)>>4)|((n&0x0f0f0f0f)<<4)
        n = ((n&0xcccccccc)>>2)|((n&0x33333333)<<2)
        n = ((n&0xaaaaaaaa)>>1)|((n&0x55555555)<<1)
        return n

# By bitwise, time: O(1), space: O(1)
# python整數長度無限, 為了模擬一般int所以只做32輪, 因此O(1)
# 非python不做32bits限制的話time就會是O(logn)
# class Solution:
#     def reverseBits(self, n):
#         res = 0
#         # 假設int有32bit
#         for i in range(32):
#             # res先左移1bit, 再和n&1做|, 最後將結果存到res
#             # 對0做|等同於做+, 也就是在n為奇數時+1, 偶數時+0
#             # 永遠不會進位
#             # 第一輪0<<=1, 也就是0左移一位元後, 0後面接剩下的
#             # 也就是因此雖然range(32)有32輪, 但實際上只左移31次共32bit
#             # 也可改成|後再res<<=1, 但這樣左移32次共33bits, 所以return時要res>>1
#             res = res<<1|(n&1)
#             n >>= 1
#         return res
        
# @lc code=end

