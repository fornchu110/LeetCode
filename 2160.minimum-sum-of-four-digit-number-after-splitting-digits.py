<<<<<<< HEAD
#
# @lc app=leetcode id=2160 lang=python3
#
# [2160] Minimum Sum of Four Digit Number After Splitting Digits
#

# @lc code=start
# By greedy, time: O(1), space: O(1), ぃsort()ぃ斗糤丁狡馒
# 璶盢倒﹚num–计╊だΘㄢ计, т┮Τ╊だ舱ずㄢ计㎝程ê㎝
# 猔種input琌1000~9999, ┮穦Τ计, 计╊Θㄢㄢ计程(羆㎝程)
# р耕ㄢ计ㄢ计⑻计, 耕ㄢ计ㄢ计计 
class Solution:
    def minimumSum(self, num: int) -> int:
        # 计
        digits = list()
        # 盢input–计秈list
        while num:
            digits.append(num%10)
            num //= 10
        # 竒筁sort獽眔耕㎝耕计琌ㄇ, sort()パ
        digits.sort()
        return 10*(digits[0]+digits[1])+digits[2]+digits[3]

# @lc code=end

=======
#
# @lc app=leetcode id=2160 lang=python3
#
# [2160] Minimum Sum of Four Digit Number After Splitting Digits
#

# @lc code=start
# By greedy, time: O(1), space: O(1), ぃsort()ぃ斗糤丁狡馒
# 璶盢倒﹚num–计╊だΘㄢ计, т┮Τ╊だ舱ずㄢ计㎝程ê㎝
# 猔種input琌1000~9999, ┮穦Τ计, 计╊Θㄢㄢ计程(羆㎝程)
# р耕ㄢ计ㄢ计⑻计, 耕ㄢ计ㄢ计计 
class Solution:
    def minimumSum(self, num: int) -> int:
        # 计
        digits = list()
        # 盢input–计秈list
        while num:
            digits.append(num%10)
            num //= 10
        # 竒筁sort獽眔耕㎝耕计琌ㄇ, sort()パ
        digits.sort()
        return 10*(digits[0]+digits[1])+digits[2]+digits[3]

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
