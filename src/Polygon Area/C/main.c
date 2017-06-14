#include <stdio.h>

struct vertex
{
    int x, y;
};

int det(struct vertex* v1, struct vertex* v2)
{
    return v1->x * v2->y - v1->y * v2->x;
}

int main()
{
    while(1)
    {
        int n;
        scanf("%d",&n);
        if (!n) break;

        struct vertex vertices[n];
        for (int i = 0; i < n; i++) scanf("%d %d", &(vertices + i)->x, &(vertices + i)->y);

        int sum = 0;
        for (int i = 0; i < n - 1; i++) sum += det(vertices + i, vertices + i + 1);
        sum += det(vertices + n - 1, vertices);

        if (sum < 0) printf("CW %.1f\n", -sum / 2.0);
        else printf("CCW %.1f\n", sum / 2.0);
    }
    return 0;
}