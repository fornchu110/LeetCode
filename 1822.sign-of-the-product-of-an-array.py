<<<<<<< HEAD
#
# @lc app=leetcode id=1822 lang=python3
#
# [1822] Sign of the Product of an Array
#

# @lc code=start
# ���@�}�Cnums, �Ynums���Ҧ������ۭ�=0 return 0, �ۭ����t return -1, �ۭ����� return 1

# By for loop, time: O(n), space: O(1)
# �������X, �J�줸���O0���Nreturn 0, �Y�t�Ʀ��_�ƭӥN���t, �����ƭӥN����
# ���έp�ƪ���, ���k�O�psign��1, �I��<0���N��-sign, �̫�return sign�Y�O����
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        # �������X�ӭt��
        cnt = 0
        for i in nums:
            if i<0:
                cnt += 1
            elif i==0:
                return 0
        if cnt&1:
            return -1
        else:
            return 1
            
        
# @lc code=end

=======
#
# @lc app=leetcode id=1822 lang=python3
#
# [1822] Sign of the Product of an Array
#

# @lc code=start
# ���@�}�Cnums, �Ynums���Ҧ������ۭ�=0 return 0, �ۭ����t return -1, �ۭ����� return 1

# By for loop, time: O(n), space: O(1)
# �������X, �J�줸���O0���Nreturn 0, �Y�t�Ʀ��_�ƭӥN���t, �����ƭӥN����
# ���έp�ƪ���, ���k�O�psign��1, �I��<0���N��-sign, �̫�return sign�Y�O����
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        # �������X�ӭt��
        cnt = 0
        for i in nums:
            if i<0:
                cnt += 1
            elif i==0:
                return 0
        if cnt&1:
            return -1
        else:
            return 1
            
        
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
