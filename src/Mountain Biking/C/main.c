#include <stdio.h>
#include <math.h>

#define PI 3.1415926535897932384626433832795028841971693993751058209749445923

double end_velocity(int distance, int theta, double g, double start_velocity)
{
    return sqrt(2 * g * cos(theta * PI / 180) * distance + start_velocity * start_velocity);
}

void down_from(int i, int n, int* dist, int* deg, double g)
{
    double velocity = 0;
    for (int j = i; j < n; j++) velocity = end_velocity(dist[j], deg[j], g, velocity);
    printf("%.6lf\n", velocity);
}

int main()
{
    int n;
    double g;
    scanf("%d %lf", &n, &g);
    int arr[n << 1];
    int *dist = arr;
    int *deg = arr + n;
    for (int i = 0; i < n; i++) scanf("%d %d", dist + i, deg + i);
    for (int i = 0; i < n; i++) down_from(i, n, dist, deg, g);
    return 0;
}