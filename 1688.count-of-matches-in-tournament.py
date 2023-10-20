#
# @lc app=leetcode id=1688 lang=python3
#
# [1688] Count of Matches in Tournament
#

# @lc code=start
# By simulation, time: O(log(n)), space: O(1)
# ��X�Q�^�O�������, �ӵ��D�ص������j��
class Solution:
    def numberOfMatches(self, n: int) -> int:
        res = 0
        while(n!=1):
            # ��n&1�P�_n�O�_���_��
            if n&1:
                # ��>>1�N��//2
                res += (n-1)>>1
                # �`�N>>�B�⪺�u���v��+=*/�C�ҥH�n�A��
                n = n-((n-1)>>1)
            else:
                res += n>>1
                n = n-(n>>1)
        return res

# By math, time: O(1), space: O(1)
# ��ڤW�u�|���@�H���, �ҥHn�H���ɴN��n-1�H�Q�^�O
# class Solution:
#     def numberOfMatches(self, n: int) -> int:
#         return n-1

# @lc code=end

