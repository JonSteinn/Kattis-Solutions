#include <stdio.h>
#include <math.h>

#define PI 3.1415926535897932384626433832795028841971693993751058209749445923
#define PI_HALF 1.5707963267948966192313216916397514420985846996875529104874722961

int main()
{
    int h, v;
    scanf("%d %d",&h,&v);
    printf(v <= 180 ? "safe\n" : "%d\n", (int)(h/(cos(PI * v / 180.0 + PI_HALF))));
    return 0;
}