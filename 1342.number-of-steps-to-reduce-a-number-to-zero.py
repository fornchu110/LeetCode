<<<<<<< HEAD
#
# @lc app=leetcode id=1342 lang=python3
#
# [1342] Number of Steps to Reduce a Number to Zero
#

# @lc code=start

# By & and >>, time: O(log(num)), space: O(1)
# time: O(log(num))����]�O�C���B�ⳣ�|�Nnum��b, �۷��H2������log
# ��num, ��Xnum�g�L�X���B���~�|�ܦ�0
# �W�h�O��num�����Ʈɪ������H2, ���Y�O�_�Ʈ�-1
class Solution:
    def numberOfSteps(self, num: int) -> int:
        res = 0
        while(num!=0):
            # ��num&1�D0, �N��num�O�_��
            if num&1:
                num -= 1
            # num�O����
            else:
                # ��2���P��k���@�줸, �`�N�p�G��num/=2, num�|��float�ӫDint
                num >>= 1
            res += 1
        return res
        
# @lc code=end

=======
#
# @lc app=leetcode id=1342 lang=python3
#
# [1342] Number of Steps to Reduce a Number to Zero
#

# @lc code=start

# By & and >>, time: O(log(num)), space: O(1)
# time: O(log(num))����]�O�C���B�ⳣ�|�Nnum��b, �۷��H2������log
# ��num, ��Xnum�g�L�X���B���~�|�ܦ�0
# �W�h�O��num�����Ʈɪ������H2, ���Y�O�_�Ʈ�-1
class Solution:
    def numberOfSteps(self, num: int) -> int:
        res = 0
        while(num!=0):
            # ��num&1�D0, �N��num�O�_��
            if num&1:
                num -= 1
            # num�O����
            else:
                # ��2���P��k���@�줸, �`�N�p�G��num/=2, num�|��float�ӫDint
                num >>= 1
            res += 1
        return res
        
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
