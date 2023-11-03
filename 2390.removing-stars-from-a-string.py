<<<<<<< HEAD
#
# @lc app=leetcode id=2390 lang=python3
#
# [2390] Removing Stars From a String
#

# @lc code=start
# ���@�r��s, ���X�r��ɹJ��'*'�n�N����@�Ӧr�����h, return�B�z�����r��

# By stack, time: O(n), space: O(n)


class Solution:
    def removeStars(self, s: str) -> str:
        # �Q��list����stack     
        res = []
        # �̧ǱN�r��push�i
        for i in s:
            if ord('a')<=ord(i)<=ord('z'):
                res.append(i)
            # �J��'*'�N�N���ݪ��r��pop�X��
            elif i=='*':
                res.pop()
        # �̫��"".join(res)�ഫ�^�r��
        res = "".join(res)
        return res
        
# @lc code=end

=======
#
# @lc app=leetcode id=2390 lang=python3
#
# [2390] Removing Stars From a String
#

# @lc code=start
# ���@�r��s, ���X�r��ɹJ��'*'�n�N����@�Ӧr�����h, return�B�z�����r��

# By stack, time: O(n), space: O(n)


class Solution:
    def removeStars(self, s: str) -> str:
        # �Q��list����stack     
        res = []
        # �̧ǱN�r��push�i
        for i in s:
            if ord('a')<=ord(i)<=ord('z'):
                res.append(i)
            # �J��'*'�N�N���ݪ��r��pop�X��
            elif i=='*':
                res.pop()
        # �̫��"".join(res)�ഫ�^�r��
        res = "".join(res)
        return res
        
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
