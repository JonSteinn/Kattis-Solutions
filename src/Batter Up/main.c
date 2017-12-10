#include <stdio.h>

int main()
{
    int n, temp, counter = 0;
    double sum = 0.0;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &temp);
        if (temp < 0) continue;
        counter++;
        sum += temp;
    }
    printf("%.10f\n", sum / counter);
    return 0;
}