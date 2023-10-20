#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
# 給一陣列candidates和一數target, return使用無限量candidates內元素湊成target的所有集合
# 類似硬幣湊目標值問題, 硬幣求集合數量, 此題求集合本身

# By DP, time: O(target*nlogn), n = len(candidates)
# 用類似322題硬幣湊值的想法做
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 為什麼這題要用dict而不能用list?因為extend操作可能會影響非目標index之元素
        # list是屬於可變資料類型, 也就是可能指向相同位址, 改變一邊其他的也會被改變
        # 可變資料類型會發生資料其實來自同個位址, 只是變數名稱不同而已
        # 想到copy.copy()淺複製就是對可變資料類型仍然不用獨立的新記憶體位址, 要用copy.deepcopy()才有全新獨立位址
        # 回到這題, 如果用dp = [[]]*(target+1)來宣告一個內有target+1個[]的list, 裡面這些[]其實都是來自同個位址
        # 當直接給第i個[]賦值時, 等同指向新位址, 但若對其他沒指向新位址的[]append時, 會讓所有同位址的[]進行append
        # 用dict因已經給裡面元素不同的key了, 相對應的value都是跟著key生成的, 沒有相同位址的問題       

        # dp = {i:[] for i in range(target+1)}
        # 意思是對{}內target+1個元素, 每個元素等於i:[], 也就是dp[i] = []
        # 列表生成式前面是元素會長的樣子, 後面是作用的範圍, 外面是作用的資料型態
        # 下面等同上面這句
        # dp[i]代表當target = i時, condidates所能湊出的解集合
        dp = {}
        for i in range(target+1):
            dp[i] = []
        # 從candidate大至小做
        # 為什麼不能像硬幣問題從小至大做?因為會有重複解集合的問題
        for i in sorted(candidates,reverse=True):
            # 從i做到target
            for j in range(i,target+1):
                # 當剛好i==j代表一定可以用1個i來湊出j, 而且是從大而小做
                # 所以直接有一組初始解dp[j] = [[i]]
                if j==i:
                    dp[j] = [[i]]
                # 從dp[j-i]找新解
                else:
                    dp[j].extend([x+[i] for x in dp[j-i]])
        print(dp)
        return dp[target]

# By backtracking, time: O(S), space: O(target), S = len(所有可行解)
# 回朔+剪枝算法, 利用DFS, 剪枝意思是省去會造成重複解的搜索, 像這題[2, 2, 3]和[2, 3, 2]實際上是同一種
# 找所有排列組合都可以用回朔方法找, DFS其實就是回朔的一個體現
# 所以回朔要把解畫成tree, 以target做root, 每次找新child都對candidates內的新元素做減法
# 也就是說新node都是還沒用candidate分配所剩下的target, leaf.val<=0
# 每種到達leaf的path所使用的candidate就是不同解
# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         # 記錄一個pathsum做剪枝加速計算, 不用每次重新做sum, 空間換時間
#         def dfs(startIdx, path, pathsum):
#             # 將res全部改成self.res可以不用nonlocal
#             nonlocal res
#             if pathsum==target:
#                 res.append(path[:])
#                 return

#             for i in range(startIdx, n):
#                 if pathsum+candidates[i]<=target:
#                     dfs(i, path + [candidates[i]], pathsum + candidates[i]) # 注意?里的i，下?循?可以包含本身，但不能包含之前的，避免重复
#                 # 剪枝
#                 # 如果當前path和大於target，就不用繼續往後走訪了, 做剪枝
#                 else:
#                     break 
#         # sort後方便走訪剪枝
#         candidates.sort() 
#         n = len(candidates)
#         path = []
#         # 如果做self.res = [], 等同於定義此class有一個res
#         # 那這class下面任何函式都可以對self.res做操作, 就不需要nonlocal
#         res = []
#         # 剛開始startindex為0
#         # 不希望有重複解的做法就是每層以新的candidate開頭往下走時, 接下來不能使用前面用過的candidate
#         dfs(0, path, 0) 
#         return res

# @lc code=end

