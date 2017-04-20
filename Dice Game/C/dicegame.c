#include <stdio.h>
#include <stdlib.h>

// Expected value
#define EXPECTED(a,b) (((double)(((b*(b+1))-(a*(a-1)))>>1))/(b-a+1))

int main()
{
    char* dices = (char*)calloc(8,8);
    scanf("%hhu %hhu %hhu %hhu",dices,dices+1,dices+2,dices+3);
    scanf("%hhu %hhu %hhu %hhu",dices+4,dices+5,dices+6,dices+7);
    double result = EXPECTED(*dices,*(dices+1))
                    + EXPECTED(*(dices+2),*(dices+3))
                    - EXPECTED(*(dices+4),*(dices+5))
                    - EXPECTED(*(dices+6),*(dices+7));
    printf(result > 0 ? "Gunnar" : result < 0 ? "Emma" : "Tie");
    free(dices);
    return 0;
}