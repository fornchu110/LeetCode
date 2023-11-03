<<<<<<< HEAD
#
# @lc app=leetcode id=771 lang=python3
#
# [771] Jewels and Stones
#

# @lc code=start
# By hash table, time: O(m+n), space: O(m), mæ˜¯jewlesé•·åº¦, næ˜¯stonesé•·åº¦
# è¦çœ‹jewelså…§çš„å­—ç¬¦å…±åœ¨jewelså…§å‡ºç¾å¹¾æ¬¡
# å…ˆå°‡jewelså…§å®¹èµ°è¨ªä¸€æ¬¡åŠ å…¥hash table, åˆå†èµ°è¨ªä¸€æ¬¡stoneçœ‹æ¬¡æ•¸
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        # setåœ¨pythonæ˜¯hast tableçš„ä¸€ç¨®, ä¸æœƒæœ‰é‡è¤‡å…ƒç´ 
        # å¯ä»¥ç”¨addå’Œremove, ä¸åƒlistç”¨appendåŠ å…¥
        jewelsSet = set(jewels)
        for i in stones:
            if i in jewelsSet:
                res += 1
        return res

# By for loop, time: O(m*n), space: O(1), mæ˜¯jewlesé•·åº¦, næ˜¯stonesé•·åº¦
# è¦çœ‹jewelså…§çš„å­—ç¬¦å…±åœ¨jewelså…§å‡ºç¾å¹¾æ¬¡
# é€™ç¨®å¯«æ³•æ¯æ¬¡èµ°è¨ªstoneså…§å®¹éƒ½å›å»jewelsèµ°è¨ªä¸€é, æ‰€ä»¥æ˜¯m*n
# class Solution:
#     def numJewelsInStones(self, jewels: str, stones: str) -> int:
#         res = 0
#         for i in stones:
#             if i in jewels:
#                 res += 1
#         return res

# @lc code=end

=======
#
# @lc app=leetcode id=771 lang=python3
#
# [771] Jewels and Stones
#

# @lc code=start
# By hash table, time: O(m+n), space: O(m), m¬Ojewlesªø«×, n¬Ostonesªø«×
# ­n¬İjewels¤ºªº¦r²Å¦@¦bjewels¤º¥X²{´X¦¸
# ¥ı±Njewels¤º®e¨«³X¤@¦¸¥[¤Jhash table, ¤S¦A¨«³X¤@¦¸stone¬İ¦¸¼Æ
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        # set¦bpython¬Ohast tableªº¤@ºØ, ¤£·|¦³­«½Æ¤¸¯À
        # ¥i¥H¥Îadd©Mremove, ¤£¹³list¥Îappend¥[¤J
        jewelsSet = set(jewels)
        for i in stones:
            if i in jewelsSet:
                res += 1
        return res

# By for loop, time: O(m*n), space: O(1), m¬Ojewlesªø«×, n¬Ostonesªø«×
# ­n¬İjewels¤ºªº¦r²Å¦@¦bjewels¤º¥X²{´X¦¸
# ³oºØ¼gªk¨C¦¸¨«³Xstones¤º®e³£¦^¥hjewels¨«³X¤@¹M, ©Ò¥H¬Om*n
# class Solution:
#     def numJewelsInStones(self, jewels: str, stones: str) -> int:
#         res = 0
#         for i in stones:
#             if i in jewels:
#                 res += 1
#         return res

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
