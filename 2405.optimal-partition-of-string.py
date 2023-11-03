<<<<<<< HEAD
#
# @lc app=leetcode id=2405 lang=python3
#
# [2405] Optimal Partition of String
#

# @lc code=start
# ���@�Ӧr��s, �n�D�N��Ӷ��Ǥ��ά����P�l�r��, �l�r�ꤺ���঳���ƪ��r��

# By hash, time: O(n), space: O(n)
# �إ�hash, �����l�r��J�줣�s�b���r���N�O�����~��, �J��w�s�b���N�N�����W�@��, �إ߷s��hash
# �]�i�H��set�s�@hash, set.clear(), set.add()�i�H�[�J
class Solution:
    def partitionString(self, s: str) -> int:
        hash = {}
        # �q�{����O1?�]��s���צܤ֬O1, �N��ܤַ|���@�Ӧr���r��
        res = 1
        for i in s:
            # �J�쭫�ƪ��N�N��n�ؤ@�ӷs���l�r��, �åB�M��
            if i in hash:
                res += 1
                hash = {}
            # �L�׬O�_����, ���n�Ni�O���ihash
            # �S���ƮɰO���U�Ӥ~���ˬd
            # ���Ʈɦ]�I�즹�ɲM�ŤFhash, ���n�N�o���I�쪺�r���O���ihash�קK��
            hash[i] = 1
        return res

# By bitwise, time: O(n), space: O(1)
# �Q��32��bit�O���ˬd26�Ӧr���O�_�s�b
# a��b��0�Ӧ줸, z��b��25�Ӧ줸�H������, �Υ���1���O���M�ˬd
# ��������ɶ��Ŷ�����hash�t
# class Solution:
#     def partitionString(self, s: str) -> int:
#         res = 1
#         tmp = 0
#         for i in s:
#             # �M'a'��ASCII code����۹��m
#             index = ord(i)-ord('a')
#             # mask�N�O�o�����r����������m
#             mask = 1<<index
#             # �X�{���Ʀr��, ��res+1�åB�Ntmp = mask���P�O���F�o�����r��
#             if tmp&mask:
#                 res += 1
#                 tmp = mask
#             else:
#                 # �X�{�����Ʀr��, ���N��§�mask�O���W�h��1
#                 tmp |= mask
#             # ��ꪽ���b�~���o��gtmp |= mask, if�Melse����tmp�������Ӥ]��
#         return res



# @lc code=end

=======
#
# @lc app=leetcode id=2405 lang=python3
#
# [2405] Optimal Partition of String
#

# @lc code=start
# ���@�Ӧr��s, �n�D�N��Ӷ��Ǥ��ά����P�l�r��, �l�r�ꤺ���঳���ƪ��r��

# By hash, time: O(n), space: O(n)
# �إ�hash, �����l�r��J�줣�s�b���r���N�O�����~��, �J��w�s�b���N�N�����W�@��, �إ߷s��hash
# �]�i�H��set�s�@hash, set.clear(), set.add()�i�H�[�J
class Solution:
    def partitionString(self, s: str) -> int:
        hash = {}
        # �q�{����O1?�]��s���צܤ֬O1, �N��ܤַ|���@�Ӧr���r��
        res = 1
        for i in s:
            # �J�쭫�ƪ��N�N��n�ؤ@�ӷs���l�r��, �åB�M��
            if i in hash:
                res += 1
                hash = {}
            # �L�׬O�_����, ���n�Ni�O���ihash
            # �S���ƮɰO���U�Ӥ~���ˬd
            # ���Ʈɦ]�I�즹�ɲM�ŤFhash, ���n�N�o���I�쪺�r���O���ihash�קK��
            hash[i] = 1
        return res

# By bitwise, time: O(n), space: O(1)
# �Q��32��bit�O���ˬd26�Ӧr���O�_�s�b
# a��b��0�Ӧ줸, z��b��25�Ӧ줸�H������, �Υ���1���O���M�ˬd
# ��������ɶ��Ŷ�����hash�t
# class Solution:
#     def partitionString(self, s: str) -> int:
#         res = 1
#         tmp = 0
#         for i in s:
#             # �M'a'��ASCII code����۹��m
#             index = ord(i)-ord('a')
#             # mask�N�O�o�����r����������m
#             mask = 1<<index
#             # �X�{���Ʀr��, ��res+1�åB�Ntmp = mask���P�O���F�o�����r��
#             if tmp&mask:
#                 res += 1
#                 tmp = mask
#             else:
#                 # �X�{�����Ʀr��, ���N��§�mask�O���W�h��1
#                 tmp |= mask
#             # ��ꪽ���b�~���o��gtmp |= mask, if�Melse����tmp�������Ӥ]��
#         return res



# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
