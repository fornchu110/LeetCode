#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start

# By hash, time: O(max(m, n)), space: O(k), k = 26也就是小寫英文字母數量, m = len(ransomNote), n = len(magazine)
# 用hash先走訪magazine將擁有的字母數量儲存起來, 再走訪ransomNote看能否用magazine內的字母做出來
# 注意英文字母類hash可以用bitwise做, 不超過32
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # 當ransomNote比magazine長必定不可能用magazine組合出來
        if len(ransomNote)>len(magazine):
            return False
        hash = {}
        for i in magazine:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1
        for i in ransomNote:
            if i in hash:
                hash[i] -= 1
                if hash[i]<0:
                    return False
            else:
                return False
        return True
        # hash開始這整段可以全用collections.Counter()完成
        # return not collections.Counter(ransomNote) - collections.Counter(magazine)

        
# @lc code=end

