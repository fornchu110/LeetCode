#
# @lc app=leetcode id=1832 lang=python3
#
# [1832] Check if the Sentence Is Pangram
#

# @lc code=start
# By hash, time: O(n), space: O(1), n是len(sentence)
# 判斷sentence中有沒出現過所有英文小寫字母
# 這題因為確定key的數量, 也可以用ascii碼使用ord()配合index array做
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # 建hash
        hash = dict()
        cnt = 0
        # 當字符為沒出現過的字母, 放入hash並放cnt+1
        # 有出現過就不管
        for i in sentence:
            if i not in hash:
                hash[i] = 1
                cnt += 1
        # 最後看是否放入了全部26個字母
        return cnt==26
        
# @lc code=end

