#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>
#include <stddef.h>

void KMP(char* p, size_t pl, char* t, size_t tl) {
    int suf[pl], len = 0, i = 1, j = 0, first = 1;
    suf[0] = 0;
    while (i < pl) { 
        if (p[i] == p[len]) suf[i++] = ++len;
        else if (len) len = suf[len-1];
        else suf[i++] = 0;
    }
    i = 0;
    while (i < tl) { 
        if (p[j] == t[i]) { 
            j++; i++; 
        } 
        if (j == pl) {
            if (first) first = 0;
            else putchar(' ');
            printf("%d", i-j);
            j = suf[j - 1]; 
        } else if (i < tl && p[j] != t[i]) { 
            if (j) j = suf[j-1]; 
            else i++; 
        } 
    } 
    putchar('\n');
}

int main(void) {
    size_t a = 0, b = 0;
    char *pattern = NULL, *text = NULL;
    ssize_t p_len = 0, t_len = 0;
    while ((p_len = getline(&pattern, &a, stdin)) >= 0 && (t_len = getline(&text, &b, stdin)) >= 0) {
        KMP(pattern, (size_t)(p_len-1), text, (size_t)(t_len-1));
        free(pattern);
        free(text);
        a = 0;
        b = 0;
    }
    return 0;
}