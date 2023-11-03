<<<<<<< HEAD
#
# @lc app=leetcode id=1662 lang=python3
#
# [1662] Check If Two String Arrays are Equivalent
#

# @lc code=start
# By "".join(), time: O(n), space: O(1)
# 判斷給定兩list轉換成string後是否相等, 用"".join()即可達成list轉string
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1)=="".join(word2)
# @lc code=end

=======
#
# @lc app=leetcode id=1662 lang=python3
#
# [1662] Check If Two String Arrays are Equivalent
#

# @lc code=start
# By "".join(), time: O(n), space: O(1)
# 判斷給定兩list轉換成string後是否相等, 用"".join()即可達成list轉string
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1)=="".join(word2)
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
