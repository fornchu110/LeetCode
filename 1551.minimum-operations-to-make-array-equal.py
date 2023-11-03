#
# @lc app=leetcode id=1551 lang=python3
#
# [1551] Minimum Operations to Make Array Equal
#

# @lc code=start
# ��n, n���@���t�}�C1, 3, 5, ...�������ƶq
# �w�q�@���ާ@�N�@�Ӥ���-1�@�Ӥ���+1
# return �g�L�̤֦��ާ@�����}�C���������۵�

# By greedy, time: O(n), space: O(n), ���N�}�C�����X�Ӫ��ܬOspace: O(1)
# �D�X�����ȫ�, �ݤ񥭧��Ȥp���ƻP�����Ȫ��t���`�M�Y�O����
# ��ꥭ���ȴN�O�쥻����n, �ҥH��2*i+1�Pn���t�ȧY�i, �ݭn�j���٤p��
class Solution:
    def minOperations(self, n: int) -> int:
        res = 0
        # �����X�}�C�����k
        # arr = []
        # for i in range(n):
        #     arr.append(2*i+1)
        # average = arr[0]+arr[len(arr)-1]//2
        # for i in range(len(arr)//2):
        #     res += average-arr[i]
        # return res
        # ���μ����}�C�����k, space: O(1)
        for i in range(n):
            if (2*i+1)<n:
                res += n-(2*i+1)
        return res
        # �@�檩
        # return sum(x - n for i in range(n) if (x := 2 * i + 1) > n)

# By math, time: O(1), space: O(1)
# �g�L�ƾǱ��ɥi�����׻Pn�����Y
# class Solution:
#     def minOperations(self, n: int) -> int:
#         # �O�o�[������u���v��첾��
#         return n*n>>2

# @lc code=end

