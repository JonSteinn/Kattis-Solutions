#include <stdio.h>
#include <string.h>

char getForward(char c, int n)
{
	if (n == 0) return c;
	if (c == '_') return n == 1 ? '.' : getForward('A', n-2);
	if (c == '.') return getForward('A', n-1);
	if (c == 'Z') return n == 1 ? '_' : (n == 2 ? '.' : getForward('A', n-3));	
	if (c + n <= 90) return c + n;
	return getForward('Z', n + c - 90);
}

int main()
{
	while (1) 
	{
		int n;
		scanf("%d", &n);
		if (!n) break;

		char str[41];
		scanf("%s", str);
		size_t len = strlen(str);
		str[len] = '\0';

		char output[41];
		int i;
		for (i = len - 1; i >= 0; i--) 
		{
			output[len - 1 - i] = getForward(str[i], n);
		}
		output[len] = '\0';
		printf("%s\n", output);
	}

	return 0;
}