<<<<<<< HEAD
/*
 * @lc app=leetcode id=1108 lang=c
 *
 * [1108] Defanging an IP Address
 */

// @lc code=start

// By index and sprintf, time: O(n), space: O(1)
// python�ઽ��replace, c�S��
// �n������.��index�O�U��, �A������
char* defangIPaddr(char* address) {
    int len = strlen(address);
    int idx = 0;
    // res�ΨӦs���ܫ᪺�r��, �]��c�y���L�kinplace����
    // �ŧi�Ŷ�len+7����]�O, ip�`�@�|��3��"."", �o�˦h�T��[]�@6
    // �٭n�h�@�ӪŶ���\0 
    char* res = (char*)malloc(sizeof(char)*(len+7));
    for(int i=0;i<len;i++) {
        if(address[i]=='.') {
            // sprintf�O�N�榡�Ʀr��o�e��ؼЦr��, �ؼЦr��b�e, �榡�Ʀr��b�ŧi�榡���᭱
            // �ҥH�U���o��N�O�N[.]�o�e��res�o�Ӧr��+idx����m
            // ��^���O�r���`��, �]�N�O�ثeres���̷s��m
            idx += sprintf(res+idx, "%s", "[.]");
        } 
        else {
            res[idx++] = address[i];
        }
    }
    res[idx] = '\0';
    return res;
}

// @lc code=end

=======
/*
 * @lc app=leetcode id=1108 lang=c
 *
 * [1108] Defanging an IP Address
 */

// @lc code=start

// By index and sprintf, time: O(n), space: O(1)
// python�ઽ��replace, c�S��
// �n������.��index�O�U��, �A������
char* defangIPaddr(char* address) {
    int len = strlen(address);
    int idx = 0;
    // res�ΨӦs���ܫ᪺�r��, �]��c�y���L�kinplace����
    // �ŧi�Ŷ�len+7����]�O, ip�`�@�|��3��"."", �o�˦h�T��[]�@6
    // �٭n�h�@�ӪŶ���\0 
    char* res = (char*)malloc(sizeof(char)*(len+7));
    for(int i=0;i<len;i++) {
        if(address[i]=='.') {
            // sprintf�O�N�榡�Ʀr��o�e��ؼЦr��, �ؼЦr��b�e, �榡�Ʀr��b�ŧi�榡���᭱
            // �ҥH�U���o��N�O�N[.]�o�e��res�o�Ӧr��+idx����m
            // ��^���O�r���`��, �]�N�O�ثeres���̷s��m
            idx += sprintf(res+idx, "%s", "[.]");
        } 
        else {
            res[idx++] = address[i];
        }
    }
    res[idx] = '\0';
    return res;
}

// @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
