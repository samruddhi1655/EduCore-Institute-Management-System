# Institute Management System

A Python-based, menu-driven application designed to simplify basic institute administration. The system uses CSV files for data storage and provides separate modules for managing students, courses, enquiries, follow-ups, and reports.

## Features

- **Student Management:** Add and view student records.
- **Course Management:** Add courses and view available course details.
- **Enquiry Management:** Record and view student enquiries.
- **Follow-up Management:** Record follow-ups and track their status.
- **Reports:** View summary counts for students, enquiries, courses, and follow-ups.
- **CSV Data Storage:** Store records in local CSV files.
- **Modular Architecture:** Organize functionality into separate Python modules.
- **Activity Logging:** Record selected operations using a logging decorator.

## Technology Stack

- Python 3
- CSV for data storage
- Standard Python libraries
- Visual Studio Code

## Project Structure

```text
InstituteManagementSystem/
├── institute/
│   ├── __init__.py
│   ├── admission.py
│   ├── courses.py
│   ├── decorators.py
│   ├── enquiry.py
│   ├── followup.py
│   ├── reports.py
│   └── utils.py
├── Data/
├── .venv/
├── main.py
├── requirements.txt
└── README.md
```

## Prerequisites

- Python 3 installed
- Visual Studio Code or another Python-compatible editor

## Setup and Installation

1. Open the project folder in Visual Studio Code.
2. Open the integrated terminal.
3. Activate the virtual environment if it is not already active:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

4. Install dependencies if required:

   ```powershell
   python -m pip install -r requirements.txt
   ```

## Run the Application

From the project root, execute:

```powershell
python main.py
```

Use the interactive menu to select the required operation. Enter `0` to exit.

## Data Storage

Application records are stored in CSV files in the project's data directory. These files can be opened with spreadsheet applications for inspection.

## Limitations

This is a basic educational project intended to demonstrate modular Python programming and file-based record management. It does not currently provide a web interface, database server, user authentication, or multi-user access controls.

## Future Enhancements

- Add a graphical or web-based interface.
- Introduce database integration using SQLite or MySQL.
- Add authentication and role-based access.
- Improve input validation and error handling.
- Add search, update, and delete operations.
- Generate downloadable reports.

## Author

Developed as an Institute Management System project.
