#
# @lc app=leetcode id=2485 lang=python3
#
# [2485] Find the Pivot Integer
#

# @lc code=start
# ��n, ��X�q1~n��, �O�_����res, ��1+...+res==res+...+n

# By math, time: O(1), space:O(1)
# ���D�X1+..+n�`�M, �A�N�����۵��ɪ����󰵥N�ƹB��, ��ڤW�N�O��x*x==m�bx����Ʈɦ���
# �o�D�٥i�H�ΤG���j�M�k, �򥻤W��Υ���ڸѨM������ΤG���j�M�k�ѨM
class Solution:
    def pivotInteger(self, n: int) -> int:
        m = n*(n+1)//2
        x = int(m**0.5)
        if x*x==m:
            return x
        else:
            return -1

# By for loop optimization, time: O(n), space: O(1)
# �̰򥻪��@�k�O�ɤO��, ��Ӱj��
# �o�{���i�H���D1+..+n, �C���u�z�L+-�B��ӨD�X1+..+res�Mres+..+n
# ���ݭn���A�����k�B��res*(res+1)/2�ӨD�X1+..+res�o�ӵ��t�ƦC, �[�k�M��k��ֳt
# class Solution:
#     def pivotInteger(self, n: int) -> int:
#         #1+..+res�i�H�ΨC��+i���覡��s
#         tmp1 = 0
#         # res+...+n�i�H�ΨC��-(i-1)���覡��s
#         tmp2 = n*(n+1)//2
#         for i in range(1, n+1):
#             tmp1 += i
#             tmp2 -= i-1
#             if tmp1==tmp2:
#                 return i
#         return -1
        
# @lc code=end

