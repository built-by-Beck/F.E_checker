from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Connect to the SQLite database
def get_db_connection():
    conn = sqlite3.connect('extinguisher.db')
    conn.row_factory = sqlite3.Row
    return conn

# Initialize the database (create the table if it doesn't exist)
def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS extinguishers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            location_number TEXT NOT NULL,
            type TEXT NOT NULL,
            size TEXT NOT NULL,
            location TEXT NOT NULL,
            barcode TEXT UNIQUE,
            serial_number TEXT NOT NULL,
            pass_fail TEXT DEFAULT 'Unchecked',
            date_inspected TEXT NOT NULL,
            initials TEXT NOT NULL
        );
    ''')
    conn.commit()
    conn.close()

# Route to display all fire extinguishers
@app.route('/')
def index():
    conn = get_db_connection()
    extinguishers = conn.execute('SELECT * FROM extinguishers').fetchall()
    conn.close()
    return render_template('index.html', extinguishers=extinguishers)

# Route to add new extinguisher
@app.route('/add_extinguisher', methods=['POST'])
def add_extinguisher():
    data = request.form
    conn = get_db_connection()
    conn.execute('''
        INSERT INTO extinguishers (location_number, type, size, location, barcode, serial_number, pass_fail, date_inspected, initials)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (data['location_number'], data['type'], data['size'], data['location'], data['barcode'], data['serial_number'], 'Unchecked', data['date_inspected'], data['initials']))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

# Route to scan a barcode and display the extinguisher details
@app.route('/scan', methods=['POST'])
def scan_barcode():
    barcode = request.form['barcode']
    conn = get_db_connection()
    extinguisher = conn.execute('SELECT * FROM extinguishers WHERE barcode = ?', (barcode,)).fetchone()
    conn.close()
    if extinguisher:
        return render_template('extinguisher_details.html', extinguisher=extinguisher)
    else:
        return "Extinguisher not found", 404

# Route to mark an extinguisher as passed or failed
@app.route('/mark_pass_fail/<int:id>', methods=['POST'])
def mark_pass_fail(id):
    status = request.form['status']
    conn = get_db_connection()
    conn.execute('UPDATE extinguishers SET pass_fail = ?, date_inspected = ? WHERE id = ?', (status, datetime.now().strftime("%Y-%m-%d"), id))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

# Reset all extinguishers
@app.route('/reset_inspections', methods=['POST'])
def reset_inspections():
    conn = get_db_connection()
    current_date = datetime.now().strftime('%Y-%m-%d')
    conn.execute('''
        UPDATE extinguishers
        SET pass_fail = 'Unchecked', date_inspected = ?
    ''', (current_date,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()  # Ensure the database and table are initialized
    app.run(host='0.0.0.0', port=5000)
