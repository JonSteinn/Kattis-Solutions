#include <cstdio>
#include <stack>

int main()
{
    std::stack<char> _stack;

    char c;
    while (scanf("%c", &c) != EOF && c != '\n')
    {
        if (c == '<') _stack.pop();
        else _stack.push(c);
    }
    if (_stack.size() > 0)
    {
        char buffer[_stack.size() + 1];
        buffer[_stack.size()] = '\0';
        while (!_stack.empty())
        {
            buffer[_stack.size() - 1] = _stack.top();
            _stack.pop();
        }
        printf("%s", buffer);
    }
    return 0;
}