/*
 * @lc app=leetcode id=1678 lang=c
 *
 * [1678] Goal Parser Interpretation
 */

// @lc code=start

// By for loop and sprintf, time: O(n), space: O(1)
// ���Xcommand��̷Ӧr�����e��X���P�r���res�W
// �Q��sprintf�ܭ��n, �O�b#include <stdio.h>�̭�
// �O�osprintf��^�ȩM�Q��+=��^�ȱo��s��index�Ӱ��B�z
char* interpret(char* command) {
    // strlen�^�ǭȤ��|�]�t\0, �ҥH�ݰ_�ӴX�Ӧr���N�h��
    int len = strlen(command);
    //�`�Nc�y���ΰʺA�O����ŧi�r��size�|+1�O�]���d��\0
    char* res = (char*)malloc(sizeof(char)*(len+1));
    int pos = 0;
    // �}�l���Xcommand
    for (int i=0;i<len;i++) {
        // G���ܤ��|�ܰ�, �ݨ�G��XG
        if(command[i]=='G') {
            // c�y����sprintf���榡�Ʀr���X, �N�ؼЮ榡�M���e��X��str�W
            // printf��X��ù��W, sprintf��X��ؼЦr��W
            // �bpos�o��index����m(�]�N�Ores+pos)��X���spos��
            // �^�ǭȬO�ק諸�r�żƶq, �ҥH�[�W�^�ǭȴN�O�U����index
            // Ex: �bindex1���a���X2��char, �U���N�n�qindex3�~��
            pos += sprintf(res+pos, "%s", "G");
        }
        // �P�z, �u�O�ݨ�"("�|����ص��G, �������W")"�άO���W"al)"
        else if(command[i]=='(') {
            if(command[i+1]==')') {
                pos += sprintf(res+pos, "%s", "o");
            }
            else {
                pos += sprintf(res+pos, "%s", "al");
            }
        }
    }
    return res;
}

// @lc code=end

