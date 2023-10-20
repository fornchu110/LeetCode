#
# @lc app=leetcode id=1528 lang=python3
#
# [1528] Shuffle String
#

# @lc code=start
# By zip and join(), time: O(n), space: O(1)
# 給一個str以及indices代表str中各字符應該放置到的index
# 利用zip(s, indices)就可同時讀到各個字符該放在哪個index, 儲存進res這個list
# 因需要return字串, 所以用"".join(res)這個技巧將res從list轉換成字串
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [0]*len(s)
        # 用zip同時走訪s和indices
        for i, idx in zip(s, indices):
            res[idx] = i
        # "".join(res)是指將res這個list內的元素用""也就是無字符來連結成新字串
        return "".join(res)

# @lc code=end

