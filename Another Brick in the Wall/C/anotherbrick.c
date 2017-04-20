#include <stdio.h>

#define WORKING 0
#define COMPLETE 1
#define FAILED -1

int main()
{
    int h, w, n;
    scanf("%d %d %d", &h, &w, &n);

    int status = WORKING;
    int next, current_row = w;
    while (n-- > 0)
    {
        scanf("%d", &next);
        if (!status)
        {
            if (next > current_row) status = FAILED;
            else
            {
                current_row -= next;
                if (current_row == 0)
                {
                    current_row = w;
                    h--;
                }
                if (h == 0) status = COMPLETE;
            }
        }
    }
    if (status == FAILED) printf("NO\n");
    else printf("YES\n");
    return 0;
}