<<<<<<< HEAD
#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start

# By binary search, time: O(log(n)), space: O(1)
# ㄏノdouble pointer龟, 翴弘琌binary search
# ち琌O(n/2)碞琌O(n), 璶–近常ちO(log(n))
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num
        while left<=right:
            mid = (left+right)//2
            square = mid*mid
            if square==num:
                return True
            elif square<num:
                left = mid+1
            else:
                right = mid-1
        return False

# @lc code=end

=======
#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start

# By binary search, time: O(log(n)), space: O(1)
# ㄏノdouble pointer龟, 翴弘琌binary search
# ち琌O(n/2)碞琌O(n), 璶–近常ちO(log(n))
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num
        while left<=right:
            mid = (left+right)//2
            square = mid*mid
            if square==num:
                return True
            elif square<num:
                left = mid+1
            else:
                right = mid-1
        return False

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
