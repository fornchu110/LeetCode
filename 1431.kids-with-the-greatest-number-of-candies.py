<<<<<<< HEAD
#
# @lc app=leetcode id=1431 lang=python3
#
# [1431] Kids With the Greatest Number of Candies
#

# @lc code=start
# By for loop, time: O(n), space: O(1), �]return���e����b�Ŷ�������
# �n��candis��������+�Wextra cadies�ण�ন��candies�����̤j��
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = list()
        max = 0
        # �i�H�ΥH�U�F��
        # max = max(candies)
        for i in candies:
            if i>max:
                max = i
        # �i�H�ΥH�U�F��
        # res = [candy + extraCandies >= max for candy in candies]
        for i in candies:
            if i+extraCandies>=max:
                res.append(True)
            else:
                res.append(False)
        return res
        
# @lc code=end

=======
#
# @lc app=leetcode id=1431 lang=python3
#
# [1431] Kids With the Greatest Number of Candies
#

# @lc code=start
# By for loop, time: O(n), space: O(1), �]return���e����b�Ŷ�������
# �n��candis��������+�Wextra cadies�ण�ন��candies�����̤j��
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = list()
        max = 0
        # �i�H�ΥH�U�F��
        # max = max(candies)
        for i in candies:
            if i>max:
                max = i
        # �i�H�ΥH�U�F��
        # res = [candy + extraCandies >= max for candy in candies]
        for i in candies:
            if i+extraCandies>=max:
                res.append(True)
            else:
                res.append(False)
        return res
        
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
