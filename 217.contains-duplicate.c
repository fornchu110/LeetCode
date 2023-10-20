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
    // hashtable����, �ϥ�UT_hash�ݭn�έ�pointer���Vhashtable���c
    struct hashTable* set = NULL;
    for(int i=0;i<numsSize;i++) {
        // �Ψӱ���hashtable�^�ǵ��G
        struct hashTable* tmp;
        // HASH_FIND_INT(hashtable, key, FIND KEY��m�S���NNULL)
        HASH_FIND_INT(set, nums+i, tmp);
        // ��S�bhash�����o�Ӥ���, �N��Ĥ@���X�{
        if(tmp==NULL) {
            // ���t�@��hash�Ŷ����L
            tmp = malloc(sizeof(struct hashTable));
            tmp->key = nums[i];
            // HASH_ADD_INT(hashtable, key, hash�Ŷ�)
            HASH_ADD_INT(set, key, tmp);
        } 
        else {
            return true;
        }
    }
    return false;
}

// @lc code=end

