#
# @lc app=leetcode id=1773 lang=python3
#
# [1773] Count Items Matching a Rule
#

# @lc code=start
# By by index, time: O(n), space: O(1)
# items���̾�[type, color, name]�榡�s��T, �D�P���wkey�ۦPvalue��items�ƶq
# �i�H�ݨ�T�w��type�s�bindex 0, color�s�bindex 1, name�s�bindex 2, �H����index�h�P�_value
# c�y�����r��۵��N�O��strcmp()==0�P�_, �o�O�ۤv��c�y���o�g�k
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        cnt = 0
        for i in items:
            if ruleKey=="type":
                if i[0]==ruleValue:
                    cnt += 1
            elif ruleKey=="color":
                if i[1]==ruleValue:
                    cnt += 1
            else:
                if i[2]==ruleValue:
                    cnt += 1
        return cnt

# By hash, time: O(n), space: O(1)
# python�i�H�Χ�²��ֳt�����k
# class Solution:
#     def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
#         # ��ruleKey�����P��, �����Pindex
#         index = {"type": 0, "color": 1, "name": 2}[ruleKey]
#         # ��item��index��m�O�_�PruleValue�@��, ��sum()�[�`
#         # �]��==�O���L, �u�|��^1(True)��0(False), �ҥHsum()�N���P==���ƶq
#         return sum(item[index] == ruleValue for item in items)

# @lc code=end

