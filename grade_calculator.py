def calculate_grade(marks):
    if 90 <= marks <= 100:
        return "A", "Excellent work! Keep shining!"
    elif 80 <= marks <= 89:
        return "B", "Very Good! Keep it up!"
    elif 70 <= marks <= 79:
        return "C", "Good effort! You can do even better!"
    elif 60 <= marks <= 69:
        return "D", "Keep practicing, improvement is possible!"
    else:
        return "F", "Don’t give up, work harder and you’ll improve!"


def main():
    print("===== STUDENT GRADE CALCULATOR =====")

    student_name = input("Enter student name: ")

    while True:
        try:
            marks = int(input("Enter marks (0-100): "))

            if 0 <= marks <= 100:
                break
            else:
                print("Invalid input! Marks must be between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter numbers only.")

    grade, message = calculate_grade(marks)

    print("\nRESULT FOR", student_name.upper())
    print("Marks:", marks, "/100")
    print("Grade:", grade)
    print("Message:", message)


main()
