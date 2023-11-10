#
# @lc app=leetcode id=1743 lang=python3
#
# [1743] Restore the Array From Adjacent Pairs
#

# @lc code=start
# 給一相鄰陣列adjacentPairs, 裡面每個元素代表在原陣列中的相鄰關係, return原陣列

# By hash, time: O(n), space: O(n)
# 首先注意到題目會將"所有"相鄰關係都提供出來
# 所以除了原陣列中頭尾的元素以外, 其他元素都會出現2次
# Ex: [1, 2, 3, 4], 那相鄰陣列中1、4會出現1次, 2、3會出現兩次
# 而這樣總共相鄰陣列會有6個數字3對元素, 所以原陣列長度必定是相鄰陣列長度+1
# 再來將相鄰陣列建成hash方便查找, 並把出現1次的元素作為頭尾再還原回去即可
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        # 原陣列長度
        n = len(adjacentPairs)+1
        # 建立hash用, 計算每個數字出現次數
        tmp = []
        for i in adjacentPairs:
            tmp.append(i[0])
            tmp.append(i[1])
        count = collections.Counter(tmp)
        hash = {}
        for a, b in adjacentPairs:
            if a not in hash:
                hash[a] = []
            hash[a].append(b)
            if b not in hash:
                hash[b] = []
            hash[b].append(a)
        # 出現一次的元素必定是頭尾, 抓一個當頭
        for key, value in count.items():
            if value==1:
                start = key
                break
        # 開始還原, 初始化第一個元素和他旁邊共兩個元素
        res = [0]*n
        res[0] = start
        res[1] = hash[start][0]
        for i in range(2, n):
            # 以index 2當第三個元素為例
            # 第三個元素必定在第二個元素旁邊
            x = res[i-1]
            # 回頭找第二個元素的關係, hash[第二個元素]會有已經在他左邊和不在他左邊的
            # 在他左邊的實際上就是第一個元素, 也就是res[i-2], 找出另一個就是第三個元素了
            for j in hash[x]:
                if j!=res[i-2]:
                    res[i] = j
        return res

# @lc code=end

