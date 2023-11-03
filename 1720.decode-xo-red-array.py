<<<<<<< HEAD
#
# @lc app=leetcode id=1720 lang=python3
#
# [1720] Decode XORed Array
#

# @lc code=start
# By XOR(^), time: O(n), space: O(1)
# ���w�[�K�L��list, list���C�Ӥ������O�쥻arr���۾F��Ǥ���xor�Ӧ�
# �|�����Aarr�Ĥ@�Ӥ���, �n�D�Xarr���M
# �Q�ΤFXOR���ʽ�1. x^0 = x, 2. x^x = 0�H�Υ洫�ʩM���X��
# �i�H�ݥXx^y = z����, x^z = y�Bz^y = x, �ҥH�̧ǰ�XOR�Y�i�o�X����
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        # �@�}�l�Nfirst��J�N����append�F
        res = [first]
        tmp = first
        for i in encoded:
            tmp ^= i
            res.append(tmp)
        return res

# @lc code=end

=======
#
# @lc app=leetcode id=1720 lang=python3
#
# [1720] Decode XORed Array
#

# @lc code=start
# By XOR(^), time: O(n), space: O(1)
# ���w�[�K�L��list, list���C�Ӥ������O�쥻arr���۾F��Ǥ���xor�Ӧ�
# �|�����Aarr�Ĥ@�Ӥ���, �n�D�Xarr���M
# �Q�ΤFXOR���ʽ�1. x^0 = x, 2. x^x = 0�H�Υ洫�ʩM���X��
# �i�H�ݥXx^y = z����, x^z = y�Bz^y = x, �ҥH�̧ǰ�XOR�Y�i�o�X����
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        # �@�}�l�Nfirst��J�N����append�F
        res = [first]
        tmp = first
        for i in encoded:
            tmp ^= i
            res.append(tmp)
        return res

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
