/*
 * @lc app=leetcode id=70 lang=c
 *
 * [70] Climbing Stairs
 */

// @lc code=start
// By DP
//µ¥¦Pf(n) = f(n-1)+f(n-2)
int climbStairs(int n){
    int i; 
    int p = 0, q = 0, r = 1;
    for(i=0;i<n;i++) {
        p = q;
        q = r;
        r = p+q;
    }
    return r;
}

// @lc code=end

