#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void eq_div(char* num, int num_len, int div_len) {
    // Example 12300 / 10000
    while (num[num_len-1] == '0') num_len--;
    if (num_len == 1) {
        printf("%c\n", num[0]);
    } else {
        printf("%c.",num[0]);
        printf("%.*s\n", num_len-1, num+1);
    }
}

void less_div(char* num, int num_len, int div_len) {
    // Example: 251 / 10000000
    printf("0.");
    if (div_len - num_len > 1) printf("%0*d", div_len - num_len - 1, 0);
    while (num[num_len-1] == '0') num_len--;
    printf("%.*s\n", num_len, num);
}

void more_div(char* num, int num_len, int div_len) {
    // Example: 4311561 / 100
    int padded = 0;
    while (num[num_len-1] == '0' && padded < div_len - 1) {
        num_len--;
        padded++;
    }

    if (padded == div_len - 1) {
        printf("%.*s\n", num_len, num);
    } else {
        int int_part_len = num_len + padded - div_len + 1;
        printf("%.*s.", int_part_len, num);
        printf("%.*s\n",  div_len - 1 - padded, num + int_part_len);
    }
}

void read(char **n, int *ln, int *lm) {
    size_t x = 0;
    *ln = (int)getline(n, &x, stdin) - 1;
    x = 0;
    char* tmp;
    *lm = (int)getline(&tmp, &x, stdin) - 1;
    free(tmp);
}


int main(void) {
    char *n;
    int ln, lm;
    read(&n,&ln,&lm);
    if (ln == lm) eq_div(n,ln,lm);
    else if (ln < lm) less_div(n,ln,lm);
    else more_div(n,ln,lm);
    free(n);
    return 0;
}