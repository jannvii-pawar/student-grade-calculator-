# Student Grade Calculator

## Project Overview
The Student Grade Calculator is a Python program that takes a student's name and marks as input, validates the marks, calculates the grade, and displays an encouraging message based on performance.

## Features
- Takes student name and marks as input
- Validates marks between 0 and 100
- Uses if-elif-else statements for grading
- Uses while loop for invalid input handling
- Uses function for grade calculation
- Includes basic error handling using try-except
- Displays encouraging messages for each grade

## Grading Logic
- A: 90–100
- B: 80–89
- C: 70–79
- D: 60–69
- F: 0–59

## File Structure
student-grade-calculator/
│── README.md
│── grade_calculator.py
│── test_cases.txt
│── screenshots/

## How to Run
1. Install Python on your system
2. Download or clone the project
3. Open terminal in project folder
4. Run:
   python grade_calculator.py

## Example Output
Enter student name: Priya
Enter marks (0-100): 85

RESULT FOR PRIYA
Marks: 85/100
Grade: B
Message: Very Good! Keep it up! 

## Functions Used
### calculate_grade(marks)
This function takes marks as input and returns:
- Grade
- Encouraging message

## Validation Used
- while loop ensures marks are entered again if invalid
- try-except handles non-numeric input

## Testing
The program was tested with:
- valid marks
- invalid marks above 100
- invalid marks below 0
- non-numeric input
