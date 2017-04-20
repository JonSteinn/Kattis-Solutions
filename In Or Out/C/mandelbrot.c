#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct complex
{
    double RE;
    double IM;
};

void next(struct complex* seq_num, struct complex* con)
{
    double temp = seq_num->RE * seq_num->RE - seq_num->IM * seq_num->IM + con->RE;
    seq_num->IM = 2 * seq_num->RE * seq_num->IM + con->IM;
    seq_num->RE = temp;
}

double c_len(struct complex* c_num)
{
    return sqrt(c_num->RE * c_num->RE + c_num->IM * c_num->IM);
}

int main()
{
    int n = 1;
    int iterations;
    struct complex* c = (struct complex*)malloc(sizeof(struct complex));
    struct complex* seq = (struct complex*)malloc(sizeof(struct complex));
    while (1)
    {
        seq->IM = 0; seq->RE = 0;
        if (scanf("%lf %lf %d", &c->RE, &c->IM, &iterations) != 3) break;
        int in = 1;
        while (iterations-- > 0)
        {
            next(seq, c);
            if (c_len(seq) > 2)
            {
                in = 0;
                break;
            }
        }
        printf("Case %d: %s\n", n++, in ? "IN" : "OUT");
    }
    free(c); free(seq);
    return 0;
}