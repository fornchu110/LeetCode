/*
 * @lc app=leetcode id=1678 lang=c
 *
 * [1678] Goal Parser Interpretation
 */

// @lc code=start

// By for loop and sprintf, time: O(n), space: O(1)
// 走訪command後依照字元內容輸出不同字串到res上
// 利用sprintf很重要, 是在#include <stdio.h>裡面
// 記得sprintf返回值和利用+=返回值得到新的index來做處理
char* interpret(char* command) {
    // strlen回傳值不會包含\0, 所以看起來幾個字元就多長
    int len = strlen(command);
    //注意c語言用動態記憶體宣告字串size會+1是因為留給\0
    char* res = (char*)malloc(sizeof(char)*(len+1));
    int pos = 0;
    // 開始走訪command
    for (int i=0;i<len;i++) {
        // G的話不會變動, 看到G輸出G
        if(command[i]=='G') {
            // c語言用sprintf做格式化字串輸出, 將目標格式和內容輸出到str上
            // printf輸出到螢幕上, sprintf輸出到目標字串上
            // 在pos這個index的位置(也就是res+pos)輸出後更新pos值
            // 回傳值是修改的字符數量, 所以加上回傳值就是下次的index
            // Ex: 在index1的地方輸出2個char, 下次就要從index3繼續
            pos += sprintf(res+pos, "%s", "G");
        }
        // 同理, 只是看到"("會有兩種結果, 直接接上")"或是接上"al)"
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

