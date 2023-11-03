<<<<<<< HEAD
#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
# ���@�}�Cnums, return�b�}�C�����W�L�@�b�ƶq������
# �o�˪������S�Q�٬�����(mode)
# "�W�L�@�b"�N��Y��n�Ӥ���, ���X�{���Ʀܤ�>n/2
# �D�ذ��]���w�s�b�o�˪�������}�C��

# By sort, time: O(nlogn), space: O(logn)
# �]���w�s�b�o�˪�����, �i�H�[���W�L�@�b�������b�Ƨǫᥲ�w�|�b����
# �ҥH�Ƨǫ�return�Y�i
# �o�D�]�i�H��hash�Mdivide and conquer��
# Boyer-Moore��k�i�H����time: O(n), space: O(1), �H���s
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # ���ت�sort()�t�׫ܧ�
        nums.sort()
        # �`�N�O"�W�L�@�b", �ҥH�O�n���W����
        # Ex: [1, 1, 1, 2], 4�Ӥ����ܤ֦�3�Ӥ~��W�L�@�b
        # �Y(len(nums)-1)//2�|�b���ƭӤ����ɩ��U����
        # ���W����N�O(len(nums)-1+2-1)//2 = len(nums)//2
        return nums[len(nums)//2]
        
# @lc code=end

=======
#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
# ���@�}�Cnums, return�b�}�C�����W�L�@�b�ƶq������
# �o�˪������S�Q�٬�����(mode)
# "�W�L�@�b"�N��Y��n�Ӥ���, ���X�{���Ʀܤ�>n/2
# �D�ذ��]���w�s�b�o�˪�������}�C��

# By sort, time: O(nlogn), space: O(logn)
# �]���w�s�b�o�˪�����, �i�H�[���W�L�@�b�������b�Ƨǫᥲ�w�|�b����
# �ҥH�Ƨǫ�return�Y�i
# �o�D�]�i�H��hash�Mdivide and conquer��
# Boyer-Moore��k�i�H����time: O(n), space: O(1), �H���s
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # ���ت�sort()�t�׫ܧ�
        nums.sort()
        # �`�N�O"�W�L�@�b", �ҥH�O�n���W����
        # Ex: [1, 1, 1, 2], 4�Ӥ����ܤ֦�3�Ӥ~��W�L�@�b
        # �Y(len(nums)-1)//2�|�b���ƭӤ����ɩ��U����
        # ���W����N�O(len(nums)-1+2-1)//2 = len(nums)//2
        return nums[len(nums)//2]
        
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
