/*
 * @lc app=leetcode id=203 lang=c
 *
 * [203] Remove Linked List Elements
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

// By iterative, time: O(n), space: O(1)
struct ListNode* removeElements(struct ListNode* head, int val) {
    // 記得c語言再創造node時要malloc
    struct ListNode* dummy = malloc(sizeof(struct ListNode));
    dummy->next = head;
    struct ListNode* cur = dummy;
    while(cur->next!=NULL) {
        if(cur->next->val==val) {
            cur->next = cur->next->next;
        }
        else {
            cur = cur->next;
        }
    }
    return dummy->next;
}

// By recursive, time: O(n), space: O(n)
// struct ListNode* removeElements(struct ListNode* head, int val) {
//     if (head == NULL) {
//         return head;
//     }
//     head->next = removeElements(head->next, val);
//     if(head->val==val) {
//         return head->next;
//     }
//     else {
//         return head;
//     }
// }
