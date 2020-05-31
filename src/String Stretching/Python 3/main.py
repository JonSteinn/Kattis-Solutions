import sys
from math import gcd
from collections import Counter
from functools import reduce

class StretchedString:
    TRUE = 1
    FALSE = -1
    UNCERTAIN = 0

    def __init__(self, string):
        self.string = string
        self.ratios = self._construct_ratios(string)
        self.left_order = self._get_order(string)
        self.right_order = self._get_order(reversed(string))
        self.mem = []
        self.substr = ''
        self.known = set()
        self.sstrl = 0

    def de_stretch(self):
        if 1 in self.ratios:
            return self.string[0]
        if len(self.ratios) == 1:
            return self.string

        for substr in self._valid_substrings():
            if self._is_stretchable(substr):
                return substr
        return self.string

    def _get_order(self, string):
        lis, s = [], set()
        for c in string:
            if c not in s:
                lis.append(c)
                s.add(c)
        return lis

    def _construct_ratios(self, string):
        ratio = Counter(string)
        d = reduce(gcd, set(Counter(string).values()))
        
        return {
            len(string)//factor: Counter({a: b//factor for a,b in ratio.items()}) 
                for factor in set(reduce(list.__add__, ([i, d//i] for i in range(1, int(d**0.5) + 1) if not d % i)))
        }

    def _valid_substrings(self):
        repeats = set()
        for k in sorted(self.ratios.keys())[:-1]:
            for substr in self._sorted_valid_substrings_of_length_k(k):
                valid = True
                for reap in repeats:
                    if reap * (len(substr)//len(reap)) == substr:
                        valid = False
                if valid:
                    repeats.add(substr)
                    yield substr

    def _sorted_valid_substrings_of_length_k(self,k):
        valid = set()
        for i in range(len(self.string)-k+1):
            substr = self.string[i:i+k]
            if substr in valid:
                continue
            if self._is_valid_substr(substr,k,i):
                valid.add(substr)
        for sstr in sorted(valid):
            yield sstr

    def _is_valid_substr(self,substr,k,i):
        return self.left_order == self._get_order(substr) and \
            self.right_order == self._get_order(reversed(substr)) and \
            Counter(substr) == self.ratios[k] and \
            (self.left_order == self._get_order(self.string[:i]+self.string[i+k:])) and \
            (self.right_order == self._get_order(reversed(self.string[:i]+self.string[i+k:]))) and \
            self._pruner(substr,k,i)

    def _pruner(self,substr,k,i):
        rem_string = self.string[:i]+self.string[i+k:]
        x = rem_string.find(substr)
        return False if x == -1 else self._pruner_rec_helper(rem_string,substr, k, x)

    def _pruner_rec_helper(self, string, substr, k, x):
        lis = [x]
        while len(lis) < 5 and lis[-1] != -1:
            lis.append(string.find(substr, lis[-1]+1))
        if lis[-1] != -1:
            return True
        lis.pop()
        strings = [string[:z] + string[z+k:] for z in lis]
        if any(not z for z in strings):
            self.known.add(substr)
            return True
        zs = [s.find(substr) for s in strings]
        return False if set(zs) == {-1} else any(self._pruner_rec_helper(s, substr, k, z) for s,z in zip(strings,zs))

    def _is_stretchable(self,substr):
        if substr in self.known:
            return True
        self.mem = self._init_memory_for_substr(substr)
        self.substr = substr
        self.sstrl = len(self.substr)
        return self._dp(0,0,len(self.string))

    def _init_memory_for_substr(self, substr):
        return [
            [
                [StretchedString.UNCERTAIN] * (1+len(self.string)) 
                    for _ in range(1+len(self.string))
            ] for _ in range(len(substr))
        ]

    # Can this 'de-stretching' be done such that the substr at place i starts at l and ends at r ? 
    def _dp(self,i,l,r):
        if i == self.sstrl:
            return l==r
        if self.mem[i][l][r] == StretchedString.UNCERTAIN:
            if self.substr[i] != self.string[l] or self.substr[-1]!= self.substr[r-1]:
                self.mem[i][l][r] = StretchedString.FALSE
            elif self._dp(i+1, l+1, r):
                self.mem[i][l][r] = StretchedString.TRUE
            else:
                self.mem[i][l][r] = StretchedString.TRUE if any(
                    self._dp(0, l+1, l+1+offset) and self._dp(i+1, l+1+offset, r) 
                        for offset in range(self.sstrl, r-l-self.sstrl+i+1, self.sstrl)
                ) else StretchedString.FALSE 
        return self.mem[i][l][r] == StretchedString.TRUE

def main():
    sys.setrecursionlimit(1_000_000)
    print(StretchedString(input()).de_stretch())

if __name__ == "__main__":
    main()