# F.E_checker

**F.E_checker** (Fire Extinguisher Checker) is a Python-based web application designed to streamline fire extinguisher inspections and data management. As a Life Safety Technician at Brookwood Hospital, I developed this tool to reduce manual work, automate inspection tracking, and ensure fire extinguishers are up to safety standards.

## Features

- **Barcode Tracking:** Track fire extinguishers using their barcode numbers for quick identification.
- **Inspection Status:** Mark fire extinguishers as "Pass" or "Fail" for each inspection cycle.
- **Reset Functionality:** Reset the inspection statuses of all extinguishers in bulk at the start of a new inspection cycle.
- **Duplicate Entry Detection:** Identify and flag duplicate entries in the database, preventing redundant or conflicting data.
- **Mobile-Friendly UI:** Accessible via smartphones, allowing inspectors to perform tasks on the go.
- **CSV Import/Export:** Import large datasets of fire extinguishers from CSV files and export current inspection data for reports.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/F.E_checker.git
   cd F.E_checker

2. Create and activate a virtual enviroment:
   python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. Install the dependencies:
   pip install -r requirements.txt

4. Initialize the database:
   python app.py

   The app will create the SQLite database and table on the first run if they don't exist.
   5. Run the application:
      flask run
Open http://127.0.0.1:5000/ in your browser to use the app.

--------------------------------------------------------
Usage
Adding Fire Extinguishers
Enter extinguisher details such as location, type, size, barcode, and serial number.
Click "Add Extinguisher" to store the entry in the database.
Inspecting Fire Extinguishers
Scan the extinguisher's barcode or search for it manually.
Mark the extinguisher as "Pass" or "Fail" after inspection. The app records the inspection date and initials.
Resetting Inspections
At the start of a new month, go to the "Reset Inspections" section to reset all statuses to "Unchecked."
Duplicate Entry Detection
The app detects duplicate barcodes to avoid conflicting records. You can also run a duplicate check by uploading a dataset.

php
F.E_checker/
│
├── app.py                   # Main Flask app
├── load_data.py              # Script to load CSV data into the database
├── duplicate_checker.py      # Script to detect duplicate entries
├── extinguisher.db           # SQLite database storing extinguisher details
├── templates/                # HTML templates
│   ├── index.html            # Main page template
│   ├── extinguisher_details.html  # Extinguisher details page
├── static/
│   ├── styles.css            # Custom styles for the web pages
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation (this file)
└── LICENSE                   # License for the project

sql
CREATE TABLE extinguishers (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  location_number TEXT NOT NULL,
  type TEXT NOT NULL,
  size TEXT NOT NULL,
  location TEXT NOT NULL,
  barcode TEXT UNIQUE NOT NULL,
  serial_number TEXT NOT NULL,
  pass_fail TEXT DEFAULT 'Unchecked',
  date_inspected TEXT NOT NULL,
  initials TEXT NOT NULL
);

Contributing
Fork the repository.
Create a new feature branch: git checkout -b feature-branch-name
Commit your changes: git commit -m 'Add new feature'
Push to the branch: git push origin feature-branch-name
Open a Pull Request.
License
This project is licensed under the MIT License. See the LICENSE file for more details.

vbnet

Make sure to adjust the repository URL (`https://github.com/yourusername/F.E_checker.git`) when you upload it to GitHub.

