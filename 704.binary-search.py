<<<<<<< HEAD
#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
# ���}�Cnums�M�ؼ�target, �bnums���j�M��target return index, �j�M����return -1

# By binary search, time: O(nlogn), space: O(1)
# �򥻪��G���j�M�k, �`�N�d��O[�U��, �W��)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        # �]�O[�U��, �W��), �ҥHright�n�O�W��+1, �ӤU�ɤW�ɽd��N�Onums��index
        right = len(nums)
        # ���i��left==right, �]��left==right��[left, right)�o�϶����s�b
        while left<right:
            # python���|����, ���������קK
            mid = (right-left)//2+left
            # ���target�^��index
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right = mid
            else:
                left = mid+1
        # �p�G�䥪�۪�, �hreturn left
        return -1
        
# @lc code=end

=======
#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
# ���}�Cnums�M�ؼ�target, �bnums���j�M��target return index, �j�M����return -1

# By binary search, time: O(nlogn), space: O(1)
# �򥻪��G���j�M�k, �`�N�d��O[�U��, �W��)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        # �]�O[�U��, �W��), �ҥHright�n�O�W��+1, �ӤU�ɤW�ɽd��N�Onums��index
        right = len(nums)
        # ���i��left==right, �]��left==right��[left, right)�o�϶����s�b
        while left<right:
            # python���|����, ���������קK
            mid = (right-left)//2+left
            # ���target�^��index
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right = mid
            else:
                left = mid+1
        # �p�G�䥪�۪�, �hreturn left
        return -1
        
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
