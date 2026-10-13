import csv
import os

from .utils import get_current_date, get_valid_phone
from .decorators import log_activity


DATA_FILE = "data/enquiries.csv"


@log_activity
def add_enquiry():
    print("\n========== STUDENT ENQUIRY ==========")

    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    phone = get_valid_phone()

    course = input("Enter interested course: ").strip()

    if not course:
        print("Course cannot be empty.")
        return

    source = input("How did you hear about us? ").strip()

    enquiry_id = generate_enquiry_id()

    enquiry = [
        enquiry_id,
        name,
        phone,
        course,
        source,
        get_current_date(),
        "New"
    ]

    file_exists = os.path.exists(DATA_FILE)

    with open(DATA_FILE, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists or os.path.getsize(DATA_FILE) == 0:
            writer.writerow([
                "Enquiry ID",
                "Name",
                "Phone",
                "Interested Course",
                "Source",
                "Enquiry Date",
                "Status"
            ])

        writer.writerow(enquiry)

    print("\nEnquiry added successfully!")
    print("Enquiry ID:", enquiry_id)


def generate_enquiry_id():
    """Generate a simple enquiry ID."""

    if not os.path.exists(DATA_FILE):
        return "ENQ001"

    with open(DATA_FILE, "r", newline="") as file:
        reader = list(csv.reader(file))

    if len(reader) <= 1:
        return "ENQ001"

    number = len(reader)
    return f"ENQ{number:03d}"


def view_enquiries():
    print("\n========== ENQUIRY RECORDS ==========")

    if not os.path.exists(DATA_FILE):
        print("No enquiry records found.")
        return

    with open(DATA_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)
        enquiries = list(reader)

    if not enquiries:
        print("No enquiry records found.")
        return

    for enquiry in enquiries:
        print("-" * 55)
        print("Enquiry ID      :", enquiry["Enquiry ID"])
        print("Name            :", enquiry["Name"])
        print("Phone           :", enquiry["Phone"])
        print("Interested Course:", enquiry["Interested Course"])
        print("Source          :", enquiry["Source"])
        print("Enquiry Date    :", enquiry["Enquiry Date"])
        print("Status          :", enquiry["Status"])