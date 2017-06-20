#include <stdio.h>

int main()
{
    int n;
    scanf("%d",&n);
    int arr[6] = {0,0,0,0,0,0};
    int indices[6] = {0,0,0,0,0,0};
    for (int i = 0; i < n; i++)
    {
        int k;
        scanf("%d",&k);
        arr[k-1]++;
        indices[k-1] = i + 1;
    }
    if (arr[5] == 1) printf("%d\n", indices[5]);
    else if (arr[4] == 1) printf("%d\n", indices[4]);
    else if (arr[3] == 1) printf("%d\n", indices[3]);
    else if (arr[2] == 1) printf("%d\n", indices[2]);
    else if (arr[1] == 1) printf("%d\n", indices[1]);
    else if (arr[0] == 1) printf("%d\n", indices[0]);
    else printf("none\n");
    return 0;
}