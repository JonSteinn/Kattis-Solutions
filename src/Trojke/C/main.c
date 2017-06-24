#include <stdio.h>
#include <stdlib.h>

struct point
{
    char x;
    char y;
};

struct frac
{
    int a, b;
};

// Lexicographical order (cmp y if not equal, x otherwise)
int p_comparator(const void* _a, const void* _b)
{
    struct point* a = (struct point*)_a;
    struct point* b = (struct point*)_b;
    return a->y - b->y ? a->y - b->y : a->x - b->x;
}

// By value of fraction
int f_comparator(const void* _a, const void* _b)
{
    struct frac* f1 = (struct frac*)_a;
    struct frac* f2 = (struct frac*)_b;

    if (f1->b == 0) return f2->b == 0 ? f1->a - f2->a : f1->a;
    if (f2->b == 0) return -f2->a;
    if (f1->a < 0 && f2->a >= 0) return -1;
    if (f2->a <0 && f1->a >= 0) return 1;
    return f1->a >= 0 ? f1->a * f2->b - f2->a * f1->b : f2->a * f1->b - f1->a * f2->b;

}

// binary gcd from wiki
int gcd(int u, int v)
{
    int shift;
    if (u == 0) return v;
    if (v == 0) return u;
    for (shift = 0; ((u | v) & 1) == 0; ++shift)
    {
        u >>= 1;
        v >>= 1;
    }
    while ((u & 1) == 0) u >>= 1;
    do
    {
        while ((v & 1) == 0) v >>= 1;
        if (u > v)
        {
            int t = v;
            v = u;
            u = t;
        }
        v = v - u;
    }
    while (v != 0);
    return u << shift;
}

void slope(struct point* from, struct point* to, struct frac* f)
{
	// 1/0 = +inf & -1/0 = -inf
    if (from->x == to->x)
    {
        f->a = from->y == to->y ? -1 : 1;
        f->b = 0;
    }
    else
    {
        f->a = to->y - from->y;
        f->b = to->x - from->x;
        // if negative, always have a < 0 and b > 0
        int g = f->b < 0 ? -gcd(abs(f->a), abs(f->b)) : gcd(abs(f->a), abs(f->b));
        f->a /= g;
        f->b /= g;
    }
}

// find points in grid and return the number of points
size_t read_points(int d, struct point* p_arr)
{
    size_t p_count = 0;
    char buffer[d + 1];
    for (char i = 0; i < d; i++)
    {
        scanf("%s", buffer);
        for (char j = 0; j < d; j++)
        {
            if (buffer[j] != '.')
            {
                p_arr[p_count].x = j;
                p_arr[p_count].y = ((char)(d-1)) - i;
                p_count++;
            }
        }
    }
    return p_count;
}

// For each run of at least two equal slopes we have
// found a line with at least one triple. Suppose this
// line ends up having k+1 points, 1 which pov's we
// are looking at and k equal slopes from it, then there
// are binom(k,2) ways of forming pairs of two from these
// k equal slopes which is the counter we return. Triples
// not envolving our pov point will be counted in later
// calls to the function.
int lines_of_two(size_t s_len, struct frac* slopes)
{
    int counter = 0;
    int last_a = slopes[0].a - 1; // anything not equal
    int last_b = 0;
    int run = 0;
    int index = 0;
    while (1)
    {
        if (index == s_len)
        {
            if (run > 1) counter += (run * (run-1)) >> 1;
            break;
        }
        if (last_a == slopes[index].a && last_b == slopes[index].b)
        {
            run++;
        }
        else
        {
            if (run > 1) counter += (run * (run-1)) >> 1; // binom(run,2)
            run = 1;
        }
        last_a = slopes[index].a;
        last_b = slopes[index].b;
        index++;
    }
    return counter;
}

// In lexicographical order, take points p in {0, 1, ..., n-3}
// and look at the sorted slopes from p to {p+1,p+2,...,n-1}.
int lines_of_three(size_t p_count, struct point* p_arr)
{
    qsort(p_arr, p_count, sizeof(struct point), p_comparator);
    int counter = 0;
    for (int i = 0; i < p_count - 2; i++)
    {
        size_t s_len = (size_t)(p_count-i-1);
        struct frac slopes[s_len];
        for (int j = i+1; j < p_count; j++) slope(&p_arr[i], &p_arr[j], &slopes[j-i-1]);
        qsort(slopes, s_len, sizeof(struct frac), f_comparator);
        counter += lines_of_two(s_len, slopes);
    }
    return counter;
}

int main()
{
    int d;
    scanf("%d",&d);
    // memory for max amount of points
    struct point p_arr[d * d];
    size_t p_count = read_points(d, p_arr);
    printf("%d\n", d < 3 || p_count < 3 ? 0 : lines_of_three(p_count, p_arr));
    return 0;
}