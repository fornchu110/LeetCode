#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
# �N���w���Ʀrn, ��G�i���ܪk��ӭ˹L��

# By divide and conquer, time: O(1), space: O(1)
# ���ݭn�j��, �Q�k�O���@�b���洫, �o��Ӥ@�b���S���@�b�ǭǥ洫, ����@�өM�@�ӥ洫���n�N�|�O����
# 32 = 2^5, �ҥH�`�@�|��5��
class Solution:
    def reverseBits(self, n):
        # �C16bits�M��16bits�洫
        n = (n>>16)|(n<<16)
        # �C16bits���C8bits�M��8bits�洫...�U���H������
        # �洫��ڤW�O�Φ첾�F��, �ӥ�0x...�o��mask�M�w����bits�n����
        # 0xff00ff00�N���b�M�k�b16bits���U�۪���8bits, �]���k�洫�ҥH�n���k8bits
        # 0x00ff00ff�N���b�M�k�b16bits���U�۪��k8bits, �U�����H������ 
        n = ((n&0xff00ff00)>>8)|((n&0x00ff00ff)<<8)
        n = ((n&0xf0f0f0f0)>>4)|((n&0x0f0f0f0f)<<4)
        n = ((n&0xcccccccc)>>2)|((n&0x33333333)<<2)
        n = ((n&0xaaaaaaaa)>>1)|((n&0x55555555)<<1)
        return n

# By bitwise, time: O(1), space: O(1)
# python��ƪ��׵L��, ���F�����@��int�ҥH�u��32��, �]��O(1)
# �Dpython����32bits�����time�N�|�OO(logn)
# class Solution:
#     def reverseBits(self, n):
#         res = 0
#         # ���]int��32bit
#         for i in range(32):
#             # res������1bit, �A�Mn&1��|, �̫�N���G�s��res
#             # ��0��|���P��+, �]�N�O�bn���_�Ʈ�+1, ���Ʈ�+0
#             # �û����|�i��
#             # �Ĥ@��0<<=1, �]�N�O0�����@�줸��, 0�᭱���ѤU��
#             # �]�N�O�]�����Mrange(32)��32��, ����ڤW�u����31���@32bit
#             # �]�i�令|��Ares<<=1, ���o�˥���32���@33bits, �ҥHreturn�ɭnres>>1
#             res = res<<1|(n&1)
#             n >>= 1
#         return res
        
# @lc code=end

