<<<<<<< HEAD
#
# @lc app=leetcode id=1614 lang=python3
#
# [1614] Maximum Nesting Depth of the Parentheses
#

# @lc code=start
# ���r��s, ��X�A�����̤j�h��, �D�ثO�ҬA���@�w����, ���|�X�{"(()"

# By stack, time: O(n), space: O(1)
# �C�J��@��'('�h�@�h, �J��@��')'�֤@�h
# �ҥH��J��'('����P���v�h�ƭ��Ӹ��h, ��j���O����
class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        cnt = 0
        for i in s:
            if i=='(':
                cnt += 1
                res = max(res, cnt)
            elif i==')':
                cnt -= 1
        return res

# @lc code=end

=======
#
# @lc app=leetcode id=1614 lang=python3
#
# [1614] Maximum Nesting Depth of the Parentheses
#

# @lc code=start
# ���r��s, ��X�A�����̤j�h��, �D�ثO�ҬA���@�w����, ���|�X�{"(()"

# By stack, time: O(n), space: O(1)
# �C�J��@��'('�h�@�h, �J��@��')'�֤@�h
# �ҥH��J��'('����P���v�h�ƭ��Ӹ��h, ��j���O����
class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        cnt = 0
        for i in s:
            if i=='(':
                cnt += 1
                res = max(res, cnt)
            elif i==')':
                cnt -= 1
        return res

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
