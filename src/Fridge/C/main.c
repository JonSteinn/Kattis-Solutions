#include <string.h>
#include <stdio.h>
#include <stdlib.h>

struct number
{
    char value;
    int amount;
};

int comparator(const void *a, const void *b)
{
    return ((struct number*)a)->amount - ((struct number*)b)->amount;
}

void print_char(char c, int n)
{
    char buffer[n + 1];
    for (int i = 0; i < n; i++) buffer[i] = c;
    buffer[n] = '\0';
    printf("%s\n", buffer);
}

char least_with(struct number* numbers, int value)
{
    char least_value = '9';
    int index = 0;
    while (numbers[index].amount == value && index < 10)
    {
        if (numbers[index].value < least_value && numbers[index].value != '0') least_value = numbers[index].value;
        index++;
    }
    return least_value;
}


void lowest(struct number* numbers)
{
    if (numbers[0].value == '0')
    {
        if (numbers[0].amount == numbers[1].amount)
        {
            print_char(least_with(numbers, numbers[0].amount), numbers[0].amount + 1);
        }
        else
        {
            printf("1");
            print_char('0', numbers[0].amount + 1);
        }
    }
    else if (numbers[0].amount == 0)
    {
        printf("%c\n", least_with(numbers, 0));
    }
    else
    {
        print_char(least_with(numbers, numbers[0].amount), numbers[0].amount + 1);
    }
}

int main()
{
    struct number numbers[10];
    for (int i = 0; i < 10; i++) {
        numbers[i].value = (char)('0'+i);
        numbers[i].amount = 0;
    }
    char buffer[1001];
    scanf("%s",buffer);
    size_t len = strlen(buffer);
    for (int i = 0; i < len; i++) numbers[buffer[i] - '0'].amount++;
    qsort(numbers, 10, sizeof(struct number), comparator);
    lowest(numbers);
    return 0;
}