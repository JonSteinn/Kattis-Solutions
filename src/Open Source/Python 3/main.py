from collections import defaultdict
import sys 

def main():
    students, projects, curr = {}, defaultdict(set),None
    for line in sys.stdin:
        if line[0] == '0':
            break
        elif line[0] == '1':
            for x,y in sorted(((a,len(b)) for a,b in projects.items()),key=lambda z: (-z[1],z[0])):
                print(f'{x} {y}')
            students, projects = {}, defaultdict(set)
        elif line[0].isupper():
            curr = line[:-1]
            projects[curr]
        else:
            s = line[:-1]
            if s in students and students[s] != curr:
                if students[s] != '#':
                    projects[students[s]].discard(s)
                students[s] = '#'
            else:
                projects[curr].add(s)
                students[s] = curr

if __name__ == "__main__":
    main()