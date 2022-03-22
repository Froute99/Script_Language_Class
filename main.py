
import random


def get_average_grade(*scores):
    total = 0
    for score in scores:
        total += score
    return total / len(scores)


students = []
for v in range(1, 21):
    student = {'Student': v, 'Kor': random.randint(0, 100), 'Eng': random.randint(0, 100), 'Math': random.randint(0, 100)}
    student['Avg'] = (student.get('Kor') + student.get('Eng') + student.get('Math')) / 3
    students.append(student)

totalKorGrade = 0
totalEngGrade = 0
totalMathGrade = 0


# print header format of grade table
print('======================================================')
print('Student    ', 'Kor    ', 'Eng    ', 'Math\t', 'AVG\t')
print('------------------------------------------------------')

for student in students:
    studentNumber = student.get('Student')
    korGrade = student.get('Kor')
    engGrade = student.get('Eng')
    mathGrade = student.get('Math')

    totalKorGrade += korGrade
    totalEngGrade += engGrade
    totalMathGrade += mathGrade

    average = GetAverageGrade(korGrade, engGrade, mathGrade)
    print(f"{studentNumber}\t\t\t{korGrade}\t\t{engGrade}\t\t{mathGrade}\t\t{average: .2f}")


print('------------------------------------------------------')
print(f'AVG         {totalKorGrade/20:.2f}, {totalEngGrade/20: .2f}, {totalMathGrade/20: .2f}')
print('======================================================')