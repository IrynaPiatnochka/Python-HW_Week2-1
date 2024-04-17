# Finding the average grade from the list

def average(grades):
    average_grade = []
    for gr in grades:
        average_grade = sum(grades)/len(grades)

    return average_grade 
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
average_grade = average(grades)
print(average_grade)


# Finding the lowest grade from the list
def highest_grade(gardes):
    highest = []
    for gr in grades:
        highest = max(grades)

    return highest

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
highest = max(grades)
print(highest)


# Finding the lowest grade from the list
def lowest_grade(gardes):
    lowest = []
    for low in grades:
        lowest = min(grades)

    return lowest

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
lowest = min(grades)
print(lowest)



# Creating a feature that categorizes grades into letter grades (A, B, C, etc.)
num_grade = input("What is the grade? ")

grade = int(num_grade)

if (80 <= grade <= 100):
    print("Your grade is A")
elif (65 <= grade <= 79):
    print("Your grade is B")
elif (50 <= grade <= 64):
    print("Your grade is C")
else:
    print("Your grade is F")






