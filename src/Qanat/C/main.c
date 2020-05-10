// See .py for explanation

#include <stdio.h>

typedef long double ld;

ld get_last(int w, int n, ld r, ld z) {
    ld zsq = z*z;
    ld total = 1.0;
    for (int i = 0; i < n-1; i++) total = zsq / total + (i&1 ? 1 : -1);
    total = w*z/total;
    return total < 0 ? -total : total;
}

void fill(ld *xs, int n, int w, ld r) {
    ld z = (1.0-r*r)/2.0;
    xs[0] = 0;
    xs[n+1] = w;
    xs[n] = get_last(w,n,r,z);
    for (int i=n-1; i > 0; i--) xs[i] = xs[i+1]/z - xs[i+2];
}

ld cost(ld x1, ld x2, ld r) {
    ld split = (x2*(1+r)+x1*(1-r))/2;
    ld a = (x2 - split + r*x2), b = (split - x1 + r*x1);
    return (a*a + b*b)/2;
}

ld get_cost(int n, ld r, ld *xs) {
    ld c = 0.0;
    ld rsq = r*r;
    for (int i = 0; i < n+1; i++) c += cost(xs[i],xs[i+1],r);
    for (int i = 1; i < n+1; i++) c -= rsq*xs[i]*xs[i]/2.0;
    return c;
}

void print_xs(ld *xs, int n) {
    int top = n > 10 ? 10 : n;
    for (int i = 1; i <= top; i++) printf("%.4LF\n", xs[i]);
}

int main() {
    int w,h,n;
    scanf("%d %d %d", &w, &h, &n);
    ld r = h/(ld)w;
    ld xs[n+2];
    fill(xs, n, w, r);
    printf("%.4LF\n", get_cost(n,r,xs));
    print_xs(xs, n);
    return 0;
}