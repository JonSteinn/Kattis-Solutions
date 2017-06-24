//
// Created by Jonni on 6/23/2017.
//

#ifndef BFS_QUEUE_H
#define BFS_QUEUE_H

#include <stdlib.h>

/*
 * Node for BFS search. It's cheaper to store cost than a 
 * parent pointer and iterate in the end since we do not
 * care about the path.
 */
struct Node {
    short x;
    short y;
    int cost;
};

/*
 * Queue for Node expansion. Memory waste for speed.
 * Pre-allocate all the memory we need to save os calls.
 * Each node can be expanded from 4 so (r*c)*4 should suffice.
 * No error handling.
 */
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
