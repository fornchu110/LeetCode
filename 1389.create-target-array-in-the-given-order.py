<<<<<<< HEAD
#
# @lc app=leetcode id=1389 lang=python3
#
# [1389] Create Target Array in the Given Order
#

# @lc code=start
# By zip and insert(), time: O(n^2), space: O(1)
# 因insert實際上要將後面的元素通通往後移動, 最壞情況每次只少移動1個, 所以O(n^2)
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = list()
        # for i in range(len(nums)):
        #     res.insert(index[i], nums[i])
        # return res
        # 用zip同時走訪nums和index, i, j也可寫為(i, j)
        # 照理來說zip更花空間, 好像也沒有比較快?
        for i, j in zip(nums, index):
            # 將i插入到index = j的地方
            res.insert(j, i)
        return res

# @lc code=end

=======
#
# @lc app=leetcode id=1389 lang=python3
#
# [1389] Create Target Array in the Given Order
#

# @lc code=start
# By zip and insert(), time: O(n^2), space: O(1)
# 因insert實際上要將後面的元素通通往後移動, 最壞情況每次只少移動1個, 所以O(n^2)
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = list()
        # for i in range(len(nums)):
        #     res.insert(index[i], nums[i])
        # return res
        # 用zip同時走訪nums和index, i, j也可寫為(i, j)
        # 照理來說zip更花空間, 好像也沒有比較快?
        for i, j in zip(nums, index):
            # 將i插入到index = j的地方
            res.insert(j, i)
        return res

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
