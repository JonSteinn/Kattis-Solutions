array = [1, 1000, 12, 3, 22, 10, 8, 3] #List storing values of the units
units = {
    'thou': 0, 'th': 0,
    'inch': 1, 'in': 1,
    'foot': 2, 'ft': 2,        #dictionary with assigned values to make it easier to iterate.
    'yard': 3, 'yd': 3,
    'chain': 4, 'ch': 4,
    'furlong': 5, 'fur': 5,
    'mile': 6, 'mi': 6,
    'league': 7, 'lea': 7
}

s = input().split()
val = int(s[0]) #isolating number
u1 = units[s[1]]  #linking unit with dictionary
u2 = units[s[3]]  #linking unit 2 with dictionary
if u1 == u2:
    print(val) #considering that both can be same units
elif u1 < u2:
    variable = 1
    while u1 != u2:
        u1 += 1
        variable /= lis[f] #diving variable by the values repeatedly till f is same as t. This willl be the same value as dividing the the number repeatedly
    print(variable * val)  #printing end product
else:
    variable = 1
    while u1 != u2:
        variable *= array[u1] #multiplying p by the values repeatedly till f is same as t. This willl be the same value as multiplying the the number repeatedly
        u1 -= 1
    print(variable * val)
