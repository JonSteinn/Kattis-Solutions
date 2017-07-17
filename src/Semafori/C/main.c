#include <stdio.h>

struct triple
{
    int d, r, g;
};

int remaining_red(struct triple* light, int time)
{
    int t = 0;
    int red_next = 1;
    while (1)
    {
        if (red_next)
        {
            t += light->r;
            if (t > time) return t - time;
            if (t == time) return 0;
        }
        else
        {
            t += light->g;
            if (t > time) return 0;
            if (t == time) return light->r;
        }
        red_next = !red_next;
    }
}

int seconds(int n, int l, struct triple* lights)
{
    int time = 0;
    int distance = 0;

    for (int i = 0; i < n; i++)
    {
        time += lights[i].d - distance;
        distance = lights[i].d;
        time += remaining_red(&lights[i], time);
    }

    return time + (l - distance);
}

int main()
{
    int n, l;
    scanf("%d %d",&n,&l);
    struct triple traffic_lights[n];
    for (int i = 0; i < n; i++) scanf("%d %d %d", &traffic_lights[i].d, &traffic_lights[i].r, &traffic_lights[i].g);
    printf("%d\n", seconds(n,l,traffic_lights));
    return 0;
}