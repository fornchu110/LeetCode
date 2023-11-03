<<<<<<< HEAD
#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
# ���@�Ӽƭn�D�o�X��G�i��U1���Ӽ�

# By bitwise, time: O(log(n)), space: O(1), n�����w�Ƥ�1���U��
# �ޥ��b��Q��n&(n-1)�|��̧C�줸��1�ഫ��0���ʽ�, �n�O�o�o��
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= n-1
            res += 1
        return res

# By bitwise, time: O(k), space: O(1), �]�D�ص�32�줸�ƩҥHk = 32
# �q�̥k��}�l�C���M1��&, �Y�̥k�䨺��O1�����G�N�O1, �M��k���`����
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         res = 0
#         while n:
#             if n&1:
#                 res += 1
#             n >>= 1
#         return res
        
# @lc code=end

=======
#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
# ���@�Ӽƭn�D�o�X��G�i��U1���Ӽ�

# By bitwise, time: O(log(n)), space: O(1), n�����w�Ƥ�1���U��
# �ޥ��b��Q��n&(n-1)�|��̧C�줸��1�ഫ��0���ʽ�, �n�O�o�o��
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= n-1
            res += 1
        return res

# By bitwise, time: O(k), space: O(1), �]�D�ص�32�줸�ƩҥHk = 32
# �q�̥k��}�l�C���M1��&, �Y�̥k�䨺��O1�����G�N�O1, �M��k���`����
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         res = 0
#         while n:
#             if n&1:
#                 res += 1
#             n >>= 1
#         return res
        
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
