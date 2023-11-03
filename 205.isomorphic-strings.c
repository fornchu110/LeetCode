<<<<<<< HEAD
/*
 * @lc app=leetcode id=205 lang=c
 *
 * [205] Isomorphic Strings
 */

// @lc code=start

// By hashtable
struct HashTable {
    char key;
    char val;
    UT_hash_handle hh;
};

bool isIsomorphic(char* s, char* t) {
    struct HashTable* hashtable = NULL;
    int len = strlen(s);
    int tlen = strlen(t);
    if(len!=tlen) {
        return false;
    }
    for (int i=0;i<len;i++) {
        char x = s[i], y = t[i];
        struct HashTable *tmp1, *tmp2;
        HASH_FIND(hh, hashtable, &x, sizeof(char), tmp1);
        if (tmp1 != NULL) {
            if (tmp1->val != y) {
                return false;
            }
        } else {
            tmp1 = malloc(sizeof(struct HashTable));
            tmp1->key = x;
            tmp1->val = y;
            for(int j=0;j<i;j++) {
                char z = s[j];
                HASH_FIND(hh, hashtable, &z, sizeof(char), tmp2);
                if(tmp2->val==y) {
                    return false;
                }
            }
            HASH_ADD(hh, hashtable, key, sizeof(char), tmp1);
        }
    }
    return true;
}

// @lc code=end

=======
/*
 * @lc app=leetcode id=205 lang=c
 *
 * [205] Isomorphic Strings
 */

// @lc code=start

// By hashtable
struct HashTable {
    char key;
    char val;
    UT_hash_handle hh;
};

bool isIsomorphic(char* s, char* t) {
    struct HashTable* hashtable = NULL;
    int len = strlen(s);
    int tlen = strlen(t);
    if(len!=tlen) {
        return false;
    }
    for (int i=0;i<len;i++) {
        char x = s[i], y = t[i];
        struct HashTable *tmp1, *tmp2;
        HASH_FIND(hh, hashtable, &x, sizeof(char), tmp1);
        if (tmp1 != NULL) {
            if (tmp1->val != y) {
                return false;
            }
        } else {
            tmp1 = malloc(sizeof(struct HashTable));
            tmp1->key = x;
            tmp1->val = y;
            for(int j=0;j<i;j++) {
                char z = s[j];
                HASH_FIND(hh, hashtable, &z, sizeof(char), tmp2);
                if(tmp2->val==y) {
                    return false;
                }
            }
            HASH_ADD(hh, hashtable, key, sizeof(char), tmp1);
        }
    }
    return true;
}

// @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
