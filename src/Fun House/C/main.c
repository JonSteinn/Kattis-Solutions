#include <stdio.h>

#define POS_45 '/'
#define NEG_45 '\\'
#define OPEN '*'
#define EXIT '&'
#define WALL 'x'

#define NORTH 0
#define EAST 1
#define SOUTH 2
#define WEST 3

struct room
{
    char grid[20][21];
    int r, c;
    int open_r, open_c;
    int orientation;
};

void find_exit(struct room* house)
{
    while (house->grid[house->open_r][house->open_c] != WALL)
    {
        if (house->orientation == NORTH)
        {
            house->open_r--;
            if (house->grid[house->open_r][house->open_c] == POS_45) house->orientation = EAST;
            else if (house->grid[house->open_r][house->open_c] == NEG_45) house->orientation = WEST;
        }
        else if (house->orientation == EAST)
        {
            house->open_c++;
            if (house->grid[house->open_r][house->open_c] == POS_45) house->orientation = NORTH;
            else if (house->grid[house->open_r][house->open_c] == NEG_45) house->orientation = SOUTH;
        }
        else if (house->orientation == SOUTH)
        {
            house->open_r++;
            if (house->grid[house->open_r][house->open_c] == POS_45) house->orientation = WEST;
            else if (house->grid[house->open_r][house->open_c] == NEG_45) house->orientation = EAST;
        }
        else
        {
            house->open_c--;
            if (house->grid[house->open_r][house->open_c] == POS_45) house->orientation = SOUTH;
            else if (house->grid[house->open_r][house->open_c] == NEG_45) house->orientation = NORTH;
        }
    }
    house->grid[house->open_r][house->open_c] = EXIT;
}

void find_start(struct room* house)
{
    for (int r = 0; r < house->r; r++)
    {
        if (r == 0 || r == house->r - 1)
        {
            for (int c = 0; c < house->c; c++)
            {
                if (house->grid[r][c] == OPEN)
                {
                    house->open_c = c;
                    house->open_r = r;
                    house->orientation = r == 0 ? SOUTH : NORTH;
                    return;
                }
            }
        }
        else
        {
            if (house->grid[r][0] == OPEN)
            {
                house->open_c = 0;
                house->open_r = r;
                house->orientation = EAST;
                return;
            }
            else if (house->grid[r][house->c - 1] == OPEN)
            {
                house->open_c = house->c - 1;
                house->open_r = r;
                house->orientation = WEST;
                return;
            }
        }
    }
}

int main()
{
    int house_number = 1;
    struct room house;
    while(1)
    {
        scanf("%d %d", &house.c, &house.r);
        if (!house.r && !house.c) break;
        for (int r = 0; r < house.r; r++) scanf("%s", house.grid[r]);
        find_start(&house);
        find_exit(&house);
        printf("House %d\n", house_number++);
        for (int r = 0; r < house.r; r++) printf("%s\n", house.grid[r]);
    }


    return 0;
}