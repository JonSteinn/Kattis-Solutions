#include <stdio.h>
#include <stdlib.h>

char* create_board();
int contains(char* board, char x, char y);
int check_diagonals(char* board);

char main()
{
    char* board;
    if ((board = create_board()) == NULL) printf("invalid\n");
    else
    {
        printf(check_diagonals(board) ? "valid\n" : "invalid\n");
        free(board);
    }
    return 0;
}

char* create_board()
{
    char* return_value = (char*)calloc(8,sizeof(char));
    char y,x,index = 0, column_check = 0;
    for (y = 7; y >= 0; y--)
    {
        char buffer[9];
        scanf("%s", buffer);
        int row_check = 0;
        for (x = 0; x < 8; x++)
        {
            if (buffer[x] == '*')
            {
                if (row_check > 0 || (column_check & (1<<x)))
                {
                    free(return_value);
                    return NULL;
                }
                *(return_value+y) |= (1 << x);
                column_check |= (1 << x);
                index++;
                row_check++;
            }
        }
    }
    if (index != 8)
    {
        free(return_value);
        return NULL;
    }
    return return_value;
}

int contains(char* board, char x, char y)
{
    return *(board+y) & (1<<x);
}

int check_diagonals(char* board)
{
    char i, x, y;
    for (i = 0; i < 8; i++)
    {
        char counter = 0; x = 0; y = i;
        while (x < 8 && y < 8)
        {
            if (contains(board, x, y)) counter++;
            if (counter > 1) return 0;
            x++; y++;
        }
        counter = 0; x = 0; y = i;
        while (x < 8 && y >= 0)
        {
            if (contains(board, x, y)) counter++;
            if (counter > 1) return 0;
            x++; y--;
        }
        counter = 0; x = 7; y = i;
        while (x >= 0 && y >= 0)
        {
            if (contains(board, x, y)) counter++;
            if (counter > 1) return 0;
            x--; y--;
        }
        counter = 0; x = 7; y = i;
        while (x >= 0 && y < 8)
        {
            if (contains(board, x, y)) counter++;
            if (counter > 1) return 0;
            x--; y++;
        }
    }
    return 1;
}