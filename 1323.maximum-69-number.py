<<<<<<< HEAD
#
# @lc app=leetcode id=1323 lang=python3
#
# [1323] Maximum 69 Number
#

# @lc code=start
# By string processing
# �n�Nnum���@��6����9, return�o�ާ@�̤j����
# �N�O�n�N�̰���ƪ�6����9, �o�رq���ݨ�k��²�檺��k�N���ഫ��str
# �]��string processing�q����k��, �B�z���A�ഫ��int
class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        # replace()�O�^�ǭȤ~�����ܹL, 1�N��u�ഫ1��
        num = num.replace("6", "9", 1)
        return int(num)

# @lc code=end

=======
#
# @lc app=leetcode id=1323 lang=python3
#
# [1323] Maximum 69 Number
#

# @lc code=start
# By string processing
# �n�Nnum���@��6����9, return�o�ާ@�̤j����
# �N�O�n�N�̰���ƪ�6����9, �o�رq���ݨ�k��²�檺��k�N���ഫ��str
# �]��string processing�q����k��, �B�z���A�ഫ��int
class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        # replace()�O�^�ǭȤ~�����ܹL, 1�N��u�ഫ1��
        num = num.replace("6", "9", 1)
        return int(num)

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
