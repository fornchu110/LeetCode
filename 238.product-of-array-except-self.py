<<<<<<< HEAD
#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start

# By divide array and dynamic programing, time: O(n), space: O(1)
# 要求出nums中自己以外的元素乘積
# 先得出自己所在index之左方和右方所有元素乘積, 最後再相乘得出答案
# 利用直接由res存放左方乘積來省下空間複雜度
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [0]*length
        # 第0個元素左邊沒元素, 將其左方乘積初始化為1        
        res[0] = 1
        # res[i]放的是nums[i]左方乘積
        # 而nums[i]左方乘積等同於nums[i-1]乘上nums[i-1]的左方乘積
        # 有點DP的想法, 這也是為何能省下時間複雜度到O(n)的關鍵
        # res[0]已經初始化所以從res[1]開始
        for i in range(1, length):
            res[i] = nums[i-1]*res[i-1]
        # 初始化右方乘積
        Rpro = 1
        # reverse是將陣列反轉, range(length)是一個從0到length的list
        # 也就是尾端開始看
        for i in reversed(range(length)):
            res[i] = res[i]*Rpro
            Rpro *= nums[i]
        return res

# @lc code=end

=======
#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start

# By divide array and dynamic programing, time: O(n), space: O(1)
# 要求出nums中自己以外的元素乘積
# 先得出自己所在index之左方和右方所有元素乘積, 最後再相乘得出答案
# 利用直接由res存放左方乘積來省下空間複雜度
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [0]*length
        # 第0個元素左邊沒元素, 將其左方乘積初始化為1        
        res[0] = 1
        # res[i]放的是nums[i]左方乘積
        # 而nums[i]左方乘積等同於nums[i-1]乘上nums[i-1]的左方乘積
        # 有點DP的想法, 這也是為何能省下時間複雜度到O(n)的關鍵
        # res[0]已經初始化所以從res[1]開始
        for i in range(1, length):
            res[i] = nums[i-1]*res[i-1]
        # 初始化右方乘積
        Rpro = 1
        # reverse是將陣列反轉, range(length)是一個從0到length的list
        # 也就是尾端開始看
        for i in reversed(range(length)):
            res[i] = res[i]*Rpro
            Rpro *= nums[i]
        return res

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
