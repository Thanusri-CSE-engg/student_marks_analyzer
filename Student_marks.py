
name = input("Enter student name: ")

tamil = int(input("Enter Tamil mark: "))
english = int(input("Enter English mark: "))
maths = int(input("Enter Maths mark: "))
physics = int(input("Enter Physics mark: "))
chemistry = int(input("Enter Chemistry mark: "))

marks = {
    "Tamil": tamil,
    "English": english,
    "Maths": maths,
    "Physics": physics,
    "Chemistry": chemistry
}

total = sum(marks.values())
average = total / 5

print("\n--- Student Result ---")
print("Name:", name)

for subject, mark in marks.items():
    print(subject, ":", mark)

print("Total:", total)
print("Average:", average)
print("Highest:", max(marks, key=marks.get))
print("Lowest:", min(marks, key=marks.get))

if min(marks.values()) >= 35:
    print("Result: PASS")

    if average >= 90:
        print("Grade: A")
    elif average >= 75:
        print("Grade: B")
    elif average >= 50:
        print("Grade: C")
    else:
        print("Grade: D")
else:
    print("Result: FAIL")
    print("Grade: No Grade")
