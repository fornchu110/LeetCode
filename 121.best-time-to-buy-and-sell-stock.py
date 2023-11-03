#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
# By DP
#���]�b��i�ѽ�X, ���b�oi�Ѥ����̧C�I�ʶR�N���̤j���q
#i�Ѥ������v�̧C�I, �u���i��O��i-1�Ѯɪ��̧C�I�β�i�Ѫ�������
#�]���i�g���ʺA�W��
#i�ѶRi�ѽ�S�N�q, �ҥH���v�̧C�I�O�b�⧹���q��A��s
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        inf = int(1e9)
        minprice = inf
        maxprofit = 0
        for price in prices:
            maxprofit = max(price - minprice, maxprofit)
            minprice = min(price, minprice)
        return maxprofit

# @lc code=end

