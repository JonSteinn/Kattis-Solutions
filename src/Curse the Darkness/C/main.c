#include <stdio.h>

int main() {
    int n;
    scanf("%d",&n);
    while(n--) {
        double bx,by;
        scanf("%lf %lf",&bx,&by);
        int c;
        scanf("%d",&c);
        int found = 0;
        while(c--) {
            double cx,cy;
            scanf("%lf %lf",&cx,&cy);
            double dx = cx-bx, dy = cy-by;
            dx *= dx;
            dy *= dy;
            if (dx + dy <= 64) {
                found = 1;
                while (c--) scanf("%lf %lf",&cx,&cy);
                c = 0;
            }
        }
        printf(found ? "light a candle\n" : "curse the darkness\n");
    }

    return 0;
}