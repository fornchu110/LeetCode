<<<<<<< HEAD
/*
 * @lc app=leetcode id=70 lang=c
 *
 * [70] Climbing Stairs
 */

// @lc code=start
// By DP
//等同f(n) = f(n-1)+f(n-2)
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

=======
/*
 * @lc app=leetcode id=70 lang=c
 *
 * [70] Climbing Stairs
 */

// @lc code=start
// By DP
//等同f(n) = f(n-1)+f(n-2)
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

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
