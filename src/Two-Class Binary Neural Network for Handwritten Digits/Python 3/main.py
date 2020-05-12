import numpy as np
from random import uniform, shuffle, sample
import os
from tqdm import tqdm
from itertools import combinations

class IO:
    @staticmethod
    def read_train_data():
        X = np.array([],dtype=int).reshape(0,51)
        Y = np.array([],dtype=int)
        with open(f'{os.path.dirname(__file__)}/train.txt', 'r') as f:
            for line in tqdm(f.readlines()):
                *xs, y = map(int, line.split())
                Y=np.append(Y, y)
                X=np.append(X, [xs], axis=0)
        return X,Y

    @staticmethod
    def read_weights():
        def r():
            return 1 if uniform(0,1) < 0.5 else -1
        with open(f'{os.path.dirname(__file__)}/weights.txt', 'r') as f:
            lines = f.readlines()
        if len(lines) < 30:
            return np.array([[r() for _ in range(51)] for _ in range(30)])
        try:
            return np.array([list(map(int, line.split())) for line in lines])
        except Exception:
            return np.array([[r() for _ in range(51)] for _ in range(30)])

    @staticmethod
    def write_weights(W):
        with open(f'{os.path.dirname(__file__)}/weights.txt', 'w') as f:
            for row in W:
                f.write(f'{" ".join((str(x) for x in row))}\n')
def correct(W,X,Y):
    M = np.sign(np.matmul(W,X.transpose()))
    return np.sum(Y==np.argmax(np.stack((np.sum(M[:15],axis=0), np.sum(M[15:],axis=0)), axis=0),axis=0))

class Tactics:
    @staticmethod
    def tactic1(w_indices, W, X, Y, curr):
        for a,b in tqdm(w_indices):
            W[a][b] = -W[a][b]
            z = correct(W,X,Y)
            if z < curr:
                W[a][b] = -W[a][b]
            else:
                curr = z
        return curr

    @staticmethod
    def tactic2(w_indices, W, X, Y, curr):
        for (a,b), (c,d), (e,f) in tqdm(combinations(w_indices, 3)):
            W[a][b] = -W[a][b]
            W[c][d] = -W[c][d]
            W[e][f] = -W[e][f]
            z = correct(W,X,Y)
            if z < curr:
                W[a][b] = -W[a][b]
                W[c][d] = -W[c][d]
                W[e][f] = -W[e][f]
            else:
                if z > curr:
                    # this tasks are so long... write here so we can interupt
                    print('Found Better!')
                    IO.write_weights(W)
                curr = z
        return curr

    @staticmethod
    def tactic3(w_indices, W, X, Y, curr):
        for (a,b), (c,d) in tqdm(combinations(w_indices, 2)):
            W[a][b] = -W[a][b]
            W[c][d] = -W[c][d]
            z = correct(W,X,Y)
            if z < curr:
                W[a][b] = -W[a][b]
                W[c][d] = -W[c][d]
            else:
                if z > curr:
                    # this tasks are so long... write here so we can interupt
                    print('Found Better!')
                    IO.write_weights(W)
                curr = z
        return curr

    @staticmethod
    def tactic4(w_indices, W, X, Y, curr, a=2, b=5):
        for _ in tqdm(range(min(len(w_indices)//3, int(uniform(10,len(w_indices)))))):
            pairs = sample(w_indices, int(uniform(a,b)))
            for a,b in pairs:
                W[a][b] = -W[a][b]
            z = correct(W,X,Y)
            if z < curr:
                for a,b in pairs:
                    W[a][b] = -W[a][b]
            else:
                if z > curr:
                    # this tasks are so long... write here so we can interupt
                    print('Found Better!')
                    IO.write_weights(W)
                curr = z
        return curr

    @staticmethod
    def tactic5(w_indices, W, X, Y, curr):
        a,b = 0,0
        while a >= b:
            a = int(uniform(0,len(w_indices)))
            b = int(uniform(0,len(w_indices)))
        return Tactics.tactic4(w_indices, W, X, Y, curr, a, b)

    @staticmethod
    def tactic6(w_indices, W, X, Y, curr):
        return Tactics.tactic4(w_indices, W, X, Y, curr, 5, 7)

def train_by_tactic(tactic,it=100):
    X,Y = IO.read_train_data()
    W = IO.read_weights()
    curr = correct(W,X,Y)
    w_indices = [(j,i) for i in range(51) for j in range(30)]
    for _ in tqdm(range(it)):
        shuffle(w_indices)
        n_curr = tactic(w_indices, W, X, Y, curr)
        if n_curr >= curr:
            if n_curr > curr:
                # Might wanna comment this out at first, then new findings become rare
                print('Found Better!')
            IO.write_weights(W)
            curr = n_curr

def train():
    #train(tactic1,it=1)
    #train(tactic2,it=1)
    #train(tactic3,it=1)
    while True:
        train_by_tactic(Tactics.tactic4,it=10)
        train_by_tactic(Tactics.tactic5,it=10)
        train_by_tactic(Tactics.tactic6,it=1)

# After some amount of training...
def print_weight():
    print("""-1 1 -1 -1 -1 -1 -1 1 -1 -1 -1 1 -1 -1 -1 -1 -1 -1 1 -1 -1 -1 1 1 1 1 1 1 1 -1 1 1 1 -1 1 -1 1 -1 1 -1 1 1 -1 -1 -1 -1 -1 1 1 1 -1
1 1 1 -1 1 -1 -1 1 1 1 -1 -1 -1 1 1 1 1 -1 1 -1 1 -1 1 1 1 -1 -1 1 -1 1 1 1 -1 -1 -1 -1 -1 -1 1 1 -1 -1 -1 -1 -1 1 -1 -1 -1 -1 -1
1 1 1 -1 1 1 -1 -1 1 -1 1 -1 1 1 1 -1 -1 1 1 1 -1 1 1 -1 1 1 -1 -1 1 -1 1 1 -1 1 -1 -1 1 1 -1 -1 -1 1 1 -1 1 -1 -1 -1 1 1 1
-1 1 1 1 1 1 -1 -1 1 1 1 1 1 -1 1 1 1 1 1 1 1 1 1 1 1 -1 1 1 -1 1 1 1 -1 -1 -1 -1 1 1 1 1 -1 -1 -1 1 1 -1 -1 -1 1 -1 1
1 1 1 -1 1 -1 -1 1 1 1 -1 -1 -1 -1 -1 -1 -1 1 1 -1 1 1 -1 1 1 1 -1 -1 1 -1 1 1 1 -1 1 1 -1 1 1 -1 1 1 1 1 -1 -1 -1 -1 1 -1 1
-1 1 -1 -1 1 -1 -1 1 1 1 -1 1 -1 1 1 -1 -1 1 1 1 1 -1 -1 -1 1 1 -1 1 1 -1 1 1 -1 -1 -1 1 1 1 1 1 -1 -1 1 1 1 -1 -1 -1 1 -1 1
1 -1 1 -1 -1 -1 -1 -1 1 1 -1 1 -1 1 -1 1 1 1 -1 -1 -1 1 -1 -1 -1 -1 -1 1 -1 -1 -1 1 1 1 1 -1 -1 -1 -1 -1 -1 1 1 -1 1 1 -1 1 1 1 1
1 -1 1 -1 1 -1 -1 -1 1 -1 -1 1 1 -1 -1 -1 -1 1 -1 -1 -1 -1 -1 -1 -1 1 1 -1 -1 -1 1 1 1 1 1 1 1 -1 1 1 1 -1 -1 -1 -1 1 -1 -1 -1 1 1
1 1 1 -1 -1 -1 1 1 1 -1 -1 1 -1 -1 -1 1 -1 -1 1 1 -1 -1 1 -1 1 1 1 -1 -1 1 1 -1 1 1 1 1 1 1 -1 1 1 1 1 1 1 1 1 1 1 1 1
-1 -1 1 1 1 -1 -1 -1 -1 -1 -1 1 1 -1 1 1 1 1 1 -1 -1 -1 -1 -1 1 1 1 1 1 -1 1 -1 1 1 1 -1 1 1 -1 1 1 1 1 -1 1 -1 -1 1 1 -1 -1
1 1 -1 -1 1 -1 -1 -1 -1 -1 -1 1 1 -1 -1 -1 -1 -1 1 -1 1 1 1 1 1 -1 -1 1 -1 -1 1 -1 1 -1 -1 -1 1 -1 -1 1 -1 1 1 -1 -1 -1 -1 1 -1 -1 -1
-1 1 1 -1 1 -1 -1 1 -1 -1 1 1 -1 -1 1 -1 -1 -1 1 -1 1 -1 -1 -1 1 1 -1 1 -1 -1 1 -1 1 1 -1 -1 -1 -1 -1 -1 1 -1 -1 -1 -1 1 -1 1 -1 1 1
1 1 -1 -1 -1 -1 -1 1 1 1 1 1 1 -1 -1 1 1 1 1 1 -1 1 -1 -1 1 1 1 -1 -1 -1 -1 -1 1 1 1 1 1 -1 1 1 1 1 -1 1 1 -1 -1 1 -1 1 1
1 1 1 -1 -1 -1 1 1 1 1 -1 -1 -1 1 1 -1 1 1 -1 -1 1 1 -1 -1 1 -1 1 -1 -1 1 -1 1 -1 1 -1 -1 1 1 -1 -1 1 -1 1 1 1 -1 1 -1 1 1 -1
1 1 1 -1 1 -1 -1 -1 1 -1 1 -1 -1 1 1 -1 1 -1 1 1 -1 1 1 -1 -1 -1 -1 1 -1 -1 1 -1 1 -1 -1 1 -1 1 1 -1 1 1 1 -1 -1 -1 -1 1 1 1 1
-1 -1 -1 1 -1 1 1 1 -1 1 -1 -1 -1 -1 -1 -1 1 1 -1 1 1 1 1 -1 -1 1 -1 -1 -1 1 1 -1 1 -1 -1 -1 -1 -1 1 1 -1 1 1 -1 -1 -1 -1 -1 1 -1 1
-1 1 -1 1 1 1 1 1 1 -1 -1 -1 -1 -1 -1 1 1 -1 1 -1 -1 -1 1 -1 1 -1 -1 1 1 1 -1 1 -1 1 -1 -1 1 -1 -1 -1 -1 1 -1 1 -1 1 1 -1 1 1 1
1 1 1 1 -1 -1 1 1 -1 1 1 1 -1 -1 1 -1 -1 -1 -1 1 -1 1 -1 -1 -1 -1 1 1 1 1 1 -1 -1 1 1 -1 -1 -1 -1 -1 1 -1 -1 -1 -1 -1 1 -1 -1 1 1
-1 -1 1 1 -1 1 1 1 -1 1 1 1 -1 1 -1 -1 1 -1 -1 -1 -1 -1 -1 1 1 -1 1 -1 -1 1 -1 1 1 -1 1 -1 -1 1 1 1 -1 -1 1 -1 -1 -1 1 -1 1 -1 1
1 1 1 1 1 -1 -1 -1 -1 -1 -1 -1 -1 1 1 1 -1 -1 1 -1 -1 -1 1 -1 -1 1 1 1 1 -1 1 1 -1 -1 -1 -1 -1 -1 1 -1 -1 -1 -1 -1 -1 -1 1 1 -1 -1 1
-1 1 -1 1 1 1 1 -1 -1 1 1 -1 1 1 -1 -1 -1 -1 -1 1 -1 -1 1 1 1 1 1 1 -1 -1 -1 -1 -1 1 1 1 1 -1 1 1 1 1 1 1 1 1 1 -1 1 1 -1
-1 -1 1 1 -1 1 1 -1 -1 -1 -1 1 1 1 1 -1 1 1 -1 -1 1 -1 1 -1 1 -1 -1 -1 1 -1 1 -1 -1 -1 1 -1 -1 -1 1 1 -1 -1 -1 1 -1 -1 1 1 1 -1 -1
-1 1 -1 1 1 1 1 1 -1 -1 -1 1 -1 -1 -1 -1 -1 1 1 -1 -1 1 -1 1 -1 1 -1 1 1 -1 1 1 -1 -1 -1 1 -1 1 -1 1 -1 1 -1 -1 -1 1 1 1 -1 -1 1
-1 -1 1 1 -1 1 1 1 1 -1 -1 1 -1 1 -1 1 1 -1 -1 1 1 -1 1 1 -1 -1 -1 1 1 -1 -1 -1 1 -1 1 -1 1 1 1 1 -1 -1 1 -1 1 1 1 1 -1 -1 1
1 1 -1 1 1 1 -1 -1 -1 -1 1 -1 1 1 1 -1 -1 -1 -1 -1 1 1 -1 1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 1 1 1 1 -1 1 1 -1 -1 -1 -1 -1 -1 1 1 -1 -1
-1 -1 1 -1 1 1 1 -1 -1 -1 -1 -1 -1 1 1 -1 1 1 -1 1 -1 1 1 1 1 -1 -1 -1 -1 -1 1 1 1 -1 -1 1 1 -1 -1 1 1 -1 1 1 -1 -1 -1 1 -1 -1 1
-1 1 -1 1 -1 1 1 1 -1 -1 1 1 1 1 1 -1 1 1 -1 1 1 -1 -1 -1 -1 1 -1 -1 -1 1 -1 -1 -1 -1 1 1 1 -1 -1 1 -1 -1 -1 1 -1 1 -1 -1 -1 1 -1
-1 1 1 1 -1 1 1 1 -1 -1 1 -1 1 -1 -1 1 1 1 -1 -1 1 1 -1 1 -1 -1 -1 1 1 1 -1 -1 -1 -1 -1 1 1 -1 1 -1 -1 -1 -1 1 -1 -1 1 -1 -1 1 -1
-1 -1 -1 1 -1 1 -1 1 -1 1 1 -1 1 -1 -1 1 -1 1 1 -1 -1 -1 -1 -1 1 -1 -1 -1 -1 -1 -1 1 1 -1 1 -1 -1 -1 -1 -1 -1 -1 1 1 -1 -1 1 1 1 -1 -1
-1 -1 -1 1 -1 1 1 -1 -1 -1 -1 1 1 1 1 1 1 1 -1 1 1 1 -1 -1 -1 1 -1 1 1 1 1 1 1 -1 1 -1 -1 1 -1 1 -1 1 -1 -1 -1 -1 -1 1 1 1 -1""")

def main():
    #train()
    print_weight()

if __name__ == "__main__":
    main()
