#include <stdio.h>

/*
0 is always a P position

0 can't be reached from {1,2,...,a-1} which are therefore also P positions

{0,1,2,...,a-1} can be reached from {a,a+1,a+2,...,a+b-1} which are therefore N positions

We can continue like this until we reach k
*/

int main() {
    int k,a,b;
    scanf("%d %d %d", &k, &a, &b);
    printf(k % (a+b) < a ? "Barb\n" : "Alex\n");
    return 0;
}