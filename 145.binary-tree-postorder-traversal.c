/*
 * @lc app=leetcode id=145 lang=c
 *
 * [145] Binary Tree Postorder Traversal
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
void postorder(struct TreeNode*root, int* res, int* resSize) {
    //�פ����, ��Dnode�ɤ��λ��j
    if(root==NULL) {
        return;
    }
    //��ǰl��:��->�k->��
    postorder(root->left, res, resSize);
    postorder(root->right, res, resSize);
    //resSize�O����, *resSize�~�Oindex
    //�N����val��Jres[*resSize], �åB�N*resSize++
    res[(*resSize)++] = root->val;
    return;
}

int* postorderTraversal(struct TreeNode* root, int* returnSize){
    //�ʺA�ŧi�^�ǫ�ǰl�ܵ��G��res�}�C
    int* res = (int*)malloc(100*sizeof(int));
    //returnSize�O����, ��l��*resturnSize�@���Nnode��Jres��index
    *returnSize = 0;
    //�qroot�}�l��Ҧ�node���j����ǰl��
    postorder(root, res, returnSize);
    //�����Ҧ����j, �^�ǵ��G
    return res;
}
// @lc code=end

