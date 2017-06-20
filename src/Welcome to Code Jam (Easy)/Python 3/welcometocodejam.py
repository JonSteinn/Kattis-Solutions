msg = 'welcome to code jam'
msg_len = len(msg)


def msg_counter(sentence, start=0):
    counter = 0
    if start == msg_len - 1:
        for i in sentence:
            if i == 'm':
                counter += 1
        return counter
    for i in enumerate(sentence):
        if i[1] == msg[start]:
            counter += msg_counter(sentence[i[0] + 1:], start + 1)
    return counter


for test_case in range(1, int(input()) + 1):
    val = msg_counter(input())
    if val < 10:
        print("Case #{0}: 000{1}".format(test_case, val))
    elif val < 100:
        print("Case #{0}: 00{1}".format(test_case, val))
    elif val < 1000:
        print("Case #{0}: 0{1}".format(test_case, val))
    else:
        print("Case #{0}: {1}".format(test_case, val))
