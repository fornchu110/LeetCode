#
# @lc app=leetcode id=1313 lang=python3
#
# [1313] Decompress Run-Length Encoded List
#

# @lc code=start
# By extend and 2 step range, time: O(n+m), space: O(1), m�Ofreq�`�M
# O(n+m)��+m����]�O�C���n�A���J m��val
# ��extend��Υ�append�ֳt
# �@��@���, index���Ʈɬ�freq, �U�@�ӬOval, �Nval���Jfreq��
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = list()
        # �i�H������range(0, len(nums, 2))�ӥu�bindex�����Ʈɰ���
        # �Ӳz�ӻ�range(0, len(nums), 2)�u�ݤ@�b��n, �����רS�ܦ����Ӥ����
        for i in range(0, len(nums), 2):
            # �άOrange(len(nums)
            # �M���if i&1==0�ӧP�_i�O���Ʈ�, ��i%2==0��
            # �쥻���@�k, �ϥ�append
            # freq = nums[i]
            # val = nums[i+1]
            # for j in range(freq):
            #     res.append(val)
            # �ϥ�extend�bres�᭱�������W�slist, ��append��
            # ��freq��val�ҥH�g��val*freq, �q�`�Q���ƪ�ܻ���, ���ƪ�ܼƶq
            res.extend([nums[i+1]]*nums[i])
        return res

# @lc code=end

