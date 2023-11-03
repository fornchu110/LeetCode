#
# @lc app=leetcode id=2418 lang=python3
#
# [2418] Sort the People
#

# @lc code=start
# By zip and �C��ͦ���, time: O(n), space: O(1)
# �n�Dreturn�Ө����Ѱ���C�Ƨǫ᪺�����H�W
# ��zip()�N�����M�W�r�@�@���X, �u�[�J�H�W
# zip�᪺list�]�i�H�Ƨ�
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        tmp = sorted(zip(heights, names), reverse = True)
        # res = [*zip(*tmp)][1]
        res = [name for height, name in tmp]
        return res
        
# By zip , time: O(n), space: O(1)
# class Solution:
#     def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
#         res = []
#         tmp = list(zip(heights, names))
#         # �Nzip�᪺list�Ƨ�, �]��sorted()�O�q�p��j�Ƨ�, reverse = True�Ѽ��ܱq�j��p�Ƨ�
#         tmp  = sorted(tmp, reverse = True)
#         # ��ƧǹL�᪺name
#         for height, name in tmp:
#             res.append(name)
#         return res

# @lc code=end

