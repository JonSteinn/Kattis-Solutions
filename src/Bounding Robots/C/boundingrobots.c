#include <stdio.h>

struct position
{
    int x;
    int y;
};

int max(int a, int b)
{
    return a < b ? b : a;
}

int min(int a, int b)
{
    return a < b ? a : b;
}

int main()
{
    while(1)
    {
        struct position room, robot, real;
        scanf("%d %d", &room.x, &room.y);
        if (room.x == 0 && room.y == 0) break;

        robot.x = 0;
        robot.y = 0;
        real.x = 0;
        real.y = 0;

        int commands;
        scanf("%d", &commands);

        while(commands--)
        {
            char command[2];
            int amount;
            scanf("%s %d", command, &amount);
            if (command[0] == 'u')
            {
                real.y = min(room.y - 1, real.y + amount);
                robot.y += amount;
            }
            else if (command[0] == 'd')
            {
                real.y = max(0, real.y - amount);
                robot.y -= amount;
            }
            else if (command[0] == 'r')
            {
                real.x = min(room.x - 1, real.x + amount);
                robot.x += amount;
            }
            else
            {
                real.x = max(0, real.x - amount);
                robot.x -= amount;
            }
        }

        printf("Robot thinks %d %d\n", robot.x, robot.y);
        printf("Actually at %d %d\n\n", real.x, real.y);

    }

    return 0;
}