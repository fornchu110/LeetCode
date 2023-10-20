/*
 * @lc app=leetcode id=328 lang=c
 *
 * [328] Odd Even Linked List
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

// By merge two head, time: O(n), space: O(1)
struct ListNode* oddEvenList(struct ListNode* head){
    if(head==NULL) {
        return head;
    }
    struct ListNode *odd = head, *even = odd->next, *evenHead = even;
    while(even!=NULL&&even->next!=NULL) {
        odd->next = even->next;
        odd = odd->next;
        even->next = odd->next;
        even = even->next;
    }
    odd->next = evenHead;
    return head;
}

// @lc code=end

