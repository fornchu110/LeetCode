#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
# ���@�}�Ccandidates�M�@��target, return�ϥεL���qcandidates�������ꦨtarget���Ҧ����X
# �����w����ؼЭȰ��D, �w���D���X�ƶq, ���D�D���X����

# By DP, time: O(target*nlogn), n = len(candidates)
# ������322�D�w����Ȫ��Q�k��
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # ������o�D�n��dict�Ӥ����list?�]��extend�ާ@�i��|�v�T�D�ؼ�index������
        # list�O�ݩ�i�ܸ������, �]�N�O�i����V�ۦP��}, ���ܤ@���L���]�|�Q����
        # �i�ܸ�������|�o�͸�ƨ��ӦۦP�Ӧ�}, �u�O�ܼƦW�٤��P�Ӥw
        # �Q��copy.copy()�L�ƻs�N�O��i�ܸ���������M���οW�ߪ��s�O�����}, �n��copy.deepcopy()�~�����s�W�ߦ�}
        # �^��o�D, �p�G��dp = [[]]*(target+1)�ӫŧi�@�Ӥ���target+1��[]��list, �̭��o��[]��곣�O�ӦۦP�Ӧ�}
        # ��������i��[]��Ȯ�, ���P���V�s��}, ���Y���L�S���V�s��}��[]append��, �|���Ҧ��P��}��[]�i��append
        # ��dict�]�w�g���̭��������P��key�F, �۹�����value���O���key�ͦ���, �S���ۦP��}�����D       

        # dp = {i:[] for i in range(target+1)}
        # �N��O��{}��target+1�Ӥ���, �C�Ӥ�������i:[], �]�N�Odp[i] = []
        # �C��ͦ����e���O�����|�����ˤl, �᭱�O�@�Ϊ��d��, �~���O�@�Ϊ���ƫ��A
        # �U�����P�W���o�y
        # dp[i]�N���target = i��, condidates�ү��X���Ѷ��X
        dp = {}
        for i in range(target+1):
            dp[i] = []
        # �qcandidate�j�ܤp��
        # �����򤣯๳�w�����D�q�p�ܤj��?�]���|�����ƸѶ��X�����D
        for i in sorted(candidates,reverse=True):
            # �qi����target
            for j in range(i,target+1):
                # ���ni==j�N��@�w�i�H��1��i�Ӵ�Xj, �ӥB�O�q�j�Ӥp��
                # �ҥH�������@�ժ�l��dp[j] = [[i]]
                if j==i:
                    dp[j] = [[i]]
                # �qdp[j-i]��s��
                else:
                    dp[j].extend([x+[i] for x in dp[j-i]])
        print(dp)
        return dp[target]

# By backtracking, time: O(S), space: O(target), S = len(�Ҧ��i���)
# �^��+�ŪK��k, �Q��DFS, �ŪK�N��O�٥h�|�y�����ƸѪ��j��, ���o�D[2, 2, 3]�M[2, 3, 2]��ڤW�O�P�@��
# ��Ҧ��ƦC�զX���i�H�Φ^�Ҥ�k��, DFS���N�O�^�Ҫ��@����{
# �ҥH�^�ҭn��ѵe��tree, �Htarget��root, �C����schild����candidates�����s��������k
# �]�N�O���snode���O�٨S��candidate���t�ҳѤU��target, leaf.val<=0
# �C�ب�Fleaf��path�ҨϥΪ�candidate�N�O���P��
# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         # �O���@��pathsum���ŪK�[�t�p��, ���ΨC�����s��sum, �Ŷ����ɶ�
#         def dfs(startIdx, path, pathsum):
#             # �Nres�����令self.res�i�H����nonlocal
#             nonlocal res
#             if pathsum==target:
#                 res.append(path[:])
#                 return

#             for i in range(startIdx, n):
#                 if pathsum+candidates[i]<=target:
#                     dfs(i, path + [candidates[i]], pathsum + candidates[i]) # �`�N?����i�A�U?�`?�i�H�]�t�����A������]�t���e���A�קK���`
#                 # �ŪK
#                 # �p�G��epath�M�j��target�A�N�����~�򩹫ᨫ�X�F, ���ŪK
#                 else:
#                     break 
#         # sort���K���X�ŪK
#         candidates.sort() 
#         n = len(candidates)
#         path = []
#         # �p�G��self.res = [], ���P��w�q��class���@��res
#         # ���oclass�U������禡���i�H��self.res���ާ@, �N���ݭnnonlocal
#         res = []
#         # ��}�lstartindex��0
#         # ���Ʊ榳���ƸѪ����k�N�O�C�h�H�s��candidate�}�Y���U����, ���U�Ӥ���ϥΫe���ιL��candidate
#         dfs(0, path, 0) 
#         return res

# @lc code=end

