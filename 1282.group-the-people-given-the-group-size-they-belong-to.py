<<<<<<< HEAD
#
# @lc app=leetcode id=1282 lang=python3
#
# [1282] Group the People Given the Group Size They Belong To
#

# @lc code=start
# By hash table, time: O(n), space: O(n)
# input�������O�Uid���H�Ҧbgroup���H��, �nreturn��input���tid������
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        res = list()
        # res�̭���ۦU��groupsize��i��group
        # hash[i]�N�O���F��@��groupsize��i��group�bres������m��index
        # �]�N�O��res[hash[i]]�Y��res��groupsize��i��group
        # �ҥHhash[i]�bsize��i��group���F�~�|�W�[
        hash = dict()
        for id, i in enumerate(groupSizes):
            # ��i���bhash���ΤW�@��group����, append�s��id�ires
            # len(res[hash[i]])==i�N�O�ΨӧP�_res��size��i��group���F�S
            if i not in hash or len(res[hash[i]])==i:
                hash[i] = len(res)
                res.append([id])
            # �bres[hash[i]]������, �~��Ni��id append�i�h
            else:
                res[hash[i]].append(id)
        return res
        
# @lc code=end

=======
#
# @lc app=leetcode id=1282 lang=python3
#
# [1282] Group the People Given the Group Size They Belong To
#

# @lc code=start
# By hash table, time: O(n), space: O(n)
# input�������O�Uid���H�Ҧbgroup���H��, �nreturn��input���tid������
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        res = list()
        # res�̭���ۦU��groupsize��i��group
        # hash[i]�N�O���F��@��groupsize��i��group�bres������m��index
        # �]�N�O��res[hash[i]]�Y��res��groupsize��i��group
        # �ҥHhash[i]�bsize��i��group���F�~�|�W�[
        hash = dict()
        for id, i in enumerate(groupSizes):
            # ��i���bhash���ΤW�@��group����, append�s��id�ires
            # len(res[hash[i]])==i�N�O�ΨӧP�_res��size��i��group���F�S
            if i not in hash or len(res[hash[i]])==i:
                hash[i] = len(res)
                res.append([id])
            # �bres[hash[i]]������, �~��Ni��id append�i�h
            else:
                res[hash[i]].append(id)
        return res
        
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
