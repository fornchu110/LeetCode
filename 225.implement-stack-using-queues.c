/*
 * @lc app=leetcode id=225 lang=c
 *
 * [225] Implement Stack using Queues
 */

// @lc code=start
// By queue, time: push: O(n), 其他: O(1), space: O(n)
// 用一個queue實現stack

//是用linklist來將結點連結在一起
typedef struct tagListNode {
    struct tagListNode* next;
    int val;
} ListNode;

typedef struct {
    ListNode* top;
} MyStack;

MyStack* myStackCreate() {
    MyStack* stk = calloc(1, sizeof(MyStack));
    return stk;
}

void myStackPush(MyStack* obj, int x) {
    ListNode* node = malloc(sizeof(ListNode));
    node->val = x;
    node->next = obj->top;
    obj->top = node;
}

int myStackPop(MyStack* obj) {
    ListNode* node = obj->top;
    int val = node->val;
    obj->top = node->next;
    free(node);

    return val;
}

int myStackTop(MyStack* obj) {
    return obj->top->val;
}

bool myStackEmpty(MyStack* obj) {
    return (obj->top == NULL);
}

void myStackFree(MyStack* obj) {
    while (obj->top != NULL) {
        ListNode* node = obj->top;
        obj->top = obj->top->next;
        free(node);
    }
    free(obj);
}


/**
 * Your MyStack struct will be instantiated and called as such:
 * MyStack* obj = myStackCreate();
 * myStackPush(obj, x);
 
 * int param_2 = myStackPop(obj);
 
 * int param_3 = myStackTop(obj);
 
 * bool param_4 = myStackEmpty(obj);
 
 * myStackFree(obj);
*/
// @lc code=end
