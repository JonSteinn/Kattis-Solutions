def stage1(not_equal, src_map, dst_map):
    counter = 0
    while src_map['?'] and len(dst_map['1']) > len(src_map['1']):
        found = -1
        for index in src_map['?']:
            if index in dst_map['1']:
                found = index
                break
        if found < 0:
            break
        counter += 1
        src_map['?'].remove(index)
        src_map['1'].add(index)
        not_equal['1'].remove(index)
    return counter
    
def stage2(not_equal, src_map, dst_map):
    counter = 0
    while src_map['?']:
        counter += 1
        index = src_map['?'].pop()
        src_map['0'].add(index)
        if index in dst_map['0']:
            not_equal['0'].remove(index)
    return counter
    
def stage3(not_equal, src_map, dst_map):
    counter = 0
    while len(src_map['1']) != len(dst_map['1']):
        index = not_equal['1'].pop()
        src_map['0'].remove(index)
        src_map['1'].add(index)
        counter += 1
    return counter
    
def stage4(not_equal, src_map, dst_map):
    # not_eq['0'] and not_eq['1] should have equal length so returning
    # either would suffice, but think this is somewhat clearer.
    return (len(not_equal['0']) + len(not_equal['1']))//2
    

def count_moves(not_equal,src_map,dst_map):
    # Can't turn 1s into 0s so impossible if..
    if len(src_map['1']) > len(dst_map['1']):
        return -1
    
    # Strategy:
    #
    # Tuples (a,b) represent same index values from src and dst,
    # (src,dst), and _ is a placeholder for any token.
    #
    # 1. Change (?,1) to (1,1) while src has less ones than dst
    # 2. Change remaining ? to 0, e.g. (?,_) to (0,_)
    # 3. While number of ones, not equal, change (0,1) to (1,1)
    # 4. Swap mismatch
    return sum(func(not_equal, src_map, dst_map) for func in [stage1,stage2,stage3,stage4])


def moves(src,dst,n):
    not_equal = {'0': set(), '1': set()}
    src_map = {'0': set(), '1': set(), '?': set()}
    dst_map = {'0': set(), '1': set()}
    for i in range(n):
        if src[i] != dst[i]:
            not_equal[dst[i]].add(i)
        src_map[src[i]].add(i)
        dst_map[dst[i]].add(i)
    return count_moves(not_equal,src_map,dst_map)

def main():
    for i in range(int(input())):
        src,dst = input(), input()
        print(f'Case {i+1}: {moves(src,dst,len(src))}')

if __name__ == "__main__":
    main()