import random
names = ['Naruto', 'Asta', 'Sasuke', 'Kakashi', 'Yuno', 'Gojo', 'Nezuko']

student_score = {student:random.randint(0, 100) for student in names}
print(student_score.keys())
for score in student_score.values():
    print(score)
passed_score = {student: score for (student, score) in student_score.items() if score > 60 }
print(passed_score)