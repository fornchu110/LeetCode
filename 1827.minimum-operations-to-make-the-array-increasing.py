<<<<<<< HEAD
#
# @lc app=leetcode id=1827 lang=python3
#
# [1827] Minimum Operations to Make the Array Increasing
#

# @lc code=start
# ���@�}�Cnums, ��X�̤֦��露��+1�ϱo�̭������O�Y�滼�W(strictly increasing)��

# By simulation, time: O(n), space: O(1)
# �n�Y�滼�W, �ҥH�u�n�᭱��<=�e����, �N�n�ɤW�t��+1, �]�N�O�A���t��+1��
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # ���వ�Ƨ�
        res = 0
        # ���ݭn��while�j��, �|�W��
        for i in range(1, len(nums)):
            if nums[i]<=nums[i-1]:
                # �`�N�n����s���G�A��snums����, ���M�N�O�s�_��
                # �_�h���G�|�Ψ��s�L��nums����
                res += nums[i-1]-nums[i]+1
                nums[i] += nums[i-1]-nums[i]+1
        return res
    
# @lc code=end

=======
#
# @lc app=leetcode id=1827 lang=python3
#
# [1827] Minimum Operations to Make the Array Increasing
#

# @lc code=start
# ���@�}�Cnums, ��X�̤֦��露��+1�ϱo�̭������O�Y�滼�W(strictly increasing)��

# By simulation, time: O(n), space: O(1)
# �n�Y�滼�W, �ҥH�u�n�᭱��<=�e����, �N�n�ɤW�t��+1, �]�N�O�A���t��+1��
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # ���వ�Ƨ�
        res = 0
        # ���ݭn��while�j��, �|�W��
        for i in range(1, len(nums)):
            if nums[i]<=nums[i-1]:
                # �`�N�n����s���G�A��snums����, ���M�N�O�s�_��
                # �_�h���G�|�Ψ��s�L��nums����
                res += nums[i-1]-nums[i]+1
                nums[i] += nums[i-1]-nums[i]+1
        return res
    
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
