/*
 * @lc app=leetcode id=226 lang=c
 *
 * [226] Invert Binary Tree
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* invertTree(struct TreeNode* root){
    //root指向了目前所在的node, 是指標
    //終止條件,當沒有走到非node時停止
    if(root==NULL) {
        return NULL;
    }
    //注意要交換的是整個node的結構, 不是只有value
    //建立指向左子點和右子點的指標
    struct TreeNode* left = invertTree(root->left);
    struct TreeNode* right = invertTree(root->right);
    //左右子點交換
    root->left = right;
    root->right = left;
    //回傳交換完左右子點的node
    //也就是說從最後一層子點將交換完的node回傳給其parent直到真正的root時結束
    return root;
}

// @lc code=end

