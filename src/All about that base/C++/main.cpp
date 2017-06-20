#include <iostream>
#include <unordered_map>

#define P '+'
#define D '-'
#define M '*'

char base_char[] = {'\0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                    'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0'};

int value_of_char(char c)
{
    return c < 60 ? c - '0' : 10 + c - 'a';
}

char read_line(std::string& a, std::string& b, std::string& c)
{
    char op, tmp;
    std::cin >> a >> op >> b >> tmp >> c;
    return op;
}

int convert_to_int(const std::string& str, int base)
{
    if (base == 1) return (int)str.length();
    int i = (int)(str.length()) - 1;
    int total = 0;
    int prod = 1;
    while (i >= 0)
    {
        total += prod * value_of_char(str[i]);
        i--;
        prod *= base;
    }
    return total;
}

bool equal(int a, int b, int c, char op)
{
    return op == P ? a + b == c :
           op == D ? a - b == c :
           op == M ? a * b == c :
           a % b == 0 && a / b == c;
}

int find_least(const std::string& str)
{
    bool has_zero = false;
    int min = 1;
    for (std::string::const_iterator it = str.begin(); it != str.end(); ++it)
    {
        int b = value_of_char(*it) + 1;
        if (b == 1) has_zero = true;
        if (b > min) min = b;
    }
    return min == 2 and !has_zero ? 1 : min;
}

int max(int a, int b)
{
    return a < b ? b : a;
}

void test_case()
{
    std::string a, b, c;
    char op = read_line(a,b,c);
    char bases[37];
    int bases_index = 0;
    int start_base = max(max(find_least(a), find_least(b)), find_least(c));
    for (int i = start_base; i < 37; i++)
    {
        if (equal(convert_to_int(a, i), convert_to_int(b, i), convert_to_int(c, i), op))
        {
            bases[bases_index++] = base_char[i];
        }
    }
    bases[bases_index] = '\0';
    if (bases_index == 0) printf("invalid\n");
    else printf("%s\n", bases);
}

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    int n;
    std::cin >> n;
    while(n--) test_case();
    return 0;
}