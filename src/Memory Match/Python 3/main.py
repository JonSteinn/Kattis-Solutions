class MemoryMatch:
    def __init__(self, n):
        self.cards = n
        self.ones = {}
        self.twos = set()

    def flip(self,c1,c2,p1,p2):
        if p1 == p2:
            self.__discard(p1)
        else:
            self.__update_knowledge(c1,c2,p1,p2)
            
    def __update_knowledge(self,c1,c2,p1,p2):
        self.__update_knowledge_single(c1,p1)
        self.__update_knowledge_single(c2,p2)
        
    def __update_knowledge_single(self,c,p):
        if p in self.ones:
            if self.ones[p] != c:
                del self.ones[p]
                self.twos.add(p)
                self.cards -= 1
        elif p not in self.twos:
            self.ones[p] = c
            self.cards -= 1

    def __discard(self,p):
        if p in self.twos:
            self.twos.discard(p)
        elif p in self.ones:
            del self.ones[p]
            self.cards -= 1
        else:
            self.cards -= 2

    def known(self):
        # Unflipped known pairs
        k = len(self.twos)
        # If there are two lefts and no singles known, they are the same
        if self.cards == 2 and not self.ones:
            k += 1
        # If we know X single cards and there are also X unknown, we pick
        # from the unknown and then the matching known, until we have all
        # the X pairs
        elif self.cards == len(self.ones):
            k += self.cards

        return k

def main():
    n,k = int(input()),int(input())
    mm = MemoryMatch(n)
    for _ in range(k):
        *c,p1,p2 = input().split()
        mm.flip(*map(int,c),p1,p2)
    print(mm.known())

if __name__ == "__main__":
    main()