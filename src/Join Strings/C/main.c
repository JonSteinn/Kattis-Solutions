#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>
#include <string.h>

// Node for list
struct Node {
    int len;
    char* str;
    struct Node* next;
};
typedef struct Node Node;

// Singly linked list
typedef struct {
    Node head;
    Node* tail;
} sll;

// Append one singly linked list to another
void append_to(sll* l1, sll* l2) {
    l1->tail->next = &l2->head;
    l1->tail = l2->tail;
}

void print(sll* l) {
    Node* next = &l->head;
    while (next != NULL) {
        printf("%.*s", next->len, next->str);
        next = next->next;
    }
    putchar('\n');
}

int main() {
    int n = 0;
    scanf("%d\n", &n);

    sll lists[n];
    int curr = 0;
    size_t dump = 0;
    for (int i = 0; i < n; i++) {
        lists[i].head.next = NULL;
        lists[i].head.str = NULL;
        lists[i].tail = &lists[i].head;
        lists[i].head.len = getline(&lists[i].head.str, &dump, stdin) - 1;
    }
    for (int i = 0; i < n - 1; i++) {
        int a = 0, b = 0;
        scanf("%d %d", &a, &b);
        a--; b--;
        curr = a;
        append_to(&lists[a], &lists[b]);
    }

    print(&lists[curr]);

    return 0;
}