<<<<<<< HEAD
#
# @lc app=leetcode id=2103 lang=python3
#
# [2103] Rings and Rods
#

# @lc code=start
# ���@��rings�W���C��Ӽg�񤰻��C�⪺ring�b�X��rod
# �̫�return���X��rod�W����R�BG�BB�T��ring

# By bitwise, time: O(n+k), space: O(k)
# ���M�Oindex array, �����ݭn�T��array, �@��array�鷺�e������bitwise�ާ@�Y�i
# Ex: �G�i��111�N��R�BG�BB����, 101�N��S��G, 001�N��u��R
class Solution:
    def countPoints(self, rings: str) -> int:
        n = len(rings)
        # �����U��rod�������C��ring��index array
        status = [0] * 10   
        for i in range(0, n, 2):
            # python��int()�|�۰ʧ�r���নint�ӫDascii, �ҥH�]���ઽ����r�����B��
            idx = int(rings[i+1])
            # ����3�T��array����], ��2�i�쪺�Ӧ�Ƭ���
            # R�b��0��, G�b��1��, B�b��2��
            if rings[i] == 'R':
                status[idx] |= 1
            elif rings[i] == 'G':
                status[idx] |= 2
            else:
                status[idx] |= 4
        res = 0
        for i in status:
            # �G�i��111���P��̶i��7
            if i == 7:
                res += 1
        return res

# By index array and ord(), time: O(n+k), space: O(3*k), n = len(rings), k = rod�ƶq   
# ��index array���覡�O���U�C��ring��b����rod, �̫�ݨ���index�P�ɦb�Tarray�W��1
# class Solution:
#     def countPoints(self, rings: str) -> int:
#         res = 0
#         r = [0]*10
#         g = [0]*10
#         b = [0]*10
#         n = len(rings)
#         for i in range(1, n, 2):
#             if rings[i-1]=='R':
#                 r[ord(rings[i])-ord('0')] += 1
#             if rings[i-1]=='G':
#                 g[ord(rings[i])-ord('0')] += 1
#             if rings[i-1]=='B':
#                 b[ord(rings[i])-ord('0')] += 1
#         for i, j , k in zip(r, g ,b):
#             if i!=0 and j!=0 and k!=0:
#                 res += 1
#         return res

# @lc code=end

=======
#
# @lc app=leetcode id=2103 lang=python3
#
# [2103] Rings and Rods
#

# @lc code=start
# ���@��rings�W���C��Ӽg�񤰻��C�⪺ring�b�X��rod
# �̫�return���X��rod�W����R�BG�BB�T��ring

# By bitwise, time: O(n+k), space: O(k)
# ���M�Oindex array, �����ݭn�T��array, �@��array�鷺�e������bitwise�ާ@�Y�i
# Ex: �G�i��111�N��R�BG�BB����, 101�N��S��G, 001�N��u��R
class Solution:
    def countPoints(self, rings: str) -> int:
        n = len(rings)
        # �����U��rod�������C��ring��index array
        status = [0] * 10   
        for i in range(0, n, 2):
            # python��int()�|�۰ʧ�r���নint�ӫDascii, �ҥH�]���ઽ����r�����B��
            idx = int(rings[i+1])
            # ����3�T��array����], ��2�i�쪺�Ӧ�Ƭ���
            # R�b��0��, G�b��1��, B�b��2��
            if rings[i] == 'R':
                status[idx] |= 1
            elif rings[i] == 'G':
                status[idx] |= 2
            else:
                status[idx] |= 4
        res = 0
        for i in status:
            # �G�i��111���P��̶i��7
            if i == 7:
                res += 1
        return res

# By index array and ord(), time: O(n+k), space: O(3*k), n = len(rings), k = rod�ƶq   
# ��index array���覡�O���U�C��ring��b����rod, �̫�ݨ���index�P�ɦb�Tarray�W��1
# class Solution:
#     def countPoints(self, rings: str) -> int:
#         res = 0
#         r = [0]*10
#         g = [0]*10
#         b = [0]*10
#         n = len(rings)
#         for i in range(1, n, 2):
#             if rings[i-1]=='R':
#                 r[ord(rings[i])-ord('0')] += 1
#             if rings[i-1]=='G':
#                 g[ord(rings[i])-ord('0')] += 1
#             if rings[i-1]=='B':
#                 b[ord(rings[i])-ord('0')] += 1
#         for i, j , k in zip(r, g ,b):
#             if i!=0 and j!=0 and k!=0:
#                 res += 1
#         return res

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
