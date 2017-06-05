//
// Created by Jonni on 6/5/2017.
//

#ifndef UNTITLED5_SKY_H
#define UNTITLED5_SKY_H

#include <unordered_set>
#include <stack>
#include <cstdio>

class Sky {
public:
    Sky(int m, int n);
    int number_of_stars();
private:
    int n, m;
    std::unordered_set<int> stars;
};


#endif //UNTITLED5_SKY_H
