/*
 * @lc app=leetcode id=94 lang=c
 *
 * [94] Binary Tree Inorder Traversal
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
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

//By recursive
// resSize�O���F���D��U��J��node�ө�bres������index
void inorder(struct TreeNode* root, int* res, int* resSize) {
    //�פ����, �Dnode�ɨS��k���j, ����return
    if (!root) {
        return;
    }
    //inoder���ǬO:��->��->�k, �����|���l��
    //���l�𰵻��j
    inorder(root->left, res, resSize);
    //���l�𻼰j����, �Nroot��J�ç�reSize+1(���P�U��root�n��J����m)
    res[(*resSize)++] = root->val;
    //���l��Mroot�������~���k�l��
    inorder(root->right, res, resSize);
}

int* inorderTraversal(struct TreeNode* root, int* returnSize) {
    //��tree�Ҧ�node�����j, �C�����H��U��node��root
    int* res = malloc(sizeof(int)*100);
    //�@�}�l�@�w�O�qres[0]�}�l��Jnode, �ҥHreturnSize = 0
    *returnSize = 0;
    inorder(root, res, returnSize);
    //��������Ҧ�node��inorder�l�ܫ�, resSize�K�OreturnSize=node�`��
    return res;
}

// @lc code=end

