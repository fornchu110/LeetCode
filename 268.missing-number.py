#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number

# @lc code=start
# ���d��0~n, ���@�}�Cnums, nums���׷|�On�B������unique, ��X0~n��(n+1�Ӥ���)�ʤ֪����@����

# By bitwise(XOR), time: O(n), space: O(1)
# nums��n�Ӥ���, �Y�bnums��K�[0~n�on+1�Ӥ���, �o���`�@�N��2n+1�Ӥ���
# �o2n+1�Ӥ�����, �u���ʤ֪����@�����X�{�@��, ��L�S�ʤ֪��������X�{�F�⦸
# �ҥH�o2n+1�Ӥ��������@�_��XOR, �̫�N�|�O�ʥ������@����, �]�S�ʥ���XOR��=0, ��0�M�ʥ���XOR�Y�O�ʥ���
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0
        # ��2n�Ӥ�����XOR, �䤤i�n�N���O��ӲK�[��0~n�on+1��
        for i, num in enumerate(nums):
            xor ^= i^num
        # ���]nums�u��n��, �W��i�u�N��0~n-1
        # �ٯʤ֤@�ӫ�ӼW�[������, �Y�On, �]�N�Olen(nums)
        # �o�˴N�N2n+1�Ӥ��������۰�XOR�o�X���G
        return xor^len(nums)

# By hash, time: O(n), space: O(n)
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         # �]nums����������, �Bset()�i�H��in��@hash�d��, �ҥH��set(nums)�إ�hash
#         hash = set(nums)
#         # �]nums���w�w�g�ʤ֤@��, �ҥH��len(nums)+1��index, �]�N�O�q0���len(nums)
#         for i in range(len(nums)+1):
#             # ���bhash����index�N�N��ʥ��F
#             if i not in hash:
#                 return i

# By sort and index, time: O(nlogn), space: O(logn)
# space = O(logn)����]�O.sort()�brecursive�ɥe�Ϊ�stack�Ŷ�
# ���Nnums�ƧǹL��, ����O�_�Mindex�ۦP, ���P�N�N��֤Findex, ����᳣̫�ۦP�N�N��֤Findex+1
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         nums.sort()
#         res = 0
#         for i in nums:
#             if i!= res:
#                 return res
#             res += 1
#         # ��o�{�q�Y���X������Mindex�ۦP, �N����Oindex+1�o�Ӥ����ʥ��F
#         # Ex: nums = [0,1], �ӵ��״N�O2
#         return res
        
# @lc code=end

