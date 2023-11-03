#
# @lc app=leetcode id=860 lang=python3
#
# [860] Lemonade Change
#

# @lc code=start

# By Greedy, time: O(n), space: O(1)
# �u�Ψ���ܶq�sfive�Mten�����k, greedy�b�n��15���u����ܧ�10+5�ӫD5*3
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        for i in range(len(bills)):
            if bills[i]==5:
                five += 1
            elif bills[i]==10:
                if five>=1:
                    five -= 1
                    ten += 1
                else:
                    return False
            elif bills[i]==20:
                if ten>=1 and five>=1:
                    five -= 1
                    ten -= 1
                elif five>=3:
                    five -= 3
                else:
                    return False
        return True

# By Greedy hashtable, time: O(n), space: O(1)
# �`���N�O�J��5��������, �J��10���ݦ��S��5���, �J��20�ݦ��S��15���
# ����ڤW���ӥ�hasttable�s5���M10���ƶq, 20�]���Φs, ��������ܶq�Y�i
# class Solution:
#     def lemonadeChange(self, bills: List[int]) -> bool:
#         change = dict([(5, 0), (10, 0), (20, 0)])
#         for i in range(len(bills)):
#             if bills[i]==5:
#                 change[5] += 1
#             elif bills[i]==10:
#                 if change[5]>=1:
#                     change[5] -= 1
#                     change[10] += 1
#                 else:
#                     return False
#             elif bills[i]==20:
#                 if change[10]>=1 and change[5]>=1:
#                     change[5] -= 1
#                     change[10] -= 1
#                     change[20] += 1
#                 elif change[5]>=3:
#                     change[5] -= 3
#                     change[20] += 1
#                 else:
#                     return False
#         return True


        
# @lc code=end

