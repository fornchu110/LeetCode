#
# @lc app=leetcode id=1534 lang=python3
#
# [1534] Count Good Triplets
#

# @lc code=start
# ���@�}�Carr�M�T���a�Bb�Bc, ��Xarr���T�Ӻ��i��index i�Bj�Bk
# �ϱo|arr[i]-arr[j]|<=a�B|arr[j]-arr[k]|<=b�B|arr[i]-arr[k]]<=c
# return�ŦX���󪺤Tindex�ռƶq

# By triple for loop(simulation), time: O(n^3), space: O(1)
# �Ѥp�ܤj��index�@�ӭ��ˬd��X�ŦX����
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        res = 0
        # index���|����, i�᭱�ܤ��٦�j�Mk�ҥH����˼ƲĤT�ӴN�i
        for i in range(len(arr)-2):
            for j in range(i+1, len(arr)-1):
                # �u���קK���������T�j�骺�覡
                # �w�g��index i�Bj, �]������n���ŦX
                # �ҥH���P�_��i�Bj����������O�_�ŦX, ���ŦX�N���άݸ�k����������F, ���ŦX�A��for�j��
                if abs(arr[i]-arr[j])<=a:
                    for k in range(j+1, len(arr)):
                        if abs(arr[j]-arr[k])<=b and abs(arr[i]-arr[k])<=c:
                            res += 1
        return res
                                                    
# @lc code=end

