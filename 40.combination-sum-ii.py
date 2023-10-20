#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
# By sort and recursive, time: 
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # �o���D�حn�Q���sort
        candidates.sort()
        # �ЫتŰ}�C, []�į��list()�n
        res = []
        # used��ܤw�g����ƭȪ��C��, remain��ܶZ��target�ٮt����
        def find(idx, used, remain):
            for i in range(idx, len(candidates)):
                num = candidates[i]
                # ��recursive�P�@�Ť����|�X�{�ۦP����, �����P�Ť����i�H
                if i>idx and candidates[i-1]==candidates[i]:
                    continue
                # ���ŦX�t�Ȫ�num, �N��M��Uused�ꦨ�@��
                if num == remain:
                    res.append(used+[num])
                    return
                # �]���w�ƧǹL, �ҥH�Y�p��t��, �������U�~���
                if num<remain:
                    find(i+1, used+[num], remain-num)
                # ���ΦA���U��F, �{�b�j��t�ȫ᭱�@�w����j
                if num>remain:
                    return
        find(0,[], target)
        return res
        
# @lc code=end

