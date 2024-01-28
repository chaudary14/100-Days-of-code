student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}




# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.

student_grades = {}
#TODO-2: Write your code below to add the grades to student_grades.👇
for x in student_scores:
    score = student_scores[x]
    if 90 < score:
        student_grades[x] = "OUTSTANDING"
        # print(x, "grade is EXcelleent")
    elif 80 < score:
        student_grades[x] = "EXceeding acceptation"

        # print(x, "grade is exceeds expectation")
    elif 70 < score:
        student_grades[x] = "acceptable"
        # print(x, "grade is acceptable.")
    else:
        student_grades[x] = "Fail"
        # print(x, "grade is Fail")


# 🚨 Don't change the code below 👇

print(student_grades)
