#include <string.h>
#include <stdio.h>

void func(char* command, size_t cmd_len, int* list, int head, int tail)
{
    int direction = 1;
    int is_empty = 0;

    for (int i = 0; i < cmd_len; i++)
    {
        if (command[i] == 'D')
        {
            if (is_empty)
            {
                printf("error\n");
                return;
            }
            if (head == tail) is_empty = 1;
            head += direction;
        }
        else
        {
            if (head - tail) head ^= tail ^= head ^= tail;
            direction = -direction;
        }
    }

    if (is_empty) printf("[]\n");
    else if (head == tail) printf("[%d]\n", list[head]);
    else
    {
        printf("[%d", list[head]);
        int index = head + direction;
        while (1)
        {
            printf(",%d", list[index]);
            if (index == tail) break;
            index += direction;
        }
        printf("]\n");
    }
}

int containsDrop(char *str, size_t len)
{
    for (int i = 0; i < len; i++)
    {
        if (str[i] == 'D') return 1;
    }
    return 0;
}

int main()
{
    char command[100001];
    int list[100000];
    int n;
    scanf("%d",&n);
    while(n--)
    {
        scanf("%s", command);
        size_t cmd_len = strlen(command);
        int list_len;
        scanf("%d", &list_len);
        if (list_len == 0)
        {
            char dump[3];
            scanf("%s", dump);
            printf(containsDrop(command, cmd_len) ? "error\n" : "[]\n");
        }
        else
        {
            char dump;
            scanf(" %c", &dump);
            scanf("%d", list);
            for (int i = 1; i < list_len; i++) scanf(",%d", list + i);
            scanf("%c", &dump);

            func(command, cmd_len, list, 0, list_len - 1);
        }
    }
    return 0;
}