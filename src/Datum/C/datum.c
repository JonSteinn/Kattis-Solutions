#include <stdio.h>

int months_to_days(int n)
{
    switch(n)
    {
        case 1:
            return 0;
        case 2:
            return 31;
        case 3:
            return 59;
        case 4:
            return 90;
        case 5:
            return 120;
        case 6:
            return 151;
        case 7:
            return 181;
        case 8:
            return 212;
        case 9:
            return 243;
        case 10:
            return 273;
        case 11:
            return 304;
        case 12:
        default:
            return 334;
    }
}

int main()
{
    int day = 4;
    int days, months;
    scanf("%d %d", &days, &months);
    day += (days-1) + months_to_days(months);
    day %= 7;
    switch (day)
    {
        case 0:
            printf("Sunday\n");
            break;
        case 1:
            printf("Monday\n");
            break;
        case 2:
            printf("Tuesday\n");
            break;
        case 3:
            printf("Wednesday\n");
            break;
        case 4:
            printf("Thursday\n");
            break;
        case 5:
            printf("Friday\n");
            break;
        case 6:
            printf("Saturday\n");
            break;
        default:
            printf("Saturday\n");
    }
    return 0;
}