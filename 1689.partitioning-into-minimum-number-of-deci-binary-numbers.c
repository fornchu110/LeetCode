/*
 * @lc app=leetcode id=1689 lang=c
 *
 * [1689] Partitioning Into Minimum Number Of Deci-Binary Numbers
 */

// @lc code=start
// 0��ascii�X�O48, �q�r��}�Y��m�}�l���, �̫�^�ǱNascii�ন���T�Ʀr
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

