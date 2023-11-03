<<<<<<< HEAD
#
# @lc app=leetcode id=1389 lang=python3
#
# [1389] Create Target Array in the Given Order
#

# @lc code=start
# By zip and insert(), time: O(n^2), space: O(1)
# �]insert��ڤW�n�N�᭱�������q�q���Ჾ��, ���a���p�C���u�ֲ���1��, �ҥHO(n^2)
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = list()
        # for i in range(len(nums)):
        #     res.insert(index[i], nums[i])
        # return res
        # ��zip�P�ɨ��Xnums�Mindex, i, j�]�i�g��(i, j)
        # �Ӳz�ӻ�zip���Ŷ�, �n���]�S�������?
        for i, j in zip(nums, index):
            # �Ni���J��index = j���a��
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
# �]insert��ڤW�n�N�᭱�������q�q���Ჾ��, ���a���p�C���u�ֲ���1��, �ҥHO(n^2)
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = list()
        # for i in range(len(nums)):
        #     res.insert(index[i], nums[i])
        # return res
        # ��zip�P�ɨ��Xnums�Mindex, i, j�]�i�g��(i, j)
        # �Ӳz�ӻ�zip���Ŷ�, �n���]�S�������?
        for i, j in zip(nums, index):
            # �Ni���J��index = j���a��
            res.insert(j, i)
        return res

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
