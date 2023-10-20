#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
# 給一由字母組成的二維陣列board和一字串word, 判斷word是否存在board中return ture false
# word存在board的意思是可以在二維陣列中找到一個連續路徑連成word

# By backtracking recursive, time: O(MN*3^L), space: O(MN), 其中M、N為board之row、col, L為len(word)
# time = O(MN*3^L)是因為, 首先至少要一一走訪board內所有元素, 再來要對每個元素最多會有三個相鄰元素要判斷
# space = O(MN)是因為額外用了visited這個set, 避免走訪到相同位置

# 要建立一個函式check, 代表從(i, j)出發時, 能否往下找到word[k:]字串, k之前就是已經走訪到的word內容
# 所以說在check的過程中只要遇到board(i, j)不等於k代表false
# 如果走訪完word仍然相同代表true
# 當board(i, j)等於k且走訪仍未完成, 則從(i, j)相鄰的三個元素為起點做check找s[k+1:]
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 分別代表右、左、下、上四種移動操作
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # 參數i、j是row、col, k是目前要搜尋的字元
        def check(i: int, j: int, k: int) -> bool:
            # 終止條件 找失敗和已找完
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            # 走訪過的位置記錄在visited內, 跟list不同不是用append
            visited.add((i, j))
            # 初始化為沒找到, check完會return result
            result = False
            # 對每個元素做四種可能的移動
            for di, dj in directions:
                # 做完移動後的座標
                newi, newj = i+di, j+dj
                # 注意不能out of range, 所以在範圍內才能做
                if 0<=newi<len(board) and 0<=newj<len(board[0]):
                    # 新移動是沒走訪過的座標, 代表不會回頭
                    if (newi, newj) not in visited:
                        # 繼續往下找, check(newi, newj, k+1)為True, 代表這個方向可以走訪到word[k+1:]
                        if check(newi, newj, k+1):
                            # 而走到這裡同時也代表(i, j)有k, 所以往上面return說從(i, j)能走訪到word[k:]
                            result = True
                            break
            # (i, j)這個位置走訪結束了, 也就是已經找到word[k:]或是確定三種移動都無法找出word[k:]就刪除(i, j)
            # 重置目的是給其他位置為起點走訪使用, 原本visited只是為了每次到各個位置走訪時, 不要回頭找
            visited.remove((i, j))
            return result
        
        # board之row、col
        h, w = len(board), len(board[0])
        # 位置獨一無二所以可以用set(), 重點是可以用add、remove還有in
        # 不用像list()一樣注意重複和index
        visited = set()
        # 對board所有元素做check
        for i in range(h):
            for j in range(w):
                # check(i, j, 0)為True代表在(i, j)能走訪出word[0:], 也就是整個word
                if check(i, j, 0):
                    return True    
        return False
    
# @lc code=end

