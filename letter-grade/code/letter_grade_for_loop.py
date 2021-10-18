letterGrade = ["AA", "BA", "BB", "CB", "CC", "DC", "DD","FD", "FF"]
gradeLowerBound = [81, 76, 70, 60, 50, 45, 40, 30, 0]
weight = [0.4, 0.6] # midterm and final exam weights
print('Letter grades are ', end='')
print(letterGrade)
print('Grade lower bounds are ', end='')
print(gradeLowerBound)
midterm = float(input('Enter the midterm exam grade: '))
final = float(input('Enter the final exam grade: '))
weightedAvg = weight[0]*midterm + weight[1]*final
grade = int(round(weightedAvg))
print("The (weighted) final grade is %.2f." % weightedAvg)
print("After rounding, the (weighted) final grade is %i." % grade)
for i in range(len(letterGrade)):
    if grade >= gradeLowerBound[i]:
        print('You got %s in this course.' % letterGrade[i])
        break