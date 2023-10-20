#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
# ���@�Ѧr���զ����G���}�Cboard�M�@�r��word, �P�_word�O�_�s�bboard��return ture false
# word�s�bboard���N��O�i�H�b�G���}�C�����@�ӳs����|�s��word

# By backtracking recursive, time: O(MN*3^L), space: O(MN), �䤤M�BN��board��row�Bcol, L��len(word)
# time = O(MN*3^L)�O�]��, �����ܤ֭n�@�@���Xboard���Ҧ�����, �A�ӭn��C�Ӥ����̦h�|���T�Ӭ۾F�����n�P�_
# space = O(MN)�O�]���B�~�ΤFvisited�o��set, �קK���X��ۦP��m

# �n�إߤ@�Ө禡check, �N��q(i, j)�X�o��, ��_���U���word[k:]�r��, k���e�N�O�w�g���X�쪺word���e
# �ҥH���bcheck���L�{���u�n�J��board(i, j)������k�N��false
# �p�G���X��word���M�ۦP�N��true
# ��board(i, j)����k�B���X��������, �h�q(i, j)�۾F���T�Ӥ������_�I��check��s[k+1:]
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # ���O�N��k�B���B�U�B�W�|�ز��ʾާ@
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # �Ѽ�i�Bj�Orow�Bcol, k�O�ثe�n�j�M���r��
        def check(i: int, j: int, k: int) -> bool:
            # �פ���� �䥢�ѩM�w�䧹
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            # ���X�L����m�O���bvisited��, ��list���P���O��append
            visited.add((i, j))
            # ��l�Ƭ��S���, check���|return result
            result = False
            # ��C�Ӥ������|�إi�઺����
            for di, dj in directions:
                # �������ʫ᪺�y��
                newi, newj = i+di, j+dj
                # �`�N����out of range, �ҥH�b�d�򤺤~�వ
                if 0<=newi<len(board) and 0<=newj<len(board[0]):
                    # �s���ʬO�S���X�L���y��, �N���|�^�Y
                    if (newi, newj) not in visited:
                        # �~�򩹤U��, check(newi, newj, k+1)��True, �N��o�Ӥ�V�i�H���X��word[k+1:]
                        if check(newi, newj, k+1):
                            # �Ө���o�̦P�ɤ]�N��(i, j)��k, �ҥH���W��return���q(i, j)�ਫ�X��word[k:]
                            result = True
                            break
            # (i, j)�o�Ӧ�m���X�����F, �]�N�O�w�g���word[k:]�άO�T�w�T�ز��ʳ��L�k��Xword[k:]�N�R��(i, j)
            # ���m�ت��O����L��m���_�I���X�ϥ�, �쥻visited�u�O���F�C����U�Ӧ�m���X��, ���n�^�Y��
            visited.remove((i, j))
            return result
        
        # board��row�Bcol
        h, w = len(board), len(board[0])
        # ��m�W�@�L�G�ҥH�i�H��set(), ���I�O�i�H��add�Bremove�٦�in
        # ���ι�list()�@�˪`�N���ƩMindex
        visited = set()
        # ��board�Ҧ�������check
        for i in range(h):
            for j in range(w):
                # check(i, j, 0)��True�N��b(i, j)�ਫ�X�Xword[0:], �]�N�O���word
                if check(i, j, 0):
                    return True    
        return False
    
# @lc code=end

