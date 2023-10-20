#
# @lc app=leetcode id=804 lang=python3
#
# [804] Unique Morse Code Words
#

# @lc code=start
# By string proccessing, time: O(n), space: O(n), n為len(words)
# 將words內每個字串轉換成密碼後, 找出這些字串不重複的數量
# 找不重複就要想到set(), 用len(set)即是不重複數量
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res = set()
        for i in words:
            tmp = ""
            for j in i:
                # 利用"a"+"b" = "ab", 在string做+=讓同一字串內不同密碼連結再一起
                # c語言是使用sprinf()做連結, 透過要處理的字符所在位址來做
                tmp += code[ord(j)-ord("a")]
            # 每次將處理完的字串加進res, 注意set是用.add()不是append
            res.add(tmp)
        return len(res)
        # 上面那段的一行版, 但看不懂如何把轉換過的字元join的
        # return len(set("".join(code[ord(ch) - ord('a')] for ch in word) for word in words))

# @lc code=end

