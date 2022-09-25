import csv
from collections import defaultdict

from pyhtml import *


class Student:
    def __init__(self, ID):
        self.ID = ID
        self.marks = defaultdict(int)


courses = defaultdict(list)
students = defaultdict(dict)
student_db = {}
with open('data.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    line_count = 0
    for row in reader:
        if line_count == 0:
            # print(row)
            line_count += 1
            continue
        # student_db[row[0]] =
        if row[0] not in student_db:
            student_db[row[0]] = Student(ID=row[0])
        student_db[row[0]].marks[row[1]] = row[2]
        students[row[0]][row[1]] = row[2]
        courses[row[1]].append(row[2])
print(courses)
print(student_db)
print(students)
tab = table(
    tr(
        th("Student id"),
        th("Course id"),
        th('Marks')
    ),

)
if sys.argv[1] == '-c':
    pass
if sys.argv[1] == '-s':
    pass

print(tab)
