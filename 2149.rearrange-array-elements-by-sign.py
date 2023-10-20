#
# @lc app=leetcode id=2149 lang=python3
#
# [2149] Rearrange Array Elements by Sign
#

# @lc code=start

# ���@�}�Cnums, �n�D�̷Ӥ������t���t���s�Ƨ�, �B��P���ƦӨ��۹��m�������
# �D�ئ������ƩM�t�Ƽƶq�@��, �ҥH���w��len(nums)/2��

# By double pointer, time: O(n), space: O(1)
# �Ψ��pointer�����ثe���ƩM�t�Ƨ�����index
# �C�����䥿��, �u�n�J��t�ƴN���U�ӧ�, ���A�[�Jres, �A�Ӱ��t�ƦP�z
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pos = neg = 0
        res = list()
        for i in range(n//2):
            # �ϥ�while�ϧ�쥿�Ƥ~����
            while nums[pos]<0:
                pos += 1
            res.append(nums[pos])
            pos += 1
            # �ϥ�while�ϧ��t�Ƥ~����
            while nums[neg] > 0:
                neg += 1
            res.append(nums[neg])
            neg += 1
            # �C��������n�[�J�@�ӥ��Ƥ@�ӭt�ƶires, �@n/2��
        return res

# By array, time: O(n), space: O(n)
# ���Xnums�N�̧ǱN���t�Ʀs�ipos�Mneg
# �̫�A���Xlen(nums)/2��, �C���̧ǱNpos�Mneg���ۦPindex��������ires
# class Solution:
#     def rearrangeArray(self, nums: List[int]) -> List[int]:
#         pos = []
#         neg = []
#         res = []
#         for i in nums:
#             if i>0:
#                 pos.append(i)
#             else:
#                 neg.append(i)
#         for i in range(len(nums)//2):
#             res.append(pos[i])
#             res.append(neg[i])
#         return res
        
# @lc code=end

