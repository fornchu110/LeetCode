#
# @lc app=leetcode id=2011 lang=python3
#
# [2011] Final Value of Variable After Performing Operations
#

# @lc code=start
# By string compartion, time: O(n), space: O(1)
# ��list���C�Ӧr�갵���, �u��X++, ++X , X--, --X�|�إi��
# �e���x += 1, ����x -= 1�Y�i
# ���Ǫ��覡�O�u�P�_list���r�ꤤ�����ӲŸ�, ����+��-
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for i in operations:
            # �����P�_���覡
            # if i=="X++" or i=="++X":
            # ���ǧP�_i[1]����+��-
            if i[1]=="+":
                x += 1
            else:
                x -= 1
        return x 
        
# @lc code=end

