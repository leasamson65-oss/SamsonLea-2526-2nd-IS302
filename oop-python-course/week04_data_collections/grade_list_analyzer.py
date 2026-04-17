grades_lea = []

for i in range(5):
    grade = float(input(f"Enter grade {i+1}: "))
    grades_lea.append(grade)

average_lea = sum(grades_lea) / len(grades_lea)
highest_lea = max(grades_lea)
lowest_lea = min(grades_lea)

print("\nAverage Grade:", average_lea)
print("Highest Grade:", highest_lea)
print("Lowest Grade:", lowest_lea)