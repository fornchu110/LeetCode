#
# @lc app=leetcode id=859 lang=python3
#
# [859] Buddy Strings
#

# @lc code=start

# By enum , time: O(n), space: O(c), 因有26個英文字母所以c = 26
# 要注意到特例並優先判斷, 確認好特例的情況再開始做處理
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # 長度不一樣必為false
        if len(s)!=len(goal):
            return False
        # 如果s和goal完全相同, 應該像這樣在實際交換前就判斷, 不該放在後面
        if s==goal:
            # 有相同char的話set必定比較小, 可以交換
            if len(set(s))<len(goal): 
                return True
            # s和goal內部完全沒有重複char, 不可交換
            else:
                return False
        # zip在做將不同iterable資料結構中相同位置的兩元素放進()裡
        # 所以zip(s, goal)是個list, zip(s, goal)[0] = (s[0], goal[0]), ...
        # 直到較短的資料結構結束, 捨棄較長中的剩下的元素
        # zip的用途是同時處理不同iterable資料結構, 很適合判斷str是否相同和共同sub str
        diff = [(a, b) for a, b in zip(s, goal) if a!=b]
        print(diff)
        # 看s和goal同位置時不同char的狀況數量, 應該要==2且交換後就完全相等
        return len(diff)==2 and diff[0][0]==diff[1][1] and diff[0][1]==diff[1][0]

# @lc code=end

