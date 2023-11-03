/*
 * @lc app=leetcode id=206 lang=c
 *
 * [206] Reverse Linked List
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
struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode* prev = NULL;
    struct ListNode* cur = head;
    while (cur) {
        struct ListNode* next = cur->next;
        cur->next = prev;
        prev = cur;
        cur = next;
    }
    return prev;
}

// By recursive, time: O(n), space: O(n)
// struct ListNode* reverseList(struct ListNode* head) {
//     if (head == NULL || head->next == NULL) {
//         return head;
//     }
//     struct ListNode* newHead = reverseList(head->next);
//     head->next->next = head;
//     head->next = NULL;
//     return newHead;
// }

// @lc code=end

