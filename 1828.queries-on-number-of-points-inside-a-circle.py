#
# @lc app=leetcode id=1828 lang=python3
#
# [1828] Queries on Number of Points Inside a Circle
#

# @lc code=start
# By enumerate, time: O(m*n), space: O(1), m�O��߼ƶq, n�O�I�ƶq
# �o�D����ߩM��b�|, �D���wn��points��󤣦P�ꤺ���ƶq
class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = list()
        # python�i�H�����ά۹������榡��o�ƾ�, ���[
        for (cx, cy, cr) in queries:
            tmp = 0
            for (px, py) in points:
                if(cx-px)**2+(cy-py)**2<=cr**2:
                    tmp += 1
            res.append(tmp)
        # �A�u�ƥi�H��res = [0]*len(queries)
        # �M��N��٤Utmp�Ŷ�, ����for i, (cx, cy, cr) in enumerate(queries):
        # �P����oindex i�M���N(cx, cy, cr), �o�˦bif���߮�res[i] += 1�Y�i

        # �@�}�l�����k, ��i�h���N���, ��j���N�I, index�Ӧs�����e
        # ��c�y���g�k
        # for i in queries:
        #     tmp = 0
        #     for j in points:
        #         if (i[0]-j[0])**2+(i[1]-j[1])**2<=i[2]**2:
        #             tmp += 1
        #     res.append(tmp)
        return res

# @lc code=end

