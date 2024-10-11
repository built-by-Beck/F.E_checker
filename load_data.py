import csv
import sqlite3

# Function to load the CSV data into the SQLite database
def load_csv_to_db():
    conn = sqlite3.connect('extinguisher.db')
    cursor = conn.cursor()

    # Read the CSV file
    with open('all_fire_extinguishers.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        # Loop through each row in the CSV and insert into the database
        for row in reader:
            location_number = row['Location #'] if row['Location #'] else 'N/A'
            extinguisher_type = row['Type']
            size = row['Size']
            location = row['Location']
            barcode = row['Barcode'] if row['Barcode'] else None  # Handle missing barcodes
            serial_number = row['Serial Number']
            pass_fail = row['Pass Y/N'] if row['Pass Y/N'] else 'Unchecked'
            date_inspected = row['Date Inspected'] if row['Date Inspected'] else '2024-01-01'  # Default date if missing
            initials = row['Initials'] if row['Initials'] else 'N/A'

            # Insert data into the database
            cursor.execute('''
                INSERT INTO extinguishers (location_number, type, size, location, barcode, serial_number, pass_fail, date_inspected, initials)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (location_number, extinguisher_type, size, location, barcode, serial_number, pass_fail, date_inspected, initials))
    
    conn.commit()
    conn.close()
    print("CSV data loaded into the database successfully!")

if __name__ == '__main__':
    load_csv_to_db()
