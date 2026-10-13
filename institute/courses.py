
import csv
import os

from .decorators import log_activity

DATA_FILE = "data/courses.csv"


@log_activity
def add_course():
    print("\n========== ADD COURSE ==========")

    course_name = input("Enter course name: ").strip()
    duration = input("Enter course duration: ").strip()
    fee = input("Enter course fee: ").strip()

    if not course_name or not duration or not fee:
        print("All fields are required.")
        return

    if not fee.isdigit():
        print("Fee must be a number.")
        return

    course_id = generate_course_id()

    file_exists = os.path.exists(DATA_FILE)

    with open(DATA_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists or os.path.getsize(DATA_FILE) == 0:
            writer.writerow([
                "Course ID", "Course Name", "Duration", "Fee"
            ])

        writer.writerow([course_id, course_name, duration, fee])

    print("\nCourse added successfully!")
    print("Course ID:", course_id)


def generate_course_id():
    if not os.path.exists(DATA_FILE):
        return "CRS001"

    with open(DATA_FILE, "r", newline="", encoding="utf-8") as file:
        records = list(csv.reader(file))

    return f"CRS{len(records):03d}"


def view_courses():
    print("\n========== AVAILABLE COURSES ==========")

    if not os.path.exists(DATA_FILE):
        print("No courses found.")
        return

    with open(DATA_FILE, "r", newline="", encoding="utf-8") as file:
        courses = list(csv.DictReader(file))

    if not courses:
        print("No courses found.")
        return

    for course in courses:
        print("-" * 40)
        print("Course ID :", course["Course ID"])
        print("Course    :", course["Course Name"])
        print("Duration  :", course["Duration"])
        print("Fee       :", course["Fee"])
