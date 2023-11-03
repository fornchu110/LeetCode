<<<<<<< HEAD
#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
# �����P������coins�M���Bamout
# return��X���Pamount���B�һݳּ̤ƶq��coins, �p�G�L�k��X���Pamount�����Breturn -1

# By DP, time: O(A*n), space: O(A), A�Oamount, n�Olen(coins)�]�N�Ocoins������ 
# �Q��0-1�I�]���D, �u�Ocoins���i�H�L�����������~�Ӥw
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # ��l��dp�}�Cindex�q0~amount�@amount+1�Ӥ���, ���e�s��ۤ��Pamount�ɪ��̨θ�
        # �n�D���O�̤p�Ʀ���, �ҥH��l�Ƭ��L���j(float("inf"))�n�ΨӤ��
        dp = [float('inf')]*(amount+1)
        # ��l�ƥ��w�i�H��0�ӵw����X0, �o�˫᭱���ݭn���Xdp[0]
        dp[0] = 0
        
        for i in coins:
            # �qi�}�l�]������ȬOi��, �ڥ��L�k��Xamount<i
            # Ex: �L�k��5����X1234��, ���h0��0����X0, ���w�g��l��dp[0] = 0�F
            for j in range(i, amount+1):
                # �쥻��dp[j]�N��amount= j�ɧ�p���Ȫ��̨θ�
                # dp[j-i]�]�O�p��, ��dp[j]�i�H�Odp[j-i]�A�[�W1�����Ȭ�i���w��, �ҥH�|�Odp[j-i]+1
                # �q��p���Ȫ��̨θѩMdp[j-i+1]���@�Ӹ��p��, ���N�|�O�s���̨θ�
                # �q�`�u�n��ϥΧ�j���Ȩ��@�w�|��֦���
                # �L�ѴN�o�ͦb�o��̳��O�L���j�����p
                dp[j] = min(dp[j], dp[j-i]+1)
        # dp[amonut]�N���coins��Xamount�һݪ��ּ̤ƶq
        # ��l�Ƭ��L���j�]���D�L���j�~�N����
        if dp[amount]!=float('inf'):
            return dp[amount] 
        # �L���j�N��L��
        else:
            return -1 

# @lc code=end

=======
#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
# �����P������coins�M���Bamout
# return��X���Pamount���B�һݳּ̤ƶq��coins, �p�G�L�k��X���Pamount�����Breturn -1

# By DP, time: O(A*n), space: O(A), A�Oamount, n�Olen(coins)�]�N�Ocoins������ 
# �Q��0-1�I�]���D, �u�Ocoins���i�H�L�����������~�Ӥw
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # ��l��dp�}�Cindex�q0~amount�@amount+1�Ӥ���, ���e�s��ۤ��Pamount�ɪ��̨θ�
        # �n�D���O�̤p�Ʀ���, �ҥH��l�Ƭ��L���j(float("inf"))�n�ΨӤ��
        dp = [float('inf')]*(amount+1)
        # ��l�ƥ��w�i�H��0�ӵw����X0, �o�˫᭱���ݭn���Xdp[0]
        dp[0] = 0
        
        for i in coins:
            # �qi�}�l�]������ȬOi��, �ڥ��L�k��Xamount<i
            # Ex: �L�k��5����X1234��, ���h0��0����X0, ���w�g��l��dp[0] = 0�F
            for j in range(i, amount+1):
                # �쥻��dp[j]�N��amount= j�ɧ�p���Ȫ��̨θ�
                # dp[j-i]�]�O�p��, ��dp[j]�i�H�Odp[j-i]�A�[�W1�����Ȭ�i���w��, �ҥH�|�Odp[j-i]+1
                # �q��p���Ȫ��̨θѩMdp[j-i+1]���@�Ӹ��p��, ���N�|�O�s���̨θ�
                # �q�`�u�n��ϥΧ�j���Ȩ��@�w�|��֦���
                # �L�ѴN�o�ͦb�o��̳��O�L���j�����p
                dp[j] = min(dp[j], dp[j-i]+1)
        # dp[amonut]�N���coins��Xamount�һݪ��ּ̤ƶq
        # ��l�Ƭ��L���j�]���D�L���j�~�N����
        if dp[amount]!=float('inf'):
            return dp[amount] 
        # �L���j�N��L��
        else:
            return -1 

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
