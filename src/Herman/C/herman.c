#include <stdio.h>

int main() 
{
    double pi = 3.1415926535898;
    int radius, radiusSq;
    scanf("%d", &radius);
    
    radiusSq = radius * radius;
    printf("%.7f\n%d\n", pi * radiusSq, radiusSq << 1);
    return 0;
}