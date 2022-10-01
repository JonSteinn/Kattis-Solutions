#include "heap.h"
#include <queue>

// yes I'm this lazy
std::priority_queue<int> heap;

int getMax() { return heap.top(); }

int getSize() {
    return heap.size(); 
}

void insert(int element) {
  heap.push(element);
}

void removeMax() { heap.pop(); }
