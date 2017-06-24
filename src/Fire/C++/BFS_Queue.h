//
// Created by Jonni on 6/23/2017.
//

#ifndef BFS_QUEUE_H
#define BFS_QUEUE_H

#include <stdlib.h>

struct Node {
    short x;
    short y;
    int cost;
};

class BFS_Queue {
public:
    BFS_Queue(int max_nodes_created);
    ~BFS_Queue();
    bool is_empty();
    void add(short x, short y, int cost);
    Node* poll();
private:
    Node* memory;
    Node* head;
    Node* tail;
};


#endif
