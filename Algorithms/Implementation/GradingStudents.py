#University has the following grading policy:
#Every student receives a grade in the inclusive range from 0 to 100.
#Any grade less than 40 is a failing grade.
#Sam is a professor at the university and likes to round each student's grade according to these rules:
#If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
#If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.

import sys

def solve(grades):
    res = []
    
    for el in grades:
        if el < 38:
            res.append(el)
        elif el%5 >= 3:
            res.append(el + 5-el%5)
        else:
            res.append(el)
    return res

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print("\n".join(map(str, result)))
