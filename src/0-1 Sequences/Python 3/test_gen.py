from random import choice,uniform

class BF:
    @staticmethod
    def inv(bstr):
        counter = 0
        for i,c in enumerate(bstr):
            if c == '1':
                for o in bstr[i+1:]:
                    if o == '0':
                        counter += 1
        return counter

    @staticmethod
    def bf_rec_helper(bstr, qs):
        if not qs:
            return BF.inv(bstr)
        else:
            some_q = qs.pop()
            bstr[some_q] = '0'
            x = BF.bf_rec_helper(bstr, qs)
            bstr[some_q] = '1'
            x += BF.bf_rec_helper(bstr, qs)
            bstr[some_q] = '?'
            qs.add(some_q)
            return x
        
    @staticmethod
    def brute_force_for_test_cases(bstr):
        questions = {i for i,c in enumerate(bstr) if c == '?'}
        return BF.bf_rec_helper(list(bstr), questions)


class TestGen:
    H = [chr(ord('a') + i) for i in range(26)] + [chr(ord('A') + i) for i in range(26)] + ['_']
    BIN = '01?'

    @staticmethod
    def h(n):
        return ''.join((choice(TestGen.H) for _ in range(n)))

    @staticmethod
    def b(n):
        return ''.join((choice(TestGen.BIN) for _ in range(n)))

    @staticmethod
    def iu(a,b):
        return int(uniform(a,b+1))
    
    @staticmethod
    def generate_tests(n,a,b):
        for _ in range(n):
            b_str = TestGen.b(TestGen.iu(a,b))
            res = BF.brute_force_for_test_cases(b_str)
            # Might want to edit this to write to file.... 
            print(' '*4 + f'def test_{TestGen.h(15)}(self):\n' + ' '*8 + f'self.assertEqual(inversions(\'{b_str}\'), {res % (10**9+7)})\n')

    @staticmethod
    def generate_test_for_a_specific_string(b_str):
            res = BF.brute_force_for_test_cases(b_str)
            # Might want to edit this to write to file.... 
            print(' '*4 + f'def test_{TestGen.h(15)}(self):\n' + ' '*8 + f'self.assertEqual(inversions(\'{b_str}\'), {res % (10**9+7)})\n')


def main():
    """ All length 1-3 cases
    for b in ['0','1','?','00','01','0?','10','11','1?','?0','?1','??']:
        TestGen.generate_test_for_a_specific_string(b)
    for a in ['0','1','?']:
        for b in ['0','1','?']:
            for c in ['0','1','?']:
                TestGen.generate_test_for_a_specific_string(a+b+c)
    """

    # Generate multiple
    TestGen.generate_tests(200, 7, 15)

    # Generate single
    # Dont go much higher than 65ish, bruteforce is slow as f
    #TestGen.generate_test_for_a_specific_string(TestGen.b(66))

if __name__ == "__main__":
    main()