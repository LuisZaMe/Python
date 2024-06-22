#####################################################################
#  Average Height
#####################################################################
student_heights = [156, 178, 165, 171, 187]

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
    total_height+= height
print(f"Total Height : {total_height}")

number_of_students = 0
for student in student_heights:
    number_of_students+= 1
print(f"Number of Students : {number_of_students}")

avg_height = round(total_height / number_of_students)
print(f"Avg Height : {avg_height}")

#####################################################################
#  High Scores
#####################################################################
student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

high_score = 0
for score in student_scores:
    if score > high_score:
        high_score = score

print(f"The highest score of the class is : {high_score}")

#####################################################################
#  Range Example
# for number in range(1, 10, 2):
#     print(number)
#####################################################################
target = 1000
total_sum = 0
for number in range(2, target + 1, 2):
    total_sum += number
print(total_sum)

# Or
alternative_sum =0
for n in range(1, target + 1):
    if n % 2 == 0:
        alternative_sum += n
print(alternative_sum)
