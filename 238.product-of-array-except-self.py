<<<<<<< HEAD
#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start

# By divide array and dynamic programing, time: O(n), space: O(1)
# �n�D�Xnums���ۤv�H�~���������n
# ���o�X�ۤv�Ҧbindex������M�k��Ҧ��������n, �̫�A�ۭ��o�X����
# �Q�Ϊ�����res�s�񥪤譼�n�Ӭ٤U�Ŷ�������
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [0]*length
        # ��0�Ӥ�������S����, �N�䥪�譼�n��l�Ƭ�1        
        res[0] = 1
        # res[i]�񪺬Onums[i]���譼�n
        # ��nums[i]���譼�n���P��nums[i-1]���Wnums[i-1]�����譼�n
        # ���IDP���Q�k, �o�]�O�����٤U�ɶ������ר�O(n)������
        # res[0]�w�g��l�ƩҥH�qres[1]�}�l
        for i in range(1, length):
            res[i] = nums[i-1]*res[i-1]
        # ��l�ƥk�譼�n
        Rpro = 1
        # reverse�O�N�}�C����, range(length)�O�@�ӱq0��length��list
        # �]�N�O���ݶ}�l��
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
# �n�D�Xnums���ۤv�H�~���������n
# ���o�X�ۤv�Ҧbindex������M�k��Ҧ��������n, �̫�A�ۭ��o�X����
# �Q�Ϊ�����res�s�񥪤譼�n�Ӭ٤U�Ŷ�������
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [0]*length
        # ��0�Ӥ�������S����, �N�䥪�譼�n��l�Ƭ�1        
        res[0] = 1
        # res[i]�񪺬Onums[i]���譼�n
        # ��nums[i]���譼�n���P��nums[i-1]���Wnums[i-1]�����譼�n
        # ���IDP���Q�k, �o�]�O�����٤U�ɶ������ר�O(n)������
        # res[0]�w�g��l�ƩҥH�qres[1]�}�l
        for i in range(1, length):
            res[i] = nums[i-1]*res[i-1]
        # ��l�ƥk�譼�n
        Rpro = 1
        # reverse�O�N�}�C����, range(length)�O�@�ӱq0��length��list
        # �]�N�O���ݶ}�l��
        for i in reversed(range(length)):
            res[i] = res[i]*Rpro
            Rpro *= nums[i]
        return res

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
