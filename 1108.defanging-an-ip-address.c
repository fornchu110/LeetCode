<<<<<<< HEAD
/*
 * @lc app=leetcode id=1108 lang=c
 *
 * [1108] Defanging an IP Address
 */

// @lc code=start

// By index and sprintf, time: O(n), space: O(1)
// python能直接replace, c沒有
// 要直接把.的index記下來, 再做替換
char* defangIPaddr(char* address) {
    int len = strlen(address);
    int idx = 0;
    // res用來存改變後的字串, 因為c語言無法inplace替換
    // 宣告空間len+7的原因是, ip總共會有3個"."", 這樣多三對[]共6
    // 還要多一個空間放\0 
    char* res = (char*)malloc(sizeof(char)*(len+7));
    for(int i=0;i<len;i++) {
        if(address[i]=='.') {
            // sprintf是將格式化字串發送到目標字串, 目標字串在前, 格式化字串在宣告格式的後面
            // 所以下面這行就是將[.]發送到res這個字串+idx的位置
            // 返回直是字符總數, 也就是目前res的最新位置
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
// python能直接replace, c沒有
// 要直接把.的index記下來, 再做替換
char* defangIPaddr(char* address) {
    int len = strlen(address);
    int idx = 0;
    // res用來存改變後的字串, 因為c語言無法inplace替換
    // 宣告空間len+7的原因是, ip總共會有3個"."", 這樣多三對[]共6
    // 還要多一個空間放\0 
    char* res = (char*)malloc(sizeof(char)*(len+7));
    for(int i=0;i<len;i++) {
        if(address[i]=='.') {
            // sprintf是將格式化字串發送到目標字串, 目標字串在前, 格式化字串在宣告格式的後面
            // 所以下面這行就是將[.]發送到res這個字串+idx的位置
            // 返回直是字符總數, 也就是目前res的最新位置
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
