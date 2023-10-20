#
# @lc app=leetcode id=1816 lang=python3
#
# [1816] Truncate Sentence
#

# @lc code=start
# By string processing, time: O(n), space: O(1), n=len(str)
# 要求return給定句子s中前k個單字
# 利用split把句子分散成不同單字放在list內, k以內就append到res
# 最後將res用" ".join()的方式從list變回一個句子字串
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        res = []
        for idx, i in enumerate(s.split()):
            if idx<k:
                res.append(i)
        return " ".join(res)

# By index, time: O(n), space: O(1)
# 走訪s中的字符, 利用遇到空格或結尾判斷一個單字結束並獲得index
# 最後return開頭到index內的s
# class Solution:
#     def truncateSentence(self, s: str, k: int) -> str:
#         cnt = 0
#         for i in range(1, len(s)+1):
#             if i==len(s) or s[i]==" ":
#                 cnt += 1
#                 if cnt==k:
#                     end = i
#                     break
#         return s[:end]
                    
# @lc code=end

