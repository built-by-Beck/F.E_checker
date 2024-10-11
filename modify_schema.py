import sqlite3

def modify_schema():
    conn = sqlite3.connect('extinguisher.db')
    cursor = conn.cursor()

    # Step 1: Rename the old extinguishers table
    cursor.execute('''
        ALTER TABLE extinguishers RENAME TO extinguishers_old;
    ''')

    # Step 2: Create a new extinguishers table with barcode column allowing NULL
    cursor.execute('''
        CREATE TABLE extinguishers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            location_number TEXT,
            type TEXT,
            size TEXT,
            location TEXT,
            barcode TEXT NULL,  -- Allow NULL values for barcode
            serial_number TEXT,
            pass_fail TEXT,
            date_inspected TEXT,
            initials TEXT
        );
    ''')

    # Step 3: Copy data from the old table to the new table
    cursor.execute('''
        INSERT INTO extinguishers (location_number, type, size, location, barcode, serial_number, pass_fail, date_inspected, initials)
        SELECT location_number, type, size, location, barcode, serial_number, pass_fail, date_inspected, initials
        FROM extinguishers_old;
    ''')

    # Step 4: Drop the old extinguishers table
    cursor.execute('''
        DROP TABLE extinguishers_old;
    ''')

    conn.commit()
    conn.close()
    print("Schema modified successfully. 'barcode' column now allows NULL values.")

if __name__ == '__main__':
    modify_schema()
