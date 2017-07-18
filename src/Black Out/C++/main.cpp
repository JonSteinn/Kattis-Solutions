#include <iostream>

int main()
{
    int n;
    std::cin >> n;
    while(n--)
    {
        std::cout << "5 1 5 6" << std::endl;
        while(1)
        {
            std::string command;
            std::cin >> command;
            if (*command.begin() == 'G') break;
            int r1, c1, r2, c2;
            std::cin >>  r1 >> c1 >> r2 >> c2;
            if (r2 == 5) r2 = 4;
            std::cout << 5 - r2 << " " << 7 - c2 << " " << 5 - r1 << " " << 7 - c1 << std::endl;
        }
    }
    return 0;
}