def calculate_average(g1, g2, g3):
    return (g1 + g2 + g3) / 3

def get_remark(avg):
    if 90 <= avg <= 100:
        return "Excellent"
    elif 85 <= avg <= 89:
        return "Very Good"
    elif 80 <= avg <= 84:
        return "Good"
    elif 75 <= avg <= 79:
        return "Fair"
    else:
        return "Failed"

# Main program
name_lea = input("Enter student name: ")

grade1_lea = float(input("Enter grade 1: "))
grade2_lea = float(input("Enter grade 2: "))
grade3_lea = float(input("Enter grade 3: "))

average_lea = calculate_average(grade1_lea, grade2_lea, grade3_lea)
remark_lea = get_remark(average_lea)

print("\nStudent:", name_lea)
print("Average:", average_lea)
print("Remark:", remark_lea)