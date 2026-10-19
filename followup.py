import csv
import os

from .utils import get_current_date
from .decorators import log_activity


DATA_FILE = "data/followups.csv"


@log_activity
def add_followup():
    print("\n========== FOLLOW-UP MANAGEMENT ==========")

    enquiry_id = input("Enter enquiry ID: ").strip()

    if not enquiry_id:
        print("Enquiry ID cannot be empty.")
        return

    followup_date = input(
        "Enter follow-up date (YYYY-MM-DD): "
    ).strip()

    remarks = input("Enter follow-up remarks: ").strip()

    print("\nSelect status:")
    print("1. Pending")
    print("2. Completed")
    print("3. Interested")
    print("4. Not Interested")

    choice = input("Enter choice: ").strip()

    status_map = {
        "1": "Pending",
        "2": "Completed",
        "3": "Interested",
        "4": "Not Interested"
    }

    status = status_map.get(choice)

    if status is None:
        print("Invalid status.")
        return

    followup_id = generate_followup_id()

    followup = [
        followup_id,
        enquiry_id,
        get_current_date(),
        followup_date,
        remarks,
        status
    ]

    file_exists = os.path.exists(DATA_FILE)

    with open(DATA_FILE, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists or os.path.getsize(DATA_FILE) == 0:
            writer.writerow([
                "Follow-up ID",
                "Enquiry ID",
                "Created Date",
                "Follow-up Date",
                "Remarks",
                "Status"
            ])

        writer.writerow(followup)

    print("\nFollow-up added successfully!")
    print("Follow-up ID:", followup_id)


def generate_followup_id():
    """Generate a simple follow-up ID."""

    if not os.path.exists(DATA_FILE):
        return "FUP001"

    with open(DATA_FILE, "r", newline="") as file:
        records = list(csv.reader(file))

    if len(records) <= 1:
        return "FUP001"

    number = len(records)

    return f"FUP{number:03d}"


def view_followups():
    print("\n========== FOLLOW-UP RECORDS ==========")

    if not os.path.exists(DATA_FILE):
        print("No follow-up records found.")
        return

    with open(DATA_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)
        followups = list(reader)

    if not followups:
        print("No follow-up records found.")
        return

    for followup in followups:
        print("-" * 55)
        print("Follow-up ID   :", followup["Follow-up ID"])
        print("Enquiry ID     :", followup["Enquiry ID"])
        print("Created Date   :", followup["Created Date"])
        print("Follow-up Date :", followup["Follow-up Date"])
        print("Remarks        :", followup["Remarks"])
        print("Status         :", followup["Status"])