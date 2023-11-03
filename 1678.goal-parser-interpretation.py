<<<<<<< HEAD
#
# @lc app=leetcode id=1678 lang=python3
#
# [1678] Goal Parser Interpretation
#

# @lc code=start
# By for loop, time: O(n), space: O(1), �u�ݭn�@�����X
# �O�o��"".join(list)���覡�N�U�������r�ꪺlist�ഫ���@��str
class Solution:
    def interpret(self, command: str) -> str:
        res = list()
        #enumerate�Ϊk�e���Oindex�᭱�Ostr[index], �]�N�Ocommand[i]
        for i, c in enumerate(command):
            if c == 'G':
                res.append(c)
            elif c == '(':
                # �U�����q���@��g�k
                # res.append('o' if command[i + 1] == ')' else 'al')
                if command[i+1]==")":
                    res.append("o")
                else:
                    res.append("al")
        # join�Nres�o��list����str��''(�]�N�O�ť�)�s��, �����@���str
        # �]�N�Opython���Nlist�ഫ��str���Ϊk
        return ''.join(res)

# By replace, time: O(n), space: O(1), �]res�O��^�Ȥ���b������
# �Q��python��replace�\�వ�r�����
# class Solution:
#     def interpret(self, command: str) -> str:
#         # str.replace("�n�Q��諸�¦r��", "�Q���᪺�r��")
#         # �i�H�N�@����r�ꤤ���@�������ק�, �^�ǧ粒���s�r��
#         # �Y�S�����^�ǭ�, �¦r�ꤣ�|���ק�
#         # ��������res.command.replace("(al)", "al").replace("()", "o")�|�����ɶ�
#         res = command.replace("(al)", "al")
#         res = res.replace("()", "o")
#         return res

# @lc code=end

=======
#
# @lc app=leetcode id=1678 lang=python3
#
# [1678] Goal Parser Interpretation
#

# @lc code=start
# By for loop, time: O(n), space: O(1), �u�ݭn�@�����X
# �O�o��"".join(list)���覡�N�U�������r�ꪺlist�ഫ���@��str
class Solution:
    def interpret(self, command: str) -> str:
        res = list()
        #enumerate�Ϊk�e���Oindex�᭱�Ostr[index], �]�N�Ocommand[i]
        for i, c in enumerate(command):
            if c == 'G':
                res.append(c)
            elif c == '(':
                # �U�����q���@��g�k
                # res.append('o' if command[i + 1] == ')' else 'al')
                if command[i+1]==")":
                    res.append("o")
                else:
                    res.append("al")
        # join�Nres�o��list����str��''(�]�N�O�ť�)�s��, �����@���str
        # �]�N�Opython���Nlist�ഫ��str���Ϊk
        return ''.join(res)

# By replace, time: O(n), space: O(1), �]res�O��^�Ȥ���b������
# �Q��python��replace�\�వ�r�����
# class Solution:
#     def interpret(self, command: str) -> str:
#         # str.replace("�n�Q��諸�¦r��", "�Q���᪺�r��")
#         # �i�H�N�@����r�ꤤ���@�������ק�, �^�ǧ粒���s�r��
#         # �Y�S�����^�ǭ�, �¦r�ꤣ�|���ק�
#         # ��������res.command.replace("(al)", "al").replace("()", "o")�|�����ɶ�
#         res = command.replace("(al)", "al")
#         res = res.replace("()", "o")
#         return res

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
