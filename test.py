from flask import Flask, request, jsonify, session, redirect, url_for, render_template, flash
import mariadb
from phonenumbers import parse, is_valid_number
app = Flask(__name__)
app.secret_key = "b'8\xf9\x1e\xd7\xaf\xf6\xd0\xd8\x08\x9c/\xb2\xca\x11-+\xc6\xcf(\xdb\xb9\xf3P|'"

# Database connection
def get_db_connection():
    conn = mariadb.connect(
        user='root',
        password='31283128',
        host='127.0.0.1',
        port=3306,
        database='internship'
    )
    return conn


@app.route('/contacts/remove/<int:contact_id>', methods=['POST'])
def remove_contact(contact_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM contacts WHERE id=?", (contact_id,))
    conn.commit()
    conn.close()

    return redirect(url_for('contact_list'))

def is_email_unique(email):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id FROM contacts WHERE email=?", (email,))
    return cur.fetchone() is None

def validate_phone_number(phone_number):
    try:
        number = parse(phone_number)
        return is_valid_number(number)
    except Exception:
        return False

def is_phone_number_unique(phone_number):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id FROM contacts WHERE phone_number=?", (phone_number,))
    return cur.fetchone() is None

# Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT id FROM users WHERE email=? AND password=?", (email, password))
        user = cur.fetchone()
        if user:
            session['user_id'] = user[0]
            return redirect(url_for('contact_list'))
        else:
            flash('Invalid email or password')
            return redirect(url_for('login'))
    return render_template('login.html')

# My Contact List page
@app.route('/contacts')
def contact_list():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user_id = session['user_id']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, full_name FROM contacts WHERE user_id=?", (user_id,))
    contacts = cur.fetchall()
    return render_template('contacts.html', contacts=contacts)

# Add Contact page
@app.route('/contacts/add', methods=['GET', 'POST'])
def add_contact():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        full_name = request.form.get('full_name')
        email = request.form.get('email')
        phone_number = request.form.get('phone_number')
        user_id = session['user_id']
        if not is_email_unique(email):
            return "Email is already in use", 400
        if not validate_phone_number(phone_number):
            return "Invalid phone number", 400
        if not is_phone_number_unique(phone_number):
            return "Phone number is already in use", 400
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO contacts (user_id, full_name, email, phone_number) VALUES (?, ?, ?, ?)",
                    (user_id, full_name, email, phone_number))
        conn.commit()
        return redirect(url_for('contact_list'))
    return render_template('add_contact.html')

# Contact Details page
@app.route('/contacts/<int:contact_id>', methods=['GET', 'POST'])
def contact_details(contact_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    conn = get_db_connection()
    cur = conn.cursor()
    if request.method == 'POST':
        email = request.form.get('email')
        phone_number = request.form.get('phone_number')
        cur.execute("UPDATE contacts SET email=?, phone_number=? WHERE id=?",
                    (email, phone_number, contact_id))
        conn.commit()
        return redirect(url_for('contact_list'))
    cur.execute("SELECT full_name, email, phone_number FROM contacts WHERE id=?", (contact_id,))
    contact = cur.fetchone()
    return render_template('contact_details.html', contact=contact)

if __name__ == '__main__':
    app.run(debug=True ,port=5001)