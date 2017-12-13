#include <stdio.h>

double average_test(int count)
{
    double average = 0;
    int arr[count];
    for (int i = 0; i < count; i++)
    {
        scanf("%d", arr  + i);
        average += arr[i];
    }
    average /= count;
    double counter = 0;
    for (int i = 0; i < count; i++)
    {
        if (arr[i] > average) counter++;
    }
    return (counter / count) * 100;
}

int main()
{
    int n = 0;
    scanf("%d",&n);
    while(n--)
    {
        int k = 0;
        scanf("%d",&k);
        printf("%.3f%%\n", average_test(k));
    }
    return 0;
}