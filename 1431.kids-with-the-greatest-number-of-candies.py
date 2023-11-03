<<<<<<< HEAD
#
# @lc app=leetcode id=1431 lang=python3
#
# [1431] Kids With the Greatest Number of Candies
#

# @lc code=start
# By for loop, time: O(n), space: O(1), 因return內容不算在空間複雜度
# 要看candis內的元素+上extra cadies能不能成為candies中的最大值
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = list()
        max = 0
        # 可以用以下達成
        # max = max(candies)
        for i in candies:
            if i>max:
                max = i
        # 可以用以下達成
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
# By for loop, time: O(n), space: O(1), 因return內容不算在空間複雜度
# 要看candis內的元素+上extra cadies能不能成為candies中的最大值
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = list()
        max = 0
        # 可以用以下達成
        # max = max(candies)
        for i in candies:
            if i>max:
                max = i
        # 可以用以下達成
        # res = [candy + extraCandies >= max for candy in candies]
        for i in candies:
            if i+extraCandies>=max:
                res.append(True)
            else:
                res.append(False)
        return res
        
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
