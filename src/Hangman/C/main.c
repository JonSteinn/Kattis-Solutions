#include <stdio.h>
#include <string.h>

int main() {
    char word[17], alphabet[27];
    scanf("%s", word);
    scanf("%s", alphabet);

    int w = 0;
    size_t l = strlen(word);
    for (size_t i = 0; i < l; i++) w |= (1 << (word[i] - 'A'));

    int c = 0;
    for (int i = 0; i < 26 && c < 10 && w; i++) {
        int pos = 1<<(alphabet[i]-'A');
        if (w & pos) {
            w &= ~pos;
        } else {
            c++;
        }
    }
    printf(w ? "LOSE" : "WIN");

    return 0;
}