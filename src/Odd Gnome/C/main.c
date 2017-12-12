#include <stdio.h>

int main()
{
    int n = 0;
    scanf("%d",&n);
    while(n--)
    {
        int count = 0;
        scanf("%d", &count);

        int king_pos = -1, last = 0;
        scanf("%d", &last);
        for (int i = 1; i < count; i++)
        {
            int curr = 0;
            scanf("%d",&curr);
            if (king_pos < 0)
            {
                if (last != curr - 1) king_pos = i+1;
                last = curr;
            }
        }
        printf("%d\n", king_pos);
    }
    return 0;
}