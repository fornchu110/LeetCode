/*
 * @lc app=leetcode id=237 lang=c
 *
 * [237] Delete Node in a Linked List
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
// By in-place modify, time: O(1), space: O(1)
void deleteNode(struct ListNode* node) {
    //�`�N*node->next���P*(node->next), ���Ȥ�->�u���C����[�����
    //����(*node).next�]��next�O�@��pointer, *node�O�@��node���c����ӫD���Vnode��pointer, �⵲�c���۵�
    //�o�y���P�U��y���N��
    *node = *node->next; 
    //node->val = node->next->val;
    //node->next = node->next->next;
}

// @lc code=end

