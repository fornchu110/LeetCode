<<<<<<< HEAD
#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
# ���@���n, return�@���׬�n+1���}�C, ���e��0~n�b�G�i��U1���ƶq
# �ݨ�bitwise���W�n�Q��/2(>>1)���W�ߡB�_�����t���BXOR�B�⪺�S��

# By DP and bitwise, time: O(n), space: O(1)
# �n�Τ@�Ӱ}�Cres���x�sres[i]��1�ƶq, ���`�N�@�}�l�u���@�Ӥ���0
# �ܪ��[�����Di��1�ƶq�䤤�@�سW��:�Yi��2���������, i�u�|���@��1
# Ex: res[1] = res[2] = res[4] = res[8]...
# �A�ӵo�{���u�����O�o�ӳW��
# ��i�O���Ʈ�, res[i]=res[i//2], ��i�O�_�Ʈ�, res[i]=res[i//2]+1
# �]���qi=1�}�l�v�@�إ�res�����e, �C���d��i//2�����G�M���X�_���ɪ������Y�i, ���ݭn�H��i�W�[���B�~�p��
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        for i in range(1, n + 1):
            # ��i>>1�N��i//2
            # ��i&1���Di�O�_���_��, �٥hif-else
            res.append(res[i>>1]+(i&1))
        return res

# By bitwise(n&n-1), time: O(nlogn), space: O(n)
# �q0~n+1���j��, �C����i&i-1���覡�ˬd1���ƶq
# �`�Nn&n-1�]�i�H�ΨӧP�_�O�_��2��������, �]��2��������u���@��1
# �]�N�O��, n&n-1==0�Y�N��n�O2��������
# class Solution:
#     def countBits(self, n: int) -> List[int]:
#         res =  [0]*(n+1)
#         # �o�Oindex���k���j��, �]�i�H��append����k�ְ�index=0����
#         for idx, i in enumerate(range(n+1)):
#             cnt = 0
#             # �O��n�M(n-1)��&�|��̤pbit��1������
#             # �������������۵M�N�ܦ�0, ���X�j��
#             while i!= 0:
#                 i &= i-1
#                 cnt += 1
#             res[idx] = cnt
#             # ����t����k, �@���ݬO�_��1, �M��A�k���ݥ��䨺��
#             # while i!=0:
#             #     if i&1:
#             #         cnt += 1
#             #     i >>= 1
#         return res
        
# @lc code=end

=======
#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
# ���@���n, return�@���׬�n+1���}�C, ���e��0~n�b�G�i��U1���ƶq
# �ݨ�bitwise���W�n�Q��/2(>>1)���W�ߡB�_�����t���BXOR�B�⪺�S��

# By DP and bitwise, time: O(n), space: O(1)
# �n�Τ@�Ӱ}�Cres���x�sres[i]��1�ƶq, ���`�N�@�}�l�u���@�Ӥ���0
# �ܪ��[�����Di��1�ƶq�䤤�@�سW��:�Yi��2���������, i�u�|���@��1
# Ex: res[1] = res[2] = res[4] = res[8]...
# �A�ӵo�{���u�����O�o�ӳW��
# ��i�O���Ʈ�, res[i]=res[i//2], ��i�O�_�Ʈ�, res[i]=res[i//2]+1
# �]���qi=1�}�l�v�@�إ�res�����e, �C���d��i//2�����G�M���X�_���ɪ������Y�i, ���ݭn�H��i�W�[���B�~�p��
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        for i in range(1, n + 1):
            # ��i>>1�N��i//2
            # ��i&1���Di�O�_���_��, �٥hif-else
            res.append(res[i>>1]+(i&1))
        return res

# By bitwise(n&n-1), time: O(nlogn), space: O(n)
# �q0~n+1���j��, �C����i&i-1���覡�ˬd1���ƶq
# �`�Nn&n-1�]�i�H�ΨӧP�_�O�_��2��������, �]��2��������u���@��1
# �]�N�O��, n&n-1==0�Y�N��n�O2��������
# class Solution:
#     def countBits(self, n: int) -> List[int]:
#         res =  [0]*(n+1)
#         # �o�Oindex���k���j��, �]�i�H��append����k�ְ�index=0����
#         for idx, i in enumerate(range(n+1)):
#             cnt = 0
#             # �O��n�M(n-1)��&�|��̤pbit��1������
#             # �������������۵M�N�ܦ�0, ���X�j��
#             while i!= 0:
#                 i &= i-1
#                 cnt += 1
#             res[idx] = cnt
#             # ����t����k, �@���ݬO�_��1, �M��A�k���ݥ��䨺��
#             # while i!=0:
#             #     if i&1:
#             #         cnt += 1
#             #     i >>= 1
#         return res
        
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
