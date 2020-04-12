from collections import deque

def main():
    n,k = map(int,input().split())
    most = -1
    tasks = deque()
    for _ in range(n):
        task = int(input())
        while tasks and task - tasks[0] >= 1000:
            tasks.popleft()
        tasks.append(task)
        most = max(most, len(tasks))
    print(most//k + (0 if most % k == 0 else 1))

if __name__ == "__main__":
    main()