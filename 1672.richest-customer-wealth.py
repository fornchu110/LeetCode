<<<<<<< HEAD
#
# @lc app=leetcode id=1672 lang=python3
#
# [1672] Richest Customer Wealth
#

# @lc code=start
# By for loop, time: O(m*n), space: O(1)
# �n�X��@���}�C�������M�̤j��, ��m�Ӥ@���}�C, �C�Ӥ@���}�Cn�Ӥ���
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0
        # len(accounts)�N���P�@���}�C�ƶq
        for i in range(len(accounts)):
            tmp = 0
            # len(accounts[i])�N���P��i�Ӥ@���}�C���������ƶq
            for j in range(len(accounts[i])):
                tmp += accounts[i][j]
            if tmp>max:
                max = tmp
        # �{���i�H�u���U���orow
        #return max(map(sum, accounts))
        return max

# @lc code=end

=======
#
# @lc app=leetcode id=1672 lang=python3
#
# [1672] Richest Customer Wealth
#

# @lc code=start
# By for loop, time: O(m*n), space: O(1)
# �n�X��@���}�C�������M�̤j��, ��m�Ӥ@���}�C, �C�Ӥ@���}�Cn�Ӥ���
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0
        # len(accounts)�N���P�@���}�C�ƶq
        for i in range(len(accounts)):
            tmp = 0
            # len(accounts[i])�N���P��i�Ӥ@���}�C���������ƶq
            for j in range(len(accounts[i])):
                tmp += accounts[i][j]
            if tmp>max:
                max = tmp
        # �{���i�H�u���U���orow
        #return max(map(sum, accounts))
        return max

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
