#include <malloc.h>
#include "stdio.h"

char* get_row(int row, char* board)
{
    return board + 8 * row;
}

void read_short_row(char* board, int row)
{
    scanf("%s", get_row(row, board) + 2);
}

void read_long_row(char* board, int row)
{
    scanf("%s", get_row(row, board));
}

void read_board(char* board)
{
    read_short_row(board, 0);
    read_short_row(board, 1);
    read_long_row(board, 2);
    read_long_row(board, 3);
    read_long_row(board, 4);
    read_short_row(board, 5);
    read_short_row(board, 6);
}

void show_short_row(char* board, int row)
{
    printf("  %s\n", get_row(row, board) + 2);
}

void show_long_row(char* board, int row)
{
    printf("%s\n", get_row(row, board));
}

void show_board(char* board)
{
    show_short_row(board, 0);
    show_short_row(board, 1);
    show_long_row(board, 2);
    show_long_row(board, 3);
    show_long_row(board, 4);
    show_short_row(board, 5);
    show_short_row(board, 6);
}

int out_of_bound(int x, int y /* row */)
{
    return (y >= 0 && y <= 6) ? ((y >= 2 || y <= 4) ? x < 0 || x > 6 : x < 2 || x > 4) : 1;
}

char get(int x, int y, char* board)
{
    return *(get_row(y, board) + x);
}

int check(int x, int y, char* board)
{
    return
        (!out_of_bound(x + 1, y) && !out_of_bound(x + 2, y) && (get(x + 1, y, board) == 'o' && get(x + 2, y, board) == 'o'))
        + (!out_of_bound(x - 1, y) && !out_of_bound(x - 2, y) && (get(x - 1, y, board) == 'o' && get(x - 2, y, board) == 'o'))
        + (!out_of_bound(x, y + 1) && !out_of_bound(x, y + 2) && (get(x, y + 1, board) == 'o' && get(x, y + 2, board) == 'o'))
        + (!out_of_bound(x, y - 1) && !out_of_bound(x, y - 2) && (get(x, y - 1, board) == 'o' && get(x, y - 2, board) == 'o'));
}

int check_small_row(int row, char* board)
{
    char* _row = get_row(row, board);
    int i;
    int moves = 0;
    for (i = 2; i < 5; i++) if (*(_row + i) == '.') moves += check(i, row, board);
    return moves;
}

int check_large_row(int row, char* board)
{
    char* _row = get_row(row, board);
    int i;
    int moves = 0;
    for (i = 0; i < 7; i++) if (*(_row + i) == '.') moves += check(i, row, board);
    return moves;
}

int main()
{
    char* board = (char*)malloc(sizeof(char) * 8 * 7);
    read_board(board);
    printf("%d\n",
           check_small_row(0, board) +
           check_small_row(1, board) +
           check_large_row(2, board) +
           check_large_row(3, board) +
           check_large_row(4, board) +
           check_small_row(5, board) +
           check_small_row(6, board)
    );
    free(board);
    return 0;
}