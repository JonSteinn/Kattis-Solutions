#include <stdio.h>
#include <queue>

using namespace std;

typedef unsigned long long ull;

ull m_sum(int *arr, int size) {
    priority_queue<int> max_heap;
    priority_queue<int,vector<int>,greater<int>> min_heap;

    ull total = arr[0];
    max_heap.push(arr[0]);

    for (int i = 1; i < size; i++) {
        if (arr[i] > max_heap.top()) {
            min_heap.push(arr[i]);
            if (min_heap.size() > max_heap.size()) {
                max_heap.push(min_heap.top());
                min_heap.pop();
            }
        } else {
            max_heap.push(arr[i]);
            if (max_heap.size() > min_heap.size()+1) {
                min_heap.push(max_heap.top());
                max_heap.pop();
            }
        }
        total += i&1 ? (max_heap.top() + min_heap.top())>>1 : max_heap.top();
    }

    return total;
}

int main() {
    int n, size;
    int arr[100000];
    scanf("%d",&n);
    while(n--) {
        scanf("%d",&size);
        for (int i = 0; i < size; i++) scanf("%d", arr + i);
        printf("%llu\n", m_sum(arr, size));
    }
    return 0;
}