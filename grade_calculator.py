# score = int(input("Enter your score "))
# if score >= 50 and score <= 70:
#     grade = "Pass"
# elif score >= 71 and score <= 90:
#     grade = "Merit"
# elif score > 90:
#     grade = "Distinction"
# else:
#     grade = "Fail"

# print(f"Your grade is {grade}")

# if grade == "Fail":
#     print("loser...")

def grade_calculator(score):
    if score >= 50 and score <= 70:
        grade = "Pass"
    elif score >= 71 and score <= 90:
        grade = "Merit"
    elif score > 90:
        grade = "Distinction"
    else:
        grade = "Fail"
    return grade

test_quantity = int(input("How many tests did you complete?"))
for i in range(test_quantity):
    score = int(input("Enter your score "))
    grade = grade_calculator(score)
    print(f"Test number {i+1} has a grade of {grade}")
