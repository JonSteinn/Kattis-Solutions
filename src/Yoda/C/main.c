#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void collision(int n, int k)
{
    char num_str1[11], num_str2[11];
    memset(num_str1, 0, 11);
    memset(num_str2, 0, 11);
    sprintf(num_str1, "%d", n);
    sprintf(num_str2, "%d", k);
    size_t len_n = strlen(num_str1);
    size_t len_k = strlen(num_str2);
    int i = (int)(len_n - 1);
    int j = (int)(len_k - 1);
    while (i >= 0 && j >= 0)
    {
        if (num_str1[i] > num_str2[j]) num_str2[j] = '.';
        else if (num_str1[i] < num_str2[j]) num_str1[i] = '.';
        i--; j--;
    }

    int counter_n = 0, counter_k = 0;
    char n_str[11], k_str[11];
    i = 0, j = 0;
    for (int l = 0; l < len_n; l++)
    {
        if (num_str1[l] != '.')
        {
            n_str[i++] = num_str1[l];
        }
        else
        {
            counter_n++;
        }
    }
    n_str[i] = '\0';
    for (int l = 0; l < len_k; l++)
    {
        if (num_str2[l] != '.')
        {
            k_str[j++] = num_str2[l];
        }
        else
        {
            counter_k++;
        }
    }
    k_str[j] = '\0';
    if (counter_n == len_n) printf("YODA\n");
    else printf("%d\n", atoi(n_str));
    if (counter_k == len_k) printf("YODA\n");
    else printf("%d\n", atoi(k_str));
}

int main()
{
    int n,k;
    scanf("%d %d",&n,&k);
    collision(n,k);
    return 0;
}