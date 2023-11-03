<<<<<<< HEAD
#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
# 給不同種類的coins和金額amout
# return湊出等同amount金額所需最少數量的coins, 如果無法湊出等同amount的金額return -1

# By DP, time: O(A*n), space: O(A), A是amount, n是len(coins)也就是coins種類數 
# 想到0-1背包問題, 只是coins為可以無限拿取的物品而已
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 初始化dp陣列index從0~amount共amount+1個元素, 內容存放著不同amount時的最佳解
        # 要求的是最小化次數, 所以初始化為無限大(float("inf"))好用來比較
        dp = [float('inf')]*(amount+1)
        # 初始化必定可以用0個硬幣湊出0, 這樣後面不需要走訪dp[0]
        dp[0] = 0
        
        for i in coins:
            # 從i開始因為當幣值是i時, 根本無法湊出amount<i
            # Ex: 無法用5元湊出1234元, 頂多0個0元湊出0, 但已經初始化dp[0] = 0了
            for j in range(i, amount+1):
                # 原本的dp[j]代表amount= j時更小幣值的最佳解
                # dp[j-i]也是如此, 但dp[j]可以是dp[j-i]再加上1塊價值為i的硬幣, 所以會是dp[j-i]+1
                # 從更小幣值的最佳解和dp[j-i+1]取一個較小值, 那就會是新的最佳解
                # 通常只要能使用更大幣值那一定會減少次數
                # 無解就發生在這兩者都是無限大的情況
                dp[j] = min(dp[j], dp[j-i]+1)
        # dp[amonut]代表由coins湊出amount所需的最少數量
        # 初始化為無限大因此非無限大才代表有解
        if dp[amount]!=float('inf'):
            return dp[amount] 
        # 無限大代表無解
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
# 給不同種類的coins和金額amout
# return湊出等同amount金額所需最少數量的coins, 如果無法湊出等同amount的金額return -1

# By DP, time: O(A*n), space: O(A), A是amount, n是len(coins)也就是coins種類數 
# 想到0-1背包問題, 只是coins為可以無限拿取的物品而已
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 初始化dp陣列index從0~amount共amount+1個元素, 內容存放著不同amount時的最佳解
        # 要求的是最小化次數, 所以初始化為無限大(float("inf"))好用來比較
        dp = [float('inf')]*(amount+1)
        # 初始化必定可以用0個硬幣湊出0, 這樣後面不需要走訪dp[0]
        dp[0] = 0
        
        for i in coins:
            # 從i開始因為當幣值是i時, 根本無法湊出amount<i
            # Ex: 無法用5元湊出1234元, 頂多0個0元湊出0, 但已經初始化dp[0] = 0了
            for j in range(i, amount+1):
                # 原本的dp[j]代表amount= j時更小幣值的最佳解
                # dp[j-i]也是如此, 但dp[j]可以是dp[j-i]再加上1塊價值為i的硬幣, 所以會是dp[j-i]+1
                # 從更小幣值的最佳解和dp[j-i+1]取一個較小值, 那就會是新的最佳解
                # 通常只要能使用更大幣值那一定會減少次數
                # 無解就發生在這兩者都是無限大的情況
                dp[j] = min(dp[j], dp[j-i]+1)
        # dp[amonut]代表由coins湊出amount所需的最少數量
        # 初始化為無限大因此非無限大才代表有解
        if dp[amount]!=float('inf'):
            return dp[amount] 
        # 無限大代表無解
        else:
            return -1 

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
