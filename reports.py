import csv
import os


STUDENT_FILE = "data/students.csv"
ENQUIRY_FILE = "data/enquiries.csv"
FOLLOWUP_FILE = "data/followups.csv"
COURSE_FILE = "data/courses.csv"


def count_records(file_path):
    """Count records in a CSV file."""

    if not os.path.exists(file_path):
        return 0

    with open(file_path, "r", newline="") as file:
        reader = list(csv.reader(file))

    if len(reader) <= 1:
        return 0

    return len(reader) - 1


def count_status(file_path, column_name, status):
    """Count records with a particular status."""

    if not os.path.exists(file_path):
        return 0

    with open(file_path, "r", newline="") as file:
        reader = csv.DictReader(file)

        count = 0

        for row in reader:
            if row.get(column_name) == status:
                count += 1

        return count


def show_report():
    """Display institute summary report."""

    print()
    print("=" * 60)
    print("              INSTITUTE SUMMARY REPORT")
    print("=" * 60)

    total_students = count_records(STUDENT_FILE)
    total_enquiries = count_records(ENQUIRY_FILE)
    total_followups = count_records(FOLLOWUP_FILE)
    total_courses = count_records(COURSE_FILE)

    pending_followups = count_status(
        FOLLOWUP_FILE,
        "Status",
        "Pending"
    )

    interested_students = count_status(
        FOLLOWUP_FILE,
        "Status",
        "Interested"
    )

    completed_followups = count_status(
        FOLLOWUP_FILE,
        "Status",
        "Completed"
    )

    print(f"Total Students       : {total_students}")
    print(f"Total Enquiries      : {total_enquiries}")
    print(f"Total Follow-ups     : {total_followups}")
    print(f"Total Courses        : {total_courses}")

    print("-" * 60)

    print(f"Pending Follow-ups   : {pending_followups}")
    print(f"Interested Leads     : {interested_students}")
    print(f"Completed Follow-ups : {completed_followups}")

    print("=" * 60)