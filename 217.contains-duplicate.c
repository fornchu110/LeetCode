/*
 * @lc app=leetcode id=217 lang=c
 *
 * [217] Contains Duplicate
 */

// @lc code=start
struct hashTable {
    int key;
    UT_hash_handle hh;
};

bool containsDuplicate(int* nums, int numsSize) {
    // hashtable本身, 使用UT_hash需要用個pointer指向hashtable結構
    struct hashTable* set = NULL;
    for(int i=0;i<numsSize;i++) {
        // 用來接收hashtable回傳結果
        struct hashTable* tmp;
        // HASH_FIND_INT(hashtable, key, FIND KEY位置沒找到就NULL)
        HASH_FIND_INT(set, nums+i, tmp);
        // 當沒在hash內找到這個元素, 代表第一次出現
        if(tmp==NULL) {
            // 分配一塊hash空間給他
            tmp = malloc(sizeof(struct hashTable));
            tmp->key = nums[i];
            // HASH_ADD_INT(hashtable, key, hash空間)
            HASH_ADD_INT(set, key, tmp);
        } 
        else {
            return true;
        }
    }
    return false;
}

// @lc code=end

