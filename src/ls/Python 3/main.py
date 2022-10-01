from typing import Dict, Tuple


class Pattern:
    cache: Dict[Tuple[str, str], bool] = {}

    def __init__(self, patt: str) -> None:
        self.patt = patt

    def check(self, word: str) -> bool:
        return Pattern._checker(self.patt, word)

    @staticmethod
    def _checker(patt: str, word: str) -> bool:
        if not patt and not word:
            return True
        if not patt:
            return False
        if not word:
            return patt[0] == "*" and patt == len(patt) * patt[0]
        if patt[0] != "*" and patt[0] != word[0]:
            return False
        res = Pattern.cache.get((patt, word), None)
        if res is None:
            if patt[0] == "*":
                res = (
                    Pattern._checker(patt[1:], word[1:])
                    or Pattern._checker(patt[1:], word)
                    or Pattern._checker(patt, word[1:])
                )
            else:
                res = Pattern._checker(patt[1:], word[1:])
            Pattern.cache[(patt, word)] = res
        return res


patt = Pattern(input())
contenters = (input() for _ in range(int(input())))
for contenter in contenters:
    if patt.check(contenter):
        print(contenter)
