#include <stdio.h>
#include <math.h>
#include <string.h>
#include <complex.h>
#include <stdlib.h>

typedef double complex c;
typedef struct {
    c *arr;
    int size;
} Polynomial;

void fft(c *arr, c *tmp, int n, int s) {
    if (s >= n) return;
    int s2 = s<<1;
    fft(tmp, arr, n, s2);
    fft(tmp+s, arr+s, n, s2);
    for (int i = 0; i < n; i += s2) {
        c twiddle = cexp(-I * M_PI * i / n) * tmp[i + s];
        arr[i>>1] = tmp[i]+twiddle;
        arr[(i+n)>>1] = tmp[i]-twiddle;
    }
}

void inverse_fft(c *arr, c *tmp, int n, int s) {
    if (s >= n) return;
    int s2 = s<<1;
    inverse_fft(tmp, arr, n, s2);
    inverse_fft(tmp+s, arr+s, n, s2);
    for (int i = 0; i < n; i += s2) {
        c twiddle = cexp(I * M_PI * i / n) * tmp[i + s];
        arr[i>>1] = (tmp[i]+twiddle)/2;
        arr[(i+n)>>1] = (tmp[i]-twiddle)/2;
    }
}

void poly_mul(Polynomial *p, Polynomial *q, Polynomial *tmp) {
    memcpy(tmp->arr, p->arr, p->size * sizeof(c));
    fft(p->arr, tmp->arr, p->size, 1);

    memcpy(tmp->arr, q->arr, q->size * sizeof(c));
    fft(q->arr, tmp->arr, q->size, 1);

    for (int i = 0; i < p->size; i++) p->arr[i] = p->arr[i] * q->arr[i];

    memcpy(tmp->arr, p->arr, p->size * sizeof(c));
    inverse_fft(p->arr, tmp->arr, p->size, 1);
}

int smallest_2nd_power_larger_or_equal_to(int k) {
    int n = k;
    n |= (n >>  1);
    n |= (n >>  2);
    n |= (n >>  4);
    n |= (n >>  8);
    n |= (n >> 16);
    n &= ~(n>>1);
    return k == n ? n : n<<1;
}

int init_poly(Polynomial *p, Polynomial *q, Polynomial *tmp) {
    int x;
    scanf("%d",&x); // Dump test case
    
    p->arr = (c*)calloc(786432, sizeof(c));
    q->arr = p->arr + 262144;
    tmp->arr = q->arr + 262144;

    int a,b;
    scanf("%d",&a);
    for (int i = 0; i <= a; i++) {
        scanf("%d",&x);
        p->arr[i] = x;
    }
    scanf("%d",&b);
    for (int i = 0; i <= b; i++) {
        scanf("%d",&x);
        q->arr[i] = x;
    }

    int size = a+b+1;
    p->size = smallest_2nd_power_larger_or_equal_to(size);
    q->size = p->size;
    tmp->size = q->size;
    return size;
}

int main() {
    Polynomial p,q,tmp;
    int size = init_poly(&p, &q, &tmp);
    poly_mul(&p,&q,&tmp);
    printf("%d\n", size-1);
    for (int i = 0; i < size; i++) {
        if (i) putchar(' ');
        double x = creal(p.arr[i]);
        printf("%d", (int)(x + 0.5 - (x<0)));
    }
    putchar('\n');
    return 0;
}