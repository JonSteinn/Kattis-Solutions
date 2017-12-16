#include <stdio.h>

// n^2 is fine for n <= 50...

int walk(int count, int* commands, int goal_x, int goal_y)
{
    // N = 0, E = 1, S = 2, W = 3
    int x = 0, y = 0, o = 0;
    for (int i = 0; i < count; i++)
    {
        if (commands[i] == 0)
        {
            if (o == 0) y++;
            else if (o == 1) x++;
            else if (o == 2) y--;
            else x--;
        }
        else if (commands[i] < 0)
        {
            o = (o + 3) % 4;
        }
        else
        {
            o = (o + 1) % 4;
        }
    }
    return x == goal_x && y == goal_y;
}

int main()
{
    int x = 0,y = 0;
    scanf("%d %d",&x,&y);

    int count = 0;
    scanf("%d",&count);
    int commands[count];
    char buffer[8];
    for (int i = 0; i < count; i++)
    {
        scanf("%s", buffer);
        commands[i] = buffer[0] == 'F' ? 0 : buffer[0] == 'L' ? -1 : 1;
    }

    for (int i = 0; i < count; i++)
    {
        int original = commands[i];
        int found = 0;
        for (int z = -1; z < 2; z++)
        {
            if (z != original)
            {
                commands[i] = z;
                if (walk(count, commands, x, y))
                {
                    printf("%d %s\n", i + 1, !z ? "Forward" : z < 0 ? "Left" : "Right");
                    found = 1;
                }
            }
            if (found) break;
        }
        if (found) break;
        commands[i] = original;
    }

    return 0;
}