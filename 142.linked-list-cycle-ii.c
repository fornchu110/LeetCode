<<<<<<< HEAD
/*
 * @lc app=leetcode id=142 lang=c
 *
 * [142] Linked List Cycle II
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
// By fast-slow pointer, time: O(n), space: O(1)
struct ListNode *detectCycle(struct ListNode *head) {
    struct ListNode *fast = head, *slow = head;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow==fast) { 
            fast = head;
            while(fast!=slow) {
                fast = fast->next;
                slow = slow->next;
            }
            return fast;
        }
    }
    return NULL;
}

// @lc code=end

=======
/*
 * @lc app=leetcode id=142 lang=c
 *
 * [142] Linked List Cycle II
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
// By fast-slow pointer, time: O(n), space: O(1)
struct ListNode *detectCycle(struct ListNode *head) {
    struct ListNode *fast = head, *slow = head;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow==fast) { 
            fast = head;
            while(fast!=slow) {
                fast = fast->next;
                slow = slow->next;
            }
            return fast;
        }
    }
    return NULL;
}

// @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
