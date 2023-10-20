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
    //注意*node->next等同*(node->next), 取值比->優先低但比加減乘除高
    //不能(*node).next因為next是一個pointer, *node是一個node結構實體而非指向node的pointer, 兩結構不相等
    //這句等同下兩句的意思
    *node = *node->next; 
    //node->val = node->next->val;
    //node->next = node->next->next;
}

// @lc code=end

