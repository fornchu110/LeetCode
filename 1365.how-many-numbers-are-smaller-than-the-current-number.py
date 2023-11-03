<<<<<<< HEAD
#
# @lc app=leetcode id=1365 lang=python3
#
# [1365] How Many Numbers Are Smaller Than the Current Number
#

# @lc code=start

# By counting sort, time: O(n+k), space: O(k), k�Oinput�Ȱ�j�p
# �O��counting sort�O�u�ʱƧǫܧ�, �����Ŷ�, �]���ھڭȰ�M�w
# counting sort�N�Oindex array���Q�k, ��ȥ�����index
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # �D�ص�input�̦h101�Ӥ���, 101�]�N�O�Ȱ�j�pk
        arr = [0]*101
        res = list()
        # �barr������0~101����nums���X�{������
        # �ѩ�arr��index�Onums����������, �ҥH��ꨫ�Xarr�N�|�Ѥp�ܤj���Xnums
        for i in nums:
            arr[i] += 1 
        lessthan = list()  
        # �N�Oarr���U�Ӥ���(index)��U����
        temp = 0 
        # ���Xarr��temp���[�`�N���
        # �Ѥp�ܤj�ݤ��U������p���������X�{���ƩM, �å[�Jlessthan����
        # �ҥHlessthan���j�p�Marr�@��, ���O[0]*101
        for i in arr:
            # temp+=i�bappend����, �ҥH���|����U�����ۤv���X�{����
            # �Y�n��<=���ƴN��temp+=i���append�e��
            lessthan.append(temp)
            temp += i
        # �Hnums���������@��index�d��lessthan�Y�i���D�p��ۤv�������ƶq
        for i in nums:  
            res.append(lessthan[i])
        return res

# By sort and hash, time: O(n*log(n)), space: O(n)
# ���I�b��ƧǹL�᪺nums��, �C�Ӥ����Ĥ@���X�{��index�Y�O�p��L�������ƶq
# class Solution:
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#         res = list()
#         hash = dict()
#         # nums.sort()�����Nnums���Ƨ�, sorted(nums)�h�^�Ǥ@�ӷs��list
#         # �b�o��ѩ�ݭn�Ӷ���return, �ҥH�ݭn�Τ@��sort�L���slist
#         arr = sorted(nums)
#         # �̧Ǩ��X�ƧǹL��arr
#         # ���C�����Ĥ@���X�{�ɪ�index�N�O�p��Ӥ����������ƶq
#         for i in range(len(arr)):
#             if arr[i] not in hash:
#                 hash[arr[i]] = i
#         # �w�g��hash�����p��U�������ƶq, ��nums�����Ǩ��X�@�M�[�Jres
#         for i in nums:
#             res.append(hash[i])
#         return res
        
# @lc code=end

=======
#
# @lc app=leetcode id=1365 lang=python3
#
# [1365] How Many Numbers Are Smaller Than the Current Number
#

# @lc code=start

# By counting sort, time: O(n+k), space: O(k), k�Oinput�Ȱ�j�p
# �O��counting sort�O�u�ʱƧǫܧ�, �����Ŷ�, �]���ھڭȰ�M�w
# counting sort�N�Oindex array���Q�k, ��ȥ�����index
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # �D�ص�input�̦h101�Ӥ���, 101�]�N�O�Ȱ�j�pk
        arr = [0]*101
        res = list()
        # �barr������0~101����nums���X�{������
        # �ѩ�arr��index�Onums����������, �ҥH��ꨫ�Xarr�N�|�Ѥp�ܤj���Xnums
        for i in nums:
            arr[i] += 1 
        lessthan = list()  
        # �N�Oarr���U�Ӥ���(index)��U����
        temp = 0 
        # ���Xarr��temp���[�`�N���
        # �Ѥp�ܤj�ݤ��U������p���������X�{���ƩM, �å[�Jlessthan����
        # �ҥHlessthan���j�p�Marr�@��, ���O[0]*101
        for i in arr:
            # temp+=i�bappend����, �ҥH���|����U�����ۤv���X�{����
            # �Y�n��<=���ƴN��temp+=i���append�e��
            lessthan.append(temp)
            temp += i
        # �Hnums���������@��index�d��lessthan�Y�i���D�p��ۤv�������ƶq
        for i in nums:  
            res.append(lessthan[i])
        return res

# By sort and hash, time: O(n*log(n)), space: O(n)
# ���I�b��ƧǹL�᪺nums��, �C�Ӥ����Ĥ@���X�{��index�Y�O�p��L�������ƶq
# class Solution:
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#         res = list()
#         hash = dict()
#         # nums.sort()�����Nnums���Ƨ�, sorted(nums)�h�^�Ǥ@�ӷs��list
#         # �b�o��ѩ�ݭn�Ӷ���return, �ҥH�ݭn�Τ@��sort�L���slist
#         arr = sorted(nums)
#         # �̧Ǩ��X�ƧǹL��arr
#         # ���C�����Ĥ@���X�{�ɪ�index�N�O�p��Ӥ����������ƶq
#         for i in range(len(arr)):
#             if arr[i] not in hash:
#                 hash[arr[i]] = i
#         # �w�g��hash�����p��U�������ƶq, ��nums�����Ǩ��X�@�M�[�Jres
#         for i in nums:
#             res.append(hash[i])
#         return res
        
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
