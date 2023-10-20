#
# @lc app=leetcode id=2220 lang=python3
#
# [2220] Minimum Bit Flips to Convert Number
#

# @lc code=start
# By XOR and bitwise, time: O(log(n)), space: O(1), n�Ostart�Mgoal���j����, log(n)�Y�O���X��ƪ�������
# �n��start�g�L�@�@½��G�i�쪺bit�ഫ��goal, �ݳ̤�½�স��
# �]�N�O���u�n��start�Mgoal�b�G�i��U���Pbit���ƶq�Y�i
# �Q��XOR���ʽ�, 1^1 = 0, 1^0 = 1, �Nstrat�Mgoal��XOR�N���D���Pbit�ƶq
# �A�ӱq�k�@�@�ݭӦ�ƪ�bit�O�_��1, �O1�N���Pbit, res+1
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        res = 0
        tmp = start^goal
        # 0�O�פ���󪺱��p���ΦA�g!=0, while(0)�۵M�|���X
        while tmp:
            # if tmp&1:
            #     res += 1
            # �o�˼g�W�����q��²��
            res += tmp&1
            tmp >>= 1
        return res
                
# @lc code=end

