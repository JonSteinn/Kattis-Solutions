#include <stdio.h>

int main()
{
	long long a, b;
	while (scanf("%lld%lld", &a, &b) == 2) printf("%lld\n", b < a ? a - b : b - a);
	return 0;
}