value = int(input("input value: "))

if value >= 90:
    grade = 'A'
elif value >= 80:
    grade = 'B+'
elif value >= 70:
    grade = 'B'
elif value >= 60:
    grade = 'C+'
elif value >= 50:
    grade = 'C'
elif value >= 40:
    grade = 'D'
elif value >= 30:
    grade = 'E'
else:
    grade = 'F'

print("Value\t\t: ", value)
print("Your Grade\t: ", grade)