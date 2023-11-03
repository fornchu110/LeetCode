<<<<<<< HEAD
#
# @lc app=leetcode id=2348 lang=python3
#
# [2348] Number of Zero-Filled Subarrays
#

# @lc code=start
# ���@�}�Cnums, return�̭��U�سs�����0���l�}�C�ƥ�

# By DP, time: O(n), space: O(1)
# �l�}�C�ƥحn�O�o�o��
# Ex: [0]�u��1�Ӥl�}�C, [0, 0]��3�Ӥl�}�C, [0, 0, 0]��6�Ӥl�}�C
# �ҥH�|�o�{, 1 = 0+1, 3 = 1+2, 6 = 3+3, �C���o�{�s��0�N+0���ƶq�N�O�s�W�[���l�}�C�ƥ�
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = cnt = 0
        for i in nums:
            if i:
                cnt = 0
            else:
                cnt += 1
                res += cnt
        return res

# @lc code=end

=======
#
# @lc app=leetcode id=2348 lang=python3
#
# [2348] Number of Zero-Filled Subarrays
#

# @lc code=start
# ���@�}�Cnums, return�̭��U�سs�����0���l�}�C�ƥ�

# By DP, time: O(n), space: O(1)
# �l�}�C�ƥحn�O�o�o��
# Ex: [0]�u��1�Ӥl�}�C, [0, 0]��3�Ӥl�}�C, [0, 0, 0]��6�Ӥl�}�C
# �ҥH�|�o�{, 1 = 0+1, 3 = 1+2, 6 = 3+3, �C���o�{�s��0�N+0���ƶq�N�O�s�W�[���l�}�C�ƥ�
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = cnt = 0
        for i in nums:
            if i:
                cnt = 0
            else:
                cnt += 1
                res += cnt
        return res

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
