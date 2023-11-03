/*
 * @lc app=leetcode id=1114 lang=c
 *
 * [1114] Print in Order
 */

// @lc code=start

//By mutex lock
typedef struct {
    // User defined data may be declared here.
    pthread_mutex_t mutexA;//定義兩個mutex lock
    pthread_mutex_t mutexB;
} Foo;

Foo* fooCreate() {
    Foo* obj = (Foo*) malloc(sizeof(Foo));
    pthread_mutex_init(&(obj->mutexA),NULL);
    pthread_mutex_init(&(obj->mutexB),NULL);
    pthread_mutex_lock(&(obj->mutexA));
    pthread_mutex_lock(&(obj->mutexB));
    return obj;
}

void first(Foo* obj) {
    // printFirst() outputs "first". Do not change or remove this line.//不要更改或?除?一行。
    printFirst();
    pthread_mutex_unlock(&(obj->mutexA));
}

void second(Foo* obj) {
    pthread_mutex_lock(&(obj->mutexA));
    // printSecond() outputs "second". Do not change or remove this line.
    printSecond();
    pthread_mutex_unlock(&(obj->mutexB));
}

void third(Foo* obj) {
    pthread_mutex_lock(&(obj->mutexB));
    // printThird() outputs "third". Do not change or remove this line.
    printThird();
}

void fooFree(Foo* obj) {
    // User defined data may be cleaned up here.
    pthread_mutex_destroy(&(obj->mutexA));
    pthread_mutex_destroy(&(obj->mutexB));
}

// @lc code=end

