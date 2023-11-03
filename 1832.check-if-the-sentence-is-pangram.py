<<<<<<< HEAD
#
# @lc app=leetcode id=1832 lang=python3
#
# [1832] Check if the Sentence Is Pangram
#

# @lc code=start
# By hash, time: O(n), space: O(1), n琌len(sentence)
# 耞sentenceいΤ⊿瞷筁┮Τ璣ゅ糶ダ
# 硂肈絋﹚key计秖, ノascii絏ㄏノord()皌index array暗
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # hash
        hash = dict()
        cnt = 0
        # 讽才⊿瞷筁ダ, hashcnt+1
        # Τ瞷筁碞ぃ恨
        for i in sentence:
            if i not in hash:
                hash[i] = 1
                cnt += 1
        # 程琌场26ダ
        return cnt==26
        
# @lc code=end

=======
#
# @lc app=leetcode id=1832 lang=python3
#
# [1832] Check if the Sentence Is Pangram
#

# @lc code=start
# By hash, time: O(n), space: O(1), n琌len(sentence)
# 耞sentenceいΤ⊿瞷筁┮Τ璣ゅ糶ダ
# 硂肈絋﹚key计秖, ノascii絏ㄏノord()皌index array暗
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # hash
        hash = dict()
        cnt = 0
        # 讽才⊿瞷筁ダ, hashcnt+1
        # Τ瞷筁碞ぃ恨
        for i in sentence:
            if i not in hash:
                hash[i] = 1
                cnt += 1
        # 程琌场26ダ
        return cnt==26
        
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
