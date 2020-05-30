import sys
from math import gcd
from collections import Counter, defaultdict
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
        # TODO: wrap into re-usable units
        w = string.find(substr, x+1)
        if w == -1:
            string = string[:x] + string[x+k:]
            if not string:
                self.known.add(substr)
                return True
            z = string.find(substr)
            return False if z == -1 else self._pruner_rec_helper(string, substr, k, z)
        ww = string.find(substr,w+1)
        if ww == -1:
            str1,str2 = string[:x] + string[x+k:], string[:w] + string[w+k:]
            if not str1 or not str2:
                self.known.add(substr)
                return True
            z1,z2 = str1.find(substr), str2.find(substr)
            if z1 == z2 == -1:
                return False
            else:
                return self._pruner_rec_helper(str1, substr, k, z1) or \
                    self._pruner_rec_helper(str2, substr, k, z2)
        if string.find(substr,ww+1) == -1:
            str1,str2,str3 = string[:x] + string[x+k:], string[:w] + string[w+k:], string[:ww] + string[ww+k:]
            if not str1 or not str2 or not str3:
                self.known.add(substr)
                return True
            z1,z2,z3 = str1.find(substr), str2.find(substr), str3.find(substr)
            if z1 == z2 == z3 == -1:
                return False
            else:
                return self._pruner_rec_helper(str1, substr, k, z1) or \
                    self._pruner_rec_helper(str2, substr, k, z2) or \
                    self._pruner_rec_helper(str3, substr, k, z3)
        return True

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
            if l > r:
                self.mem[i][l][r] = StretchedString.FALSE
            elif self.substr[i] != self.string[l]:
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