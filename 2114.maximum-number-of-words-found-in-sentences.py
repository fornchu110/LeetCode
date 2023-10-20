#
# @lc app=leetcode id=2114 lang=python3
#
# [2114] Maximum Number of Words Found in Sentences
#

# @lc code=start
# By for loop, time: O(m), space: O(1), m琌┮Τsentencesぇ才羆计
# 穦р┮Τ才常筂, pythonノmax()㎝count()е
# т倒﹚sentencesい虫计程ê肚
# ㄤ龟т–ㄣsentenceフ计, +1碞琌虫计
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res = 0
        for i in sentences:
            cnt = 0
            # pythonノ硂countㄓ璸衡フ计
            # cnt = i.count(' ') + 1
            # 癸sentence[i]い–才j耞琌フ
            for j in i:
                if j==" ":
                    cnt += 1
            # python钡max(cnt, res)ㄓゑ耕
            if cnt>res:
                res = cnt
        res += 1
        return res
        
# @lc code=end

