#include <stdio.h>
#include <unordered_set>

void dump()
{
    short a, b;
    while (scanf("%hd %hd",&a,&b) == 2) {};
}

int main()
{
    std::unordered_set<short> d1, d2, v, h;
    short n, valid = 1;
    scanf("%hd",&n);
    while(n--)
    {
        short x, y, a, b;
        scanf("%hd %hd",&x,&y);
        a = x+y;
        b = x-y;
        if (d1.find(a) != d1.end() || d2.find(b) != d2.end() || v.find(x) != v.end() || h.find(y) != h.end())
        {
            dump();
            valid = 0;
            break;
        }
        else
        {
            d1.insert(a);
            d2.insert(b);
            v.insert(x);
            h.insert(y);
        }
    }
    printf(valid ? "CORRECT\n" : "INCORRECT\n");
    return 0;
}