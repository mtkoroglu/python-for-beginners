grade = zeros(1,4); % midterm, final, weighted avg and rounded
weight = [0.4, 0.6]; % midterm and final exam weights
grade(1) = input('Enter the midterm exam grade: ');
grade(2) = input('Enter the final exam grade: ');
grade(3) = weight(1)*grade(1) + weight(2)*grade(2);
grade(4) = round(grade(3));
fprintf('The (weighted) final grade is %.2f.\n', grade(3));
fprintf('After rounding, the (weighted) final grade is %i.\n', grade(4));
letterGrade = {'AA', 'BA', 'BB', 'CB', 'CC', 'DC', 'DD', 'FD', 'FF'};
gradeTransition = [81, 76, 70, 60, 50, 45, 40, 30];
if (grade(3) >= gradeTransition(1)) % AA
    fprintf('You got %s in this course.\n', letterGrade{1,1});
else if (grade(3) >= gradeTransition(2)) % BA
        fprintf('You got %s in this course.\n', letterGrade{1,2});
    else if (grade(3) >= gradeTransition(3)) % BB
            fprintf('You got %s in this course.\n', letterGrade{1,3});
        else if (grade(3) >= gradeTransition(4)) % CB
                fprintf('You got %s in this course.\n', letterGrade{1,4});
            else if (grade(3) >= gradeTransition(5)) % CC
                    fprintf('You got %s in this course.\n', letterGrade{1,5});
                else if (grade(3) >= gradeTransition(6)) % DC
                        fprintf('You got %s in this course.\n', letterGrade{1,6});
                    else if (grade(3) >= gradeTransition(7)) % DD
                            fprintf('You got %s in this course.\n', letterGrade{1,7});
                        else if (grade(3) >= gradeTransition(8)) % FD
                                fprintf('You got %s in this course.\n', letterGrade{1,8});
                            else
                                fprintf('You got %s in this course.\n', letterGrade{1,9});
                            end
                        end
                    end
                end
            end
        end
    end
end