/*

// My initial attempt until I realized the actual value n can be... what fresh hell is this...

#include <stdio.h>

typedef long long ll;
const ll MOD = 1000000007;

ll f(ll n) {
  ll arr[4] = {1, 5, 17, 63};
  if (n < 4)
      return arr[n];
  for (ll i = 3; i < n; i++) {
    arr[0] = (MOD + (arr[3] << 1) + (arr[2] << 1) + (arr[2] << 2) - arr[0]) % MOD;
    arr[0] ^= arr[1] ^= arr[0] ^= arr[1];
    arr[1] ^= arr[2] ^= arr[1] ^= arr[2];
    arr[2] ^= arr[3] ^= arr[2] ^= arr[3];
  }
  return arr[3];
}

int main(void) {
  ll n;
  scanf("%lld", &n);
  printf("%lld\n", f(n));
  return 0;
}

*/

//////////////////////////////////////////////////////////////////////////

/*
A = comb class desribed
A = disjoint_union(classes starting with...)
etc

combinatorial specification => solve for A => get GF/recurrence relation => profit

f(n) = 2f(n-1) + 6f(n-2) - f(n-4)

with such a large n we will need to convert this to a matrix equation and use
power by squaring

| 2  6  0  -1 |   | f(n-1) |   | 2f(n-1)+6f(n-2)-f(n-34) |   | f(n)   |
| 1  0  0   0 |   | f(n-2) |   | f(n-1)                  |   | f(n-1) |
| 0  1  0   0 | * | f(n-3) | = | f(n-2)                  | = | f(n-2) |
| 0  0  1   0 |   | f(n-4) |   | f(n-3)                  |   | f(n-3) |

so if
    | 2  6  0  -1 |       | 63 |
    | 1  0  0   0 |       | 17 |
M = | 0  1  0   0 |   v = | 5  |
    | 0  0  1   0 |       | 1  |
then M^(n-3) * v will hold the answer at position 0 for n > 3 (answers in v for other cases).

*/

#include <stdio.h>
#include <string.h>

typedef long long ll;

const ll MOD = 1000000007;

typedef struct {
    ll data[4][4];
} mat4;

typedef struct {
    ll data[4];
} vec4;

/* Store result in rhs */
void mat_prod(mat4 *lhs, mat4 *rhs) {
    ll a, b, c, d;
    for (int i = 0; i < 4; i++) {
        a = lhs->data[0][0] * rhs->data[0][i] +
            lhs->data[0][1] * rhs->data[1][i] +
            lhs->data[0][2] * rhs->data[2][i] +
            lhs->data[0][3] * rhs->data[3][i];

        b = lhs->data[1][0] * rhs->data[0][i] +
            lhs->data[1][1] * rhs->data[1][i] +
            lhs->data[1][2] * rhs->data[2][i] +
            lhs->data[1][3] * rhs->data[3][i];

        c = lhs->data[2][0] * rhs->data[0][i] +
            lhs->data[2][1] * rhs->data[1][i] +
            lhs->data[2][2] * rhs->data[2][i] +
            lhs->data[2][3] * rhs->data[3][i];

        d = lhs->data[3][0] * rhs->data[0][i] +
            lhs->data[3][1] * rhs->data[1][i] +
            lhs->data[3][2] * rhs->data[2][i] +
            lhs->data[3][3] * rhs->data[3][i];

        rhs->data[0][i] = (MOD + a) % MOD;
        rhs->data[1][i] = (MOD + b) % MOD;
        rhs->data[2][i] = (MOD + c) % MOD;
        rhs->data[3][i] = (MOD + d) % MOD;
    }
}

/* Store result in self */
void mat_square(mat4 *mat) {
    mat4 tmp;
    memcpy(&tmp, mat, sizeof(mat4));
    mat_prod(&tmp, mat);
}

// Too lazy to change this but this requires identity mat as input
// and us defining our matrix within the function...
void mat_pow(mat4 *odds, ll n) {
    mat4 mat = {.data = {{2LL, 6LL, 0LL, -1LL},
                         {1LL, 0LL, 0LL, 0LL},
                         {0LL, 1LL, 0LL, 0LL},
                         {0LL, 0LL, 1LL, 0LL}}};
    while (n > 1) {
        if (n & 1) {
            mat_prod(&mat, odds);
            mat_square(&mat);
            n = (n - 1) / 2;
        } else {
            mat_square(&mat);
            n /= 2;
        }
    }
    mat_prod(&mat, odds);
}

int g(ll n, vec4 *vec) {
    mat4 mat = {.data = {{1LL, 0LL, 0LL, 0LL},
                         {0LL, 1LL, 0LL, 0LL},
                         {0LL, 0LL, 1LL, 0LL},
                         {0LL, 0LL, 0LL, 1LL}}};
    mat_pow(&mat, n);
    return (mat.data[0][0] * vec->data[0] + mat.data[0][1] * vec->data[1] +
            mat.data[0][2] * vec->data[2] + mat.data[0][3] * vec->data[3]) %
        MOD;
}

ll f(ll n) {
    vec4 vec = {.data = {63LL, 17LL, 5LL, 1LL}};
    if (n < 4)
        return vec.data[3 - n];
    return g(n - 3, &vec);
}

int main() {
    ll n;
    scanf("%lld", &n);
    printf("%lld\n", f(n));
    return 0;
}