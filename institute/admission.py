import csv
import os

from .utils import get_current_date, get_valid_phone, get_valid_email
from .decorators import log_activity


DATA_FILE = "data/students.csv"


@log_activity
def add_student():
    print("\n========== STUDENT ADMISSION ==========")

    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    age = input("Enter age: ").strip()

    if not age.isdigit():
        print("Please enter a valid age.")
        return

    phone = get_valid_phone()
    email = get_valid_email()
    course = input("Enter course: ").strip()

    if not course:
        print("Course cannot be empty.")
        return

    student_id = generate_student_id()

    student = [
        student_id,
        name,
        age,
        phone,
        email,
        course,
        get_current_date()
    ]

    file_exists = os.path.exists(DATA_FILE)

    with open(DATA_FILE, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists or os.path.getsize(DATA_FILE) == 0:
            writer.writerow([
                "Student ID",
                "Name",
                "Age",
                "Phone",
                "Email",
                "Course",
                "Admission Date"
            ])

        writer.writerow(student)

    print("\nStudent admitted successfully!")
    print("Student ID:", student_id)


def generate_student_id():
    """Generate a simple student ID."""

    if not os.path.exists(DATA_FILE):
        return "STU001"

    with open(DATA_FILE, "r", newline="") as file:
        reader = list(csv.reader(file))

    if len(reader) <= 1:
        return "STU001"

    number = len(reader)
    return f"STU{number:03d}"


def view_students():
    print("\n========== STUDENT RECORDS ==========")

    if not os.path.exists(DATA_FILE):
        print("No student records found.")
        return

    with open(DATA_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)
        students = list(reader)

    if not students:
        print("No student records found.")
        return

    for student in students:
        print("-" * 50)
        print("Student ID    :", student["Student ID"])
        print("Name          :", student["Name"])
        print("Age           :", student["Age"])
        print("Phone         :", student["Phone"])
        print("Email         :", student["Email"])
        print("Course        :", student["Course"])
        print("Admission Date:", student["Admission Date"])