#
# @lc app=leetcode id=319 lang=python3
#
# [319] Bulb Switcher
#

# @lc code=start
# 倒n縊獁秨﹍琌闽超, 材1近ゴ秨┮Τ, 材2近–2闽超, 碞琌弧材i近璶ち传i计縊獁秨闽, return n近Τぶ縊獁獹帝

# By math, time: O(1), space: O(1)
# 芠诡砏祇瞷, 材i縊獁砆ち传Ω计碞琌ㄤ计计
# ┮Τ案计计縊獁程穦穞, Τ计计縊獁程穦獹
# 计ㄢㄢΘ癸, Ex: 2琌8计, ê8/2 = 4琌8计, 硂贺, 祇瞷Τ贺薄猵计ぃΘ癸
# ê碞琌Чキよ计, Ex: 3琌9计, 9/3 = 3竒衡筁
# ┮Τ讽i琌Чキよ计穦Τ计计, 浪琩n縊獁Чキよ计计秖碞琌氮
# nずЧキよ计计碞琌腹n
class Solution:
    def bulbSwitch(self, n: int) -> int:
        # +0.5琌疊翴笲衡俱, 硂肈ぃ穦筁
        return int(sqrt(n+0.5))

# @lc code=end

