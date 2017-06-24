//
// Created by Jonni on 6/23/2017.
//

#include "BFS_Queue.h"

BFS_Queue::BFS_Queue(int max_nodes_created) {
    memory = (Node*)malloc(sizeof(Node) * max_nodes_created);
    head = memory;
    tail = memory;
}

BFS_Queue::~BFS_Queue() {
    free(memory);
}

bool BFS_Queue::is_empty() {
    return head == tail;
}

void BFS_Queue::add(short x, short y, int cost) {
    tail->x = x;
    tail->y = y;
    tail->cost = cost;
    tail++;
}

Node *BFS_Queue::poll() {
    Node* tmp = head;
    head++;
    return tmp;
}
