with open ('/home/alexandr/Downloads/dataset_3363_4.txt') as inf:
    students = []
    for line in inf:
        students.append(line.strip().split(';'))

quantity_students = len(students)


math_score = 0 
phisics_score = 0
rus_score = 0

for i in students:
    print (str((int(i[1]) + int(i[2]) + int(i[3]))/3))
    math_score += int(i[1]) 
    phisics_score += int(i[2])
    rus_score += int(i[3])


print(str(math_score/quantity_students), str(phisics_score/quantity_students), str(rus_score/quantity_students))



