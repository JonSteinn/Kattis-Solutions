def run():
    d = tuple(map(int, input().split()))[1]
    for i, k in enumerate(input().split()):
        if int(k) <= d:
            return i
    return -1

smaller_run = run()
if smaller_run == -1:
    print('It had never snowed this early!')
else:
    print(f"It hadn't snowed this early in {smaller_run} years!")