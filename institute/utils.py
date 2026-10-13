from datetime import datetime


def get_current_date():
    """Return today's date."""
    return datetime.now().strftime("%Y-%m-%d")


def print_line():
    """Print a separator line."""
    print("-" * 60)


def print_header(title):
    """Print a formatted section heading."""
    print()
    print("=" * 60)
    print(title.center(60))
    print("=" * 60)


def get_valid_phone():
    """Get and validate a 10-digit phone number."""
    while True:
        phone = input("Enter phone number: ").strip()

        if phone.isdigit() and len(phone) == 10:
            return phone

        print("Invalid phone number. Please enter exactly 10 digits.")


def get_valid_email():
    """Get and validate a basic email address."""
    while True:
        email = input("Enter email: ").strip()

        if "@" in email and "." in email:
            return email

        print("Invalid email address. Please try again.")