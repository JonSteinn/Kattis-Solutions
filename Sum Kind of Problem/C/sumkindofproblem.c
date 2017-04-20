#include <stdio.h>

// 1+2+...+n = n(n+1)/2 = (n^2+n)/2
// 1+3+...+2n-1 = ((2-1) + (4-1) + ... + (2n-1)) = (2+4+...2n)-n = 2(1+2+...+n)-n = 2n(n+1)/2-n = n^2
// 2+4+...+2n = 2(1+2+...+n) = 2n(n+1)/2 = n(n+1) = n^2+n

int main()
{
	int n, i;
	scanf("%d",&n);
	while (n-- > 0)
	{
		int K, N;
		scanf("%d %d",&K,&N);
		int sq = N*N;
		printf("%d %d %d %d\n",K,(sq+N)>>1,sq,sq+N);
	}
	return 0;
}