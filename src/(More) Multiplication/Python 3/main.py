class Multiplication:

    @staticmethod
    def create_base_mat(la,lb):
        mat = [['+'] + ['-']*(3+4*la) + ['+'], ['|'] + [' ']*(3+4*la) + ['|']]
        mat.append(list(f"| +{'+'.join(('---' for _ in range(la)))}+ |"))
        for _ in range(lb):
            mat.append(list(f"| |{'|'.join(('  /' for _ in range(la)))}| |"))
            mat.append(list(f"| |{'|'.join((' / ' for _ in range(la)))}| |"))
            mat.append(list(f"| |{'|'.join(('/  ' for _ in range(la)))}| |"))
            mat.append(list(f"| +{'+'.join(('---' for _ in range(la)))}+ |"))
        mat.append(mat[1].copy())
        mat.append(mat[0])
        return mat

    @staticmethod
    def add_numbers(mat,a,b):
        for i,x in enumerate(a):
            mat[1][4+i*4] = x
        for i,x in enumerate(b):
            mat[4+i*4][-2] = x

    @staticmethod
    def add_result(mat,a,b):
        res = list('/'.join(str(int(a)*int(b))))
        for i in range(3+(len(a)-1)*4,0,-2):
            if res:
                mat[-2][i] = res.pop()
        i = 0
        while res:
            mat[-4-i][1] = res.pop()
            i += 2

    @staticmethod
    def add_steps(mat, a, b):
        for _c,x in enumerate(a):
            for _r,y in enumerate(b):
                d,m = divmod((ord(x)-48) * (ord(y)-48),10)
                mat[3+_r*4][3+_c*4] = chr(d+48)
                mat[5+_r*4][5+_c*4] = chr(m+48)

    @staticmethod
    def create_table(a,b):
        mat = Multiplication.create_base_mat(len(a),len(b))
        Multiplication.add_numbers(mat,a,b)
        Multiplication.add_result(mat,a,b)
        Multiplication.add_steps(mat,a,b)    

        return mat

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        mat = Multiplication.create_table(self.a,self.b)
        return '\n'.join(''.join(x for x in row) for row in mat)

def main():
    while True:
        a,b = input().split()
        if a == b == '0':
            break
        print(Multiplication(a,b))

if __name__ == "__main__":
    main()