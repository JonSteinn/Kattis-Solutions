#include <stdio.h>

// binary gcd from wiki
long long gcd(long long u, long long v)
{
    long long shift;
    if (u == 0L) return v;
    if (v == 0L) return u;
    for (shift = 0L; ((u | v) & 1L) == 0L; ++shift)
    {
        u >>= 1;
        v >>= 1;
    }
    while ((u & 1L) == 0L) u >>= 1L;
    do
    {
        while ((v & 1L) == 0L) v >>= 1L;
        if (u > v)
        {
            long long t = v;
            v = u;
            u = t;
        }
        v = v - u;
    } while (v != 0L);
    return u << shift;
}

struct fraction
{
    long long a, b;
};

void sum(struct fraction* x, struct fraction* y, struct fraction* r)
{
    r->a = (x->a * y->b + y->a * x->b);
    r->b = (x->b * y->b);
}

void dif(struct fraction* x, struct fraction* y, struct fraction* r)
{
    r->a = (x->a * y->b - y->a * x->b);
    r->b = (x->b * y->b);
}

void mul(struct fraction* x, struct fraction* y, struct fraction* r)
{
    r->a = x->a * y->a;
    r->b = x->b * y->b;
}

void div(struct fraction* x, struct fraction* y, struct fraction* r)
{
    r->a = x->a * y->b;
    r->b = x->b * y->a;
}

void simplify(struct fraction* frac)
{
    if (frac->b < 0)
    {
        frac->a = -frac->a;
        frac->b = -frac->b;
    }
    long long _gcd = gcd(frac->a < 0 ? -frac->a : frac->a, frac->b);
    frac->a /= _gcd;
    frac->b /= _gcd;
}

int main()
{
    int n;
    scanf("%d",&n);
    while(n--)
    {
        struct fraction first, second;
        char op[2]; // <-- lazy char reading
        scanf("%lld %lld %s %lld %lld", &first.a, &first.b, op, &second.a, &second.b);
        struct fraction result;
        if (op[0] == '+') sum(&first, &second, &result);
        else if (op[0] == '-') dif(&first, &second, &result);
        else if (op[0] == '*') mul(&first, &second, &result);
        else div(&first, &second, &result);
        simplify(&result);
        printf("%lld / %lld\n", result.a, result.b);
    }
    return 0;
}