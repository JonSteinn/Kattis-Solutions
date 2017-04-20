#include <stdio.h>

int main()
{
    int a, b, c, d;
    int post, milk, garbage;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    scanf("%d %d %d", &post, &milk, &garbage);
    b += a; d += c;
    int p1 = post % b, p2 = post % d;
    int m1 = milk % b, m2 = milk % d;
    int g1 = garbage % b, g2 = garbage % d;
    int p = (p1 && p1 <= a) + (p2 && p2 <= c);
    int m = (m1 && m1 <= a) + (m2 && m2 <= c);
    int g = (g1 && g1 <= a) + (g2 && g2 <= c);
    printf("%s\n%s\n%s\n",
           p == 0 ? "none" : p == 1 ? "one" : "both",
           m == 0 ? "none" : m == 1 ? "one" : "both",
           g == 0 ? "none" : g == 1 ? "one" : "both");
    return 0;
}