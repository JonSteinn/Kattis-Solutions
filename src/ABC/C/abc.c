#include "stdio.h"

void swap(char* a, char* b)
{
    *a = *a ^ *b;
    *b = *b ^ *a;
    *a = *a ^ *b;
}

void sort(char* numbers)
{
    if (numbers[0] > numbers[1]) swap(numbers, numbers + 1);
    if (numbers[1] > numbers[2]) swap(numbers + 1, numbers + 2);
    if (numbers[0] > numbers[1]) swap(numbers, numbers + 1);
}

int main()
{
    char numbers[3];
    scanf("%hhd %hhd %hhd", numbers, numbers + 1, numbers + 2);
    sort(numbers);
    char letters[4];
    scanf("%s", letters);
    printf("%d %d %d", numbers[letters[0] - 'A'], numbers[letters[1] - 'A'], numbers[letters[2] - 'A']);
    return 0;
}