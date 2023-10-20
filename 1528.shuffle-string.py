#
# @lc app=leetcode id=1528 lang=python3
#
# [1528] Shuffle String
#

# @lc code=start
# By zip and join(), time: O(n), space: O(1)
# ���@��str�H��indices�N��str���U�r�����ө�m�쪺index
# �Q��zip(s, indices)�N�i�P��Ū��U�Ӧr�Ÿө�b����index, �x�s�ires�o��list
# �]�ݭnreturn�r��, �ҥH��"".join(res)�o�ӧޥ��Nres�qlist�ഫ���r��
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [0]*len(s)
        # ��zip�P�ɨ��Xs�Mindices
        for i, idx in zip(s, indices):
            res[idx] = i
        # "".join(res)�O���Nres�o��list����������""�]�N�O�L�r�Ũӳs�����s�r��
        return "".join(res)

# @lc code=end

