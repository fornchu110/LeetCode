#
# @lc app=leetcode id=2439 lang=python3
#
# [2439] Minimize Maximum of Array
#

# @lc code=start
# ���@�}�Cnums, �i�H��nums[i]-1�P��nums[i-1]+1���ާ@, �Q��k��max(nums)�̤ܳp��return�o�ӭ�

# By, category discussion, time: O(n), space: O(1)
# �����Q�תk, ���I��dp������, ���k�S���I��prefix
# �Q�γo�D���ާ@��ڤW�O�Nnums�������ɥi�઺�����Ƴo�I, �u�n�᭱���������j�N��@��������
# �[���o�{�ƻ�s�����j?��ڤW�N�O��e���Ҧ��������������٤j
# �@�}�l�u���@�Ӥ�����, �̤j�ȴN�O�@�Ӥ���
# �C����s������, �p�G�s������W����X���̤j���٤j, �N��i�H������(�]�᭱���i�H�����e��)
# ���s������������[�`�å�����, �N�O�s���̤j��
# �p�G�s�����񤧫e��X���̤j���٤p, �N��̤j�Ȥ���
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res = []
        # enumerate�_�l�Ȭ�1, �O���F���D�ثe���X�Ӥ���, accululate�O�C����s�����������M
        # Ex, nums = [1, 2, 3, 4], accumulate(nums) = [1, 3, 6, 10]
        for num, i in enumerate(accumulate(nums), 1):
            # �ѩ�W�w�������Oint, �ҥH�h�l�������Ȥ���˱�
            # �����ȬO3.5��max�N�n�O4, �]�������V�W����
            # +(num-1)�O�V�W���㪺�ޥ�, ���k�O�[�W������-1, -1�O���F�קK�㰣
            # Ex: 12//5�V�W���� = (12+5)//5 = 3
            # ��15//5�ڭ̤@�˧Ʊ�O�V�W�����, (15+5)//5 = 4, ���ŦX15//5�V�W���� = 3�����G
            # �ҥH(15+5-1)//5 = (15+4)//5�קK�F�h�[1, �B���|�藍�㰣�����p�v�T
            # �����O1�ɥ��ӴN�S���V�W����V�U���㪺���D, �ҥH+1�A-1�S�t
            res.append((i+(num-1))//num)
        # �]���o�̪��@�k�O�L�צp���X��U�Ҧ�����������, �ҥH�n��max
        return max(res)
        # �C��ͦ����g�k, �|��append��֤@�I
        return max((i+(num-1))//num for num, i in enumerate(accumulate(nums), 1))
    
# By binary solution, time: O(nlogm), space: O(1), m = max(nums)
# �G�����תk
# �`�Nmin(max)�Mmax(min), �]�N�O�̤p�Ƴ̤j�ȩγ̤j�Ƴ̤p�Ȫ����D, ���i�H�ΤG�����תk�Ӱ�
# ���M�@���u��P�ɾާ@nums[i]�Mnums[i-1], ���`�N�o�ä��N��u��nums[i]���Ư൹nums[i-1]
# Ex: [7, 8, 8, 9], �]���èS���w�ާ@����, �ҥH�u�n�N9��1�@�����e���ܦ�[8, 8, 8, 8]�Y�i
# �Q�ΤG���d���Y�p�smax(nums)�]�N�Ores���϶�
# Ex: [2, 3, 7], �o�Ӱ}�C�̫��ܦ�[4, 4, 4], ��ڤW�O�N7��2��1����2�M1��1����3�ܦ���
# �i�H�[���򥻤W�O�b�ŦX����U�Nnums��[������
# class Solution:   
#     def minimizeArrayValue(self, nums: List[int]) -> int:
#         # check�ت��O��res��max��, �˴��O�_�i��, �����T�{���L�{
#         # Ex: ���}�C[3, 5], �Yres��4, ������3�ɷ|�ѤU1��coda���᭱��4�j�����ܤp
#         # ���}�C[5, 3], �Yres��4, �|�o�{�]���e�����൹�᭱, �ҥH4�������i��, �|return False
#         def check(nums, res):
#             # �����@�}�l�O0, �]�u���J���res��p���Ƥ~���l�O�N�᭱�����ܤp
#             coda = 0
#             # �q�Y���X�T�{�s��res��_����
#             for i in nums:
#                 if i<=res:
#                     coda += res-i
#                 else:
#                     if coda<i-res:
#                         return False
#                     else:
#                         coda -= (i-res)
#             return True
        
#         # �`�N�ϥΤG���d��ä��O���F���X�}�C, �ҥHleft�Mright�ä��Oindex
#         # left�Mmax�N���O�sres�Ҧb���϶�, �����N��sres�u�Ѥ@�إi��, �]�N�O�̨θ�
#         # �����O�ҳ̨�?�]���o��ڤW�O�bres���ŦX����ɤ~�W�[res, res�ŦX����ɺɶq���res
#         left = 0
#         right = max(nums)
#         # �smax(nums)���w�b[0, max(nums)]�϶�, �Q�ΤG���d���X�smax(nums)�󦳮Ĳv
#         # �G���d�䪺�L�{�N�O�ܧ�res�ô��ժ��L�{, �G�����ت��b��qmax(nums)//2�}�l��OO(logn)
#         # ��q0���W�αqmax(nums)���U�}�l�䪺O(n)��n
#         while left<right:
#             # mid��ڤW�N�O�������]���smax(nums), �]�N�Ores
#             mid = (right-left)//2+left
#             # check��True�N��H�ثemid�@��res�i��, ���U����mid��p�ո�
#             if check(nums, mid):
#                 right = mid
#             # check��False�N��ثemid�@��res���i��, �]�N�O�Ӥp, ���U����mid��j
#             else:
#                 left = mid+1
#         # ��G���d�䵲���N���X�F�i�檺�̤pmax(nums)
#         return left
    
# �W���o�ӤG������, python�వ���u�g�k
# class Solution:
#     def minimizeArrayValue(self, nums: List[int]) -> int:
#         def check(limit: int) -> bool:
#             extra = 0
#             for i in range(len(nums) - 1, 0, -1):
#                 extra = max(nums[i] + extra - limit, 0)
#             return nums[0] + extra <= limit
#         return bisect_left(range(max(nums)), True, key=check)

# @lc code=end

