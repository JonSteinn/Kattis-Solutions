#include <iostream>
#include <list>
#include <stdio.h>

void fast_io() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(NULL);
  std::cout.tie(NULL);
}

int main() {
  fast_io();
  std::string s;
  std::cin >> s;

  std::list<char> lis;
  auto lis_it = lis.begin();

  for (auto it = s.begin(); it != s.end(); ++it) {
    switch (*it) {
    case 'B':
      lis_it = lis.erase(--lis_it);
      break;
    case 'L':
      --lis_it;
      break;
    case 'R':
      ++lis_it;
      break;
    default:
      lis.insert(lis_it, *it);
      break;
    }
  }

  for (auto it = lis.begin(); it != lis.end(); ++it) {
    printf("%c", *it);
  }
  putchar('\n');

  return 0;
}