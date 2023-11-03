#
# @lc app=leetcode id=1470 lang=python3
#
# [1470] Shuffle the Array
#

# @lc code=start

# By double pointer, time: O(n), space: O(1)
# �Hres����Ŷ������ת��[�I�OO(1), ���Mres�������OO(n)
# ���pointer, �@�}�l���V0�M���Vn, ��pointer���t�Zn�Ӥ���
# �o�˰�n���̧ǥ[�J�Y�i
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = list()
        odd = 0
        even = n
        while(n!=0):
            res.append(nums[odd])
            res.append(nums[even])
            odd += 1
            even += 1
            n -= 1
        return res

# By range, time: O(n), space: O(1)
# ���ܼƪŶ����@�k, ���Ψ�range�ɶ����[
# class Solution:
#     def shuffle(self, nums: List[int], n: int) -> List[int]:
#         res = list()
#         for i in range(n):
#             res.append(nums[i])
#             res.append(nums[i+n])
#         return res
        
# @lc code=end

