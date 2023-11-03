<<<<<<< HEAD
#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
# ���@��nums�ƦC, return�̱`���W�l�ƦC������
# ���W�l�ƦC���άO�s�򪺤���, �u�n���ǨS���ܧY�i

# By DP, time: O(n^2), space: O(n), n = len(nums)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # ��nums���ŮɥN��S���ƦC, �]������return 0
        if not nums:
            return 0
        # dp[i]�N���"�]�t�Fnums[i]"���ei�Ӥ����ɳ̨θ�, �]�N�O�ݥ]�tnums[i]���ei��nums�������̪��l�ƦC����
        # �e0�Ӥ������ΰQ��, �ҥH�Q�׫e1�Ӥ���...�en�Ӥ����@len(nums)��
        dp = [1]*len(nums)
        # ���Qdp[i]�ɪ��̨θ�
        for i in range(len(nums)):
            # �ei�Ӥ����N���0�Ӥ������i-1�Ӥ����@i��
            for j in range(i):
                # �u��nums[i]��nums[j]�٤j�����p, �~��qdp[j]+1�ಾ�L��
                # Ex: ���]dp[3]�]�N�O�e�T�Ӥ����̪��O2, dp[4]�]�N�O�e�|�Ӥ����̪��O3
                # �o�ɧڱ��Qdp[5], �o�{nums[5]>nums[3], �]�N�N��dp[5]�i�H�O2+1 = 3
                # �o�ɦA�~�򱴰Qdp[5], �o�{nums[5]<nums[4], �N�N��dp[5]���i�H�O3+1 = 4, �̦h�N��3�F 
                # ex: nums = [0, 2, 1, 5, 4], �̪��N�O[0, 2, 5]�������׬�3���l�ƦC
                if nums[i]>nums[j]:
                    # ���e��dp[i]�q��Ө�?���u�O��l�ƪ�1
                    # ���]�ثej = 3, ��dp[i]�]�i��bj = 0, 1, 2, 3�ɧ�s�L
                    # �]���ݭn�Dmax
                    # Ex : ���]i = 7�Bdp[4] = 2, ����o�N��nums[7]>nums[3](dp[4]�O�]�tnums[3]�e4�Ӯɪ���)
                    # �ҥHdp[7]�i�H�O3, ���Y�e�|�ӼƬO[1, 4, 5, 2], ����dp[3] = 3
                    # �ҥH��ڤWdp[7]���Ӧbj = 2�ɴN��s��4�F, ���Ʊ��ܦ���p��3 
                    # �]�N�O����o����nums[j]�񤧫e��nums[j]�٤p�ɷ|�o��dp[j]+1��dp[i]�٤p�����p
                    dp[i] = max(dp[i], dp[j]+1)
        # ������Omax(dp)?
        # �]��dp[i]�����]�tnums[i], �ҥH�Ynums[i]���O�̤j���N���i��|�O�̨θ�, �P�e���b��nums[j]�P�z
        return max(dp)
        
# @lc code=end

=======
#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
# ���@��nums�ƦC, return�̱`���W�l�ƦC������
# ���W�l�ƦC���άO�s�򪺤���, �u�n���ǨS���ܧY�i

# By DP, time: O(n^2), space: O(n), n = len(nums)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # ��nums���ŮɥN��S���ƦC, �]������return 0
        if not nums:
            return 0
        # dp[i]�N���"�]�t�Fnums[i]"���ei�Ӥ����ɳ̨θ�, �]�N�O�ݥ]�tnums[i]���ei��nums�������̪��l�ƦC����
        # �e0�Ӥ������ΰQ��, �ҥH�Q�׫e1�Ӥ���...�en�Ӥ����@len(nums)��
        dp = [1]*len(nums)
        # ���Qdp[i]�ɪ��̨θ�
        for i in range(len(nums)):
            # �ei�Ӥ����N���0�Ӥ������i-1�Ӥ����@i��
            for j in range(i):
                # �u��nums[i]��nums[j]�٤j�����p, �~��qdp[j]+1�ಾ�L��
                # Ex: ���]dp[3]�]�N�O�e�T�Ӥ����̪��O2, dp[4]�]�N�O�e�|�Ӥ����̪��O3
                # �o�ɧڱ��Qdp[5], �o�{nums[5]>nums[3], �]�N�N��dp[5]�i�H�O2+1 = 3
                # �o�ɦA�~�򱴰Qdp[5], �o�{nums[5]<nums[4], �N�N��dp[5]���i�H�O3+1 = 4, �̦h�N��3�F 
                # ex: nums = [0, 2, 1, 5, 4], �̪��N�O[0, 2, 5]�������׬�3���l�ƦC
                if nums[i]>nums[j]:
                    # ���e��dp[i]�q��Ө�?���u�O��l�ƪ�1
                    # ���]�ثej = 3, ��dp[i]�]�i��bj = 0, 1, 2, 3�ɧ�s�L
                    # �]���ݭn�Dmax
                    # Ex : ���]i = 7�Bdp[4] = 2, ����o�N��nums[7]>nums[3](dp[4]�O�]�tnums[3]�e4�Ӯɪ���)
                    # �ҥHdp[7]�i�H�O3, ���Y�e�|�ӼƬO[1, 4, 5, 2], ����dp[3] = 3
                    # �ҥH��ڤWdp[7]���Ӧbj = 2�ɴN��s��4�F, ���Ʊ��ܦ���p��3 
                    # �]�N�O����o����nums[j]�񤧫e��nums[j]�٤p�ɷ|�o��dp[j]+1��dp[i]�٤p�����p
                    dp[i] = max(dp[i], dp[j]+1)
        # ������Omax(dp)?
        # �]��dp[i]�����]�tnums[i], �ҥH�Ynums[i]���O�̤j���N���i��|�O�̨θ�, �P�e���b��nums[j]�P�z
        return max(dp)
        
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
