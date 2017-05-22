#include <stdio.h>
#include <string.h>

// Binary search for root of square given range
int root_of_square(int n, int lo, int hi)
{
    while(1)
    {
        int mid = lo+(hi-lo)/2;
        int sq = mid*mid;
        if (sq == n) return mid;
        else if (sq < n) lo = mid+1;
        else hi = mid-1;
    }
}

int main()
{
    int n;
    scanf("%d",&n);
    char buffer[20002];          // buffer1: 0-10000, buffer2: 10001-20001
    char* out = buffer + 10001;  // <--buffer2
    while(n--)
    {
        int index = 0;
        scanf("%s",buffer);
        int len = (int)strlen(buffer);
        int sqr = root_of_square(len, 1, 100);
        
        // Iterations take care of encoding
        // (sqr-1) + (2sqr-1) + ...
        // (sqr-2) + (2sqr-2) + ...
        // ...
        for (int i = sqr - 1; i >= 0; i--) 
        {
            for (int j = i; j < len; j += sqr)
            {
                out[index++] = buffer[j];
            }
        }
        
        out[index] = '\0';
        printf("%s\n", out);
    }
    return 0;
}