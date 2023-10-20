#
# @lc app=leetcode id=1281 lang=python3
#
# [1281] Subtract the Product and Sum of Digits of an Integer
#

# @lc code=start

# By while loop, time: O(lon(n)), space: O(1)
# time�OO(log(n))����], n�Oinput��n����Ʒ|��10������log(n+1)
# �]�N�O��O(log(n))�N�On����Ƽƶq, �Yn���O��input�ӬO��ƪ���time: O(n)
# �n�Ninput��n�C��Ƭۭ�, �A�N�C��Ƭۥ[, �̫�n-�M
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        pro = 1
        sum = 0
        while(n!=0):
            pro *= n%10
            sum += n%10
            n//=10
        return pro-sum

# @lc code=end

