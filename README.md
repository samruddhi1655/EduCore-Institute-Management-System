# EduCore — Institute Management System

A modular, menu-driven Institute Management System built using Python. EduCore helps manage essential institute operations, including student admissions, courses, enquiries, follow-ups, and reports through a command-line interface.

## 1. Project Overview

Managing institute records manually can be time-consuming and may lead to inconsistent or disorganized information. EduCore provides a simple software-based approach to organizing these routine operations.

The application uses a modular Python structure to separate functionality into individual modules. CSV files are used for storing records, allowing data to persist between application runs.

## 2. Problem Statement

Institutes need an organized way to maintain student admission records, course information, enquiries, follow-up details, and operational reports. Managing these records manually can make retrieval, updates, and tracking difficult.

EduCore aims to simplify these activities through a centralized, menu-driven application with structured data storage.

## 3. Objectives

- Develop a modular Python application for institute management.
- Manage student admission records.
- Organize course information.
- Record and manage student enquiries and follow-ups.
- Generate reports from available records.
- Use CSV files for persistent data storage.
- Apply reusable utilities and decorators to improve code organization and maintainability.

## 4. Features

### Student Admission Management
Manage student admission records through the application's admission module.

### Course Management
Manage course information using a dedicated course module.

### Enquiry Management
Maintain student enquiry records and support enquiry-related operations.

### Follow-up Management
Organize follow-up information associated with enquiries.

### Reports
Access reports generated from the application's available records.

### Modular Architecture
Separate application functionality into Python modules to improve readability, maintainability, and reuse.

### CSV-Based Data Storage
Store application records in CSV files for persistence between executions.

### Reusable Utilities and Decorators
Use shared utility functions and decorators to support common application operations.

## 5. Technologies Used

- **Python:** Core programming language.
- **CSV:** Structured storage of application records.
- **File Handling:** Reading and writing persistent data.
- **Python Modules and Packages:** Separation of application functionality.
- **VS Code:** Development environment.
- **Git and GitHub:** Version control and project hosting, if configured.

## 6. Project Structure

The project is organized approximately as follows. Update the tree if your actual folder names differ.

```text
EduCore/
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
│   ├── students.csv
│   ├── courses.csv
│   └── enquiries.csv
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

The `.venv/` directory, if present, contains the local Python virtual environment and is not part of the application source code.

## 7. Installation and Execution

### Prerequisites

- Python installed on your system.
- A code editor or terminal.
- The EduCore project files.

### Step 1: Open the project

Open the EduCore project folder in VS Code.

### Step 2: Create a virtual environment (optional if one already exists)

```bash
python -m venv .venv
```

### Step 3: Activate the virtual environment

**Windows Command Prompt:**

```bash
.venv\Scripts\activate.bat
```

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### Step 4: Install dependencies

If `requirements.txt` contains the project's required third-party packages, install them using:

```bash
python -m pip install -r requirements.txt
```

If the application uses only Python's standard library, no third-party packages need to be installed.

### Step 5: Run the application

From the project root directory, execute:

```bash
python main.py
```

On Windows, you can alternatively use:

```bash
py main.py
```

Follow the on-screen menu to access the available institute management operations.

## 8. Data Storage

EduCore uses CSV files to store application records. This approach keeps the initial implementation lightweight and makes records easy to inspect using spreadsheet software or a text editor.

The application expects its data files to be available at the paths specified in the source code. Preserve the expected directory structure when running the project.

## 9. Testing and Verification

The application has been run locally, and the main menu has been verified to start successfully.

Before final submission, test the following operations individually:

- Student admission operations.
- Course management operations.
- Enquiry creation and retrieval.
- Follow-up operations.
- Report generation.
- Data persistence after restarting the application.
- Handling of invalid menu choices and unexpected inputs.

Record the outcomes of these checks based on actual execution.

## 10. Future Enhancements

Possible future improvements include:

- A graphical user interface or web-based interface.
- Search, filtering, and improved record management.
- Stronger input validation and error handling.
- Role-based access control.
- Database integration using SQLite or PostgreSQL.
- Automated unit tests and broader test coverage.

These are potential enhancements and are not claimed as currently implemented features.

## 11. Conclusion

EduCore demonstrates the use of Python programming, modular design, file handling, CSV-based persistence, reusable utilities, and menu-driven interaction to support routine institute management operations.

The project provides a foundation for further development into a more comprehensive institute management application.

---

**Project:** EduCore — Institute Management System  
**Language:** Python  
**Interface:** Command-line interface  
**Storage:** CSV files  
**Developer:** Samruddhi