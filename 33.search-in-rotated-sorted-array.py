#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
# ���@��rotated�L�����ǼƦC, �n�D��Xtarget�O�_�b�ƦC��, �b����return index�_�h-1
# �W�w�n�btime: O(log(n))�ѨM, �Q��G���j�M

# By binary search, time: O(log(n)), space: O(1)
# �G���j�M�k, �o�D�@�˥i�H��[l, r)�����k�}���϶���
# �o�D���Q�k�O, ����mid����M�k�����O��զ���, �A��target�O�_����ը���ӨM�w�϶�
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # not nums�ΨӧP�_nums�O�_����, �]�N�O[], ���D�ػ��ܤ֦��@�Ӥ����ҥH���ݭn
        # if not nums:
        #     return -1
        l, r = 0, len(nums)-1
        # while����N�O�ϥΪ��j�M�϶�, �ڿ��[l, r)�����k�}�϶�
        while l<r:
            mid = l+(r-l)//2
            # ��mid==target������^
            if nums[mid]==target:
                return mid
            # �Ymid��nums[len(nums)-1]�٤p, �N��k��O��զ���
            if nums[mid]<nums[len(nums)-1]:
                # �k��O��զ��ǩҥH�ઽ���P�_target�O�_�b�k��
                # �`�Ntarget���i��==nums[mid], �_�h�e���w�greturn
                if nums[mid]<target<=nums[len(nums)-1]:
                    # target�b�k�䨺�Y�p�d���l�]�w��mid+1
                    l = mid+1
                # target�b����, �Ӭݪ��O[l, r)�ҥHr = mid
                else:
                    r = mid
            # �Ymid>=nums[len(nums)-1], �N����O��զ���
            else:
                # �����P�_target�O�_�����
                # �@�˪`�Ntarget���i��==nums[mid]
                if nums[0]<=target<nums[mid]:
                    # �����, �Y�p�d���r�]�w��mid
                    r = mid
                # ���k��, �Y�pl���d��
                else:
                    l = mid+1
        # �]�ڬO��while l<r, �ҥH��l==r�]�N�O�d�򤺳ѤU�@�Ӥ����ɷ|���X
        # �n�P�_�ѤU���o�Ӥ����O�_==target, ��nums[l]�Mnums[r]���@��
        if nums[l]==target:
            return l
        return -1
        
# @lc code=end

