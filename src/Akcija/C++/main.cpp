#include <stdio.h>
#include <queue>

int main()
{
    int size, next;
    scanf("%d", &size);

    std::priority_queue<int> queue;
    while (size-- > 0)
    {
        scanf("%d", &next);
        queue.push(next);
    }

    int skip = 0, sum = 0;
    while (!queue.empty())
    {
        if (skip != 2) sum += queue.top();
        queue.pop();
        skip = skip == 2 ? 0 : skip + 1;
    }
    printf("%d\n", sum);
    return 0;
}