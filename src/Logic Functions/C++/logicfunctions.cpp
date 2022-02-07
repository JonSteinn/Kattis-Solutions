#include <iostream>

void exclusive(bool x, bool y, bool& ans)
{
    ans = x ^ y;
}

void implies(bool x, bool y, bool& ans)
{
    ans = !(x && !y);
}

void equivalence(bool x, bool y, bool& ans)
{
    ans = x == y;
}

using namespace std;

void checkAns(bool val, bool expected) {
    if (val != expected) {
        cout << "FAIL - expected " << expected << endl;
        exit(1);
    }
}