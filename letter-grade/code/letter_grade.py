grade = [0.0, 0.0, 0.0, 0.0] # midterm, final, weighted avg and rounded
weight = [0.4, 0.6] # midterm and final exam weights
grade[0] = float(input('Enter the midterm exam grade: '))
grade[1] = float(input('Enter the final exam grade: '))
grade[2] = weight[0]*grade[0] + weight[1]*grade[1]
grade[3] = round(grade[2])
print("The (weighted) final grade is %.2f." % grade[2])
print("After rounding, the (weighted) final grade is %i." % int(grade[3]))
letterGrade = ["AA", "BA", "BB", "CB", "CC", "DC", "DD","FD", "FF"]
gradeTransition = [81, 76, 70, 60, 50, 45, 40, 30]
if grade[3] >= gradeTransition[0]: # AA
    print("You got %s in this course." % letterGrade[0])
elif grade[3] >= gradeTransition[1]: # BA
    print("You got %s in this course." % letterGrade[1])
elif grade[3] >= gradeTransition[2]: ## BB
    print("You got %s in this course." % letterGrade[2])
elif grade[3] >= gradeTransition[3]: # CB
    print("You got %s in this course." % letterGrade[3])
elif grade[3] >= gradeTransition[4]: # CC
    print("You got %s in this course." % letterGrade[4])
elif grade[3] >= gradeTransition[5]: #DC
    print("You got %s in this course." % letterGrade[5])
elif grade[3] >= gradeTransition[6]: # DD
    print("You got %s in this course." % letterGrade[6])
elif grade[3] >= gradeTransition[7]: # FD
    print("You got %s in this course" % letterGrade[7])
else: # FF
    print("You got %s in this course." % letterGrade[8])
