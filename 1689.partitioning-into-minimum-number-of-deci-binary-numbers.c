/*
 * @lc app=leetcode id=1689 lang=c
 *
 * [1689] Partitioning Into Minimum Number Of Deci-Binary Numbers
 */

// @lc code=start
// 0的ascii碼是48, 從字串開頭位置開始比較, 最後回傳將ascii轉成正確數字
int minPartitions(char * n) {
    int max = 0, i;
    for(i=0;i<strlen(n);i++) {
        if(n[i]>max) {
            max = n[i];
        }
    }
    return max-48;
}
// @lc code=end

