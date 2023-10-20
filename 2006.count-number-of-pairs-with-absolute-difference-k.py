#
# @lc app=leetcode id=2006 lang=python3
#
# [2006] Count Number of Pairs With Absolute Difference K
#

# @lc code=start
# �^�ǰ}�Cnums���bindex i<j�����p�U|nums[i]-nums[j]|==k��pairs�ƶq

# By hash table, time: O(n), space: O(n)
# �Q��hash�N���X�쪺�Ʀr�s�U��, �åB�O���ثe�o�ӼƦr���X��F�X��
# �C���X��s�Ʀr, �N�h�d�s�Ʀr-k�M�s�Ʀr+k���h�֥[�W��, �N��e���ŦX|nums[i]-nums[j]|==k���ƥ�
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        hash = {}
        res = 0
        # �C�����X�쪺�s�Ʀr��ڤW��@nums[j]�b��, ���X�L�w�g�bhash�W���Onums[i]
        for i in nums:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1
            # �P�_�O�_�ŦX|nums[i]-nums[j]|==k������
            # �nif in hash�~�i�H, �����S��l��hash�i��|�䤣��key
            if i-k in hash:
                res += hash[i-k]
            if i+k in hash:
                res += hash[i+k]
        return res
        
# By double for loop, time: O(n^2), space: O(1)
# # �������j�騫�X
# class Solution:
#     def countKDifference(self, nums: List[int], k: int) -> int:
#         res = 0
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if abs(nums[i]-nums[j])==k:
#                     res += 1
#         return res
    
# @lc code=end

