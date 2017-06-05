//
// Created by Jonni on 6/5/2017.
//

#include "Sky.h"

Sky::Sky(int m, int n) : m(m), n(n) {
    for (int i = 0; i < this->m; i++) {
        char buffer[this->n + 1];
        scanf("%s", buffer);
        for (int j = 0; j < this->n; j++) {
            if (buffer[j] == '-') {
                stars.insert(i * this->n + j);
            }
        }
    }
}

int Sky::number_of_stars() {
    int counter = 0;
    while (!stars.empty()) {
        std::stack<int> connected;
        connected.push(*stars.begin());
        while (!connected.empty()) {
            int current = connected.top();
            connected.pop();
            if (stars.erase(current)) {
                int neighbor, mod;
                if (stars.find(neighbor = current - n) != stars.end()) connected.push(neighbor);
                if (stars.find(neighbor = current + n) != stars.end()) connected.push(neighbor);
                if ((mod = current % n) > 0 && stars.find(neighbor = current - 1) != stars.end()) connected.push(neighbor);
                if (mod < n - 1 && stars.find(neighbor = current + 1) != stars.end()) connected.push(neighbor);
            }
        }
        counter++;
    }
    return counter;
}
