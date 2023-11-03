<<<<<<< HEAD
#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
# ���@m*n���G���}�C, �n�D�ӵۥ��W->�k�W->�k�U->���U->���W�o�����۪����Ǩ��X, return���X�ɪ�������

# By simulation recursive, time: O(m*n), space: O(1), res����Ŷ�
# �@�ˬO�N���matrix���X�@��
# �Q��k���X�̥~��, �U�@���N��̥~�鮳���A�Q��k���X�̥~��...
# �·��I�A��̫�@����, �w�g���O�@�ӥi�H¶�骺�x�}, ���@��N�O�@�C
# ��ڤW�|��@�������, �o�D�]�i�H�g���l�禡��recursive, ���o�طQ�k�o���for loop�]���o��
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        res = []
        # �A�ѤU�̫�@�h�e, �|�`��min(m, n)//2�����ƨ��X�~��
        for turn in range(min(m, n)//2):
            for i in range(turn, n-turn):
                res.append(matrix[turn][i])
            for i in range(turn+1, m-turn):
                res.append(matrix[i][n-turn-1])
            for i in range(n-turn-2, turn-1, -1):
                res.append(matrix[m-turn-1][i])
            for i in range(m-turn-2, turn, -1):
                res.append(matrix[i][turn])

        if min(m, n)%2 == 1:
            # ���|�`��min(m, n)//2��
            turn = min(m, n)//2
            # �A�Ӯھ�m�Mn���Ӥj�M�w�̫�@���O���@��row�٬O�@��col
            # �Ym<n�N��col����h, �|�ѤU�@��row, ��m=n�N�O�ѤU�@�Ӥ���
            if m<=n:
                # ���Xrow��row�ȩT�wcol�ܤ�
                for i in range(turn, n-turn):
                    res.append(matrix[turn][i])
            # m>n�P�z, �ѤU�@��col
            else:
                # ���Xcol, col�ȩT�wrow�ܤ�
                for i in range(turn, m-turn):
                    res.append(matrix[i][n-turn-1])
        return res
    
# �x��t�~��o�Ӥ�k���g�k
# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         if not matrix or not matrix[0]:
#             return list()
        
#         rows, columns = len(matrix), len(matrix[0])
#         order = list()
#         left, right, top, bottom = 0, columns - 1, 0, rows - 1
#         while left <= right and top <= bottom:
#             for column in range(left, right + 1):
#                 order.append(matrix[top][column])
#             for row in range(top + 1, bottom + 1):
#                 order.append(matrix[row][right])
#             if left < right and top < bottom:
#                 for column in range(right - 1, left, -1):
#                     order.append(matrix[bottom][column])
#                 for row in range(bottom, top, -1):
#                     order.append(matrix[row][left])
#             left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
#         return order

# By simulation, time: O(m*n), space: O(m*n)
# �u�ƪŶ������ת��覡�O�Χ�飼�X�L��������, �o�D�����b-100~100��, �ҥH�u�n���X��[�W201, �A�P�_�O�_>200�Y�i���D�O�_���X�L
# �o�˰�����space�N�OO(1)
# ���X���ǬO�k->�U->��->�W->�k, �J�쩳�ɷ|��飼�X����
# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         if not matrix or not matrix[0]:
#             return list() 
#         rows, columns = len(matrix), len(matrix[0])
#         # ��visited���x�s���Ǥ����Q���X�L
#         visited = [[False]*columns for i in range(rows)]
#         total = rows*columns
#         order = [0]*total
#         # �N��k �U �� �W�|�ب��X�Ҧ�
#         directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
#         row, column = 0, 0
#         directionIndex = 0
#         for i in range(total):
#             order[i] = matrix[row][column]
#             visited[row][column] = True
#             nextRow, nextColumn = row+directions[directionIndex][0], column+directions[directionIndex][1]
#             if not (0 <= nextRow<rows and 0<=nextColumn<columns and not visited[nextRow][nextColumn]):
#                 directionIndex = (directionIndex + 1)%4
#             row += directions[directionIndex][0]
#             column += directions[directionIndex][1]
#         return order

=======
#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
# ���@m*n���G���}�C, �n�D�ӵۥ��W->�k�W->�k�U->���U->���W�o�����۪����Ǩ��X, return���X�ɪ�������

# By simulation recursive, time: O(m*n), space: O(1), res����Ŷ�
# �@�ˬO�N���matrix���X�@��
# �Q��k���X�̥~��, �U�@���N��̥~�鮳���A�Q��k���X�̥~��...
# �·��I�A��̫�@����, �w�g���O�@�ӥi�H¶�骺�x�}, ���@��N�O�@�C
# ��ڤW�|��@�������, �o�D�]�i�H�g���l�禡��recursive, ���o�طQ�k�o���for loop�]���o��
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        res = []
        # �A�ѤU�̫�@�h�e, �|�`��min(m, n)//2�����ƨ��X�~��
        for turn in range(min(m, n)//2):
            for i in range(turn, n-turn):
                res.append(matrix[turn][i])
            for i in range(turn+1, m-turn):
                res.append(matrix[i][n-turn-1])
            for i in range(n-turn-2, turn-1, -1):
                res.append(matrix[m-turn-1][i])
            for i in range(m-turn-2, turn, -1):
                res.append(matrix[i][turn])

        if min(m, n)%2 == 1:
            # ���|�`��min(m, n)//2��
            turn = min(m, n)//2
            # �A�Ӯھ�m�Mn���Ӥj�M�w�̫�@���O���@��row�٬O�@��col
            # �Ym<n�N��col����h, �|�ѤU�@��row, ��m=n�N�O�ѤU�@�Ӥ���
            if m<=n:
                # ���Xrow��row�ȩT�wcol�ܤ�
                for i in range(turn, n-turn):
                    res.append(matrix[turn][i])
            # m>n�P�z, �ѤU�@��col
            else:
                # ���Xcol, col�ȩT�wrow�ܤ�
                for i in range(turn, m-turn):
                    res.append(matrix[i][n-turn-1])
        return res
    
# �x��t�~��o�Ӥ�k���g�k
# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         if not matrix or not matrix[0]:
#             return list()
        
#         rows, columns = len(matrix), len(matrix[0])
#         order = list()
#         left, right, top, bottom = 0, columns - 1, 0, rows - 1
#         while left <= right and top <= bottom:
#             for column in range(left, right + 1):
#                 order.append(matrix[top][column])
#             for row in range(top + 1, bottom + 1):
#                 order.append(matrix[row][right])
#             if left < right and top < bottom:
#                 for column in range(right - 1, left, -1):
#                     order.append(matrix[bottom][column])
#                 for row in range(bottom, top, -1):
#                     order.append(matrix[row][left])
#             left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
#         return order

# By simulation, time: O(m*n), space: O(m*n)
# �u�ƪŶ������ת��覡�O�Χ�飼�X�L��������, �o�D�����b-100~100��, �ҥH�u�n���X��[�W201, �A�P�_�O�_>200�Y�i���D�O�_���X�L
# �o�˰�����space�N�OO(1)
# ���X���ǬO�k->�U->��->�W->�k, �J�쩳�ɷ|��飼�X����
# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         if not matrix or not matrix[0]:
#             return list() 
#         rows, columns = len(matrix), len(matrix[0])
#         # ��visited���x�s���Ǥ����Q���X�L
#         visited = [[False]*columns for i in range(rows)]
#         total = rows*columns
#         order = [0]*total
#         # �N��k �U �� �W�|�ب��X�Ҧ�
#         directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
#         row, column = 0, 0
#         directionIndex = 0
#         for i in range(total):
#             order[i] = matrix[row][column]
#             visited[row][column] = True
#             nextRow, nextColumn = row+directions[directionIndex][0], column+directions[directionIndex][1]
#             if not (0 <= nextRow<rows and 0<=nextColumn<columns and not visited[nextRow][nextColumn]):
#                 directionIndex = (directionIndex + 1)%4
#             row += directions[directionIndex][0]
#             column += directions[directionIndex][1]
#         return order

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
