import heapq

courses, course_students = [], {}
for _ in range(int(input())):
    fname, lname, course = input().split()
    if course not in course_students:
        heapq.heappush(courses, course)
        course_students[course] = {(fname, lname)}
    else:
        course_students[course].add((fname, lname))

while courses:
    course = heapq.heappop(courses)
    count = len(course_students[course])
    print(f"{course} {count}")