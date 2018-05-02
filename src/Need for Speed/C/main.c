#include <stdio.h>

int main()
{
    unsigned int n = 0;
    double t = 0.0;
    scanf("%u %lf", &n, &t);
    double arr[n<<1U];
    double min = 100000000.0, max = 1001000.0;
    for (unsigned int i = 0; i < n; i++)
    {
        scanf("%lf %lf", arr + i, arr + (n + i));
        if (arr[n + i] < min) min = arr[n + i];
    }
    min = -min;
    while(max-min > 0.000000001)
    {
        double mid = (min + max) / 2.0;
        double sum = 0.0;
        for (unsigned int i = 0; i < n; i++) sum += arr[i] / (arr[n + i] + mid);
        if (sum > t) min = mid;
        else if (sum < t) max = mid;
        else break;
    }
    printf("%.10lf\n", (min+max)/2.0);
    return 0;
}