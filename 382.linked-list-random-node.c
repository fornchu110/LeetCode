/*
 * @lc app=leetcode id=382 lang=c
 *
 * [382] Linked List Random Node
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
typedef struct {
    int * arr;
    int length;
} Solution;

Solution* solutionCreate(struct ListNode* head) {
    Solution * obj = (Solution *)malloc(sizeof(Solution));
    // assert(obj!=NULL)同if(obj!=NULL)
    // 當條件成立就繼續, 條件不成立就會中斷並提醒, 不用寫多個if else
    assert(obj != NULL);
    obj->length = 0;
    struct ListNode * node = head;

    while (node) {
        node = node->next;
        obj->length++;
    }
    obj->arr = (int *)malloc(sizeof(int) * obj->length);
    assert(obj->arr != NULL);
    node = head;
    for (int i=0; i<obj->length; i++) {
        obj->arr[i] = node->val;
        node = node->next;
    }
    return obj;
}

int solutionGetRandom(Solution* obj) {
    return obj->arr[rand() % obj->length];
}

void solutionFree(Solution* obj) {
    free(obj->arr);
    free(obj);
}

/**
 * Your Solution struct will be instantiated and called as such:
 * Solution* obj = solutionCreate(head);
 * int param_1 = solutionGetRandom(obj);
 
 * solutionFree(obj);
*/
// @lc code=end

