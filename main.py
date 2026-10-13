
from institute.admission import add_student, view_students
from institute.courses import add_course, view_courses
from institute.enquiry import add_enquiry, view_enquiries
from institute.followup import add_followup, view_followups
from institute.reports import show_report


def main():
    while True:
        print("\n" + "=" * 50)
        print("          INSTITUTE MANAGEMENT SYSTEM")
        print("=" * 50)

        print("1.  Add Student")
        print("2.  View Students")
        print("3.  Add Course")
        print("4.  View Courses")
        print("5.  Add Enquiry")
        print("6.  View Enquiries")
        print("7.  Add Follow-up")
        print("8.  View Follow-ups")
        print("9.  View Reports")
        print("0.  Exit")

        print("=" * 50)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            add_course()

        elif choice == "4":
            view_courses()

        elif choice == "5":
            add_enquiry()

        elif choice == "6":
            view_enquiries()

        elif choice == "7":
            add_followup()

        elif choice == "8":
            view_followups()

        elif choice == "9":
            show_report()

        elif choice == "0":
            print("\nThank you for using the Institute Management System!")
            break

        else:
            print("\nInvalid choice. Please enter a number from 0 to 9.")


if __name__ == "__main__":
    main()
