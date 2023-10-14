from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'navya'  # Replace with your own secret key

# Mock user data (replace with a database)
users = []

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/register/<user_type>', methods=['GET', 'POST'])
def register(user_type):
    if user_type == 'recruiter':
        if request.method == 'POST':
            # Registration logic for recruiters
            username = request.form['username']
            password = request.form['password']

            # Check if the username is already taken (in a real application, use a database)
            if any(user['username'] == username for user in users):
                flash('Username already exists. Please choose another.', 'danger')
            else:
                # Store the user data (in a real application, use a database)
                hashed_password = generate_password_hash(password)
                users.append({'username': username, 'password': hashed_password})
                flash('Recruiter registration successful.', 'success')
                return redirect(url_for('index'))

        return render_template('recruiter_register.html')

    elif user_type == 'applicant':
        if request.method == 'POST':
            # Registration logic for job applicants
            username = request.form['username']
            password = request.form['password']

            # Check if the username is already taken (in a real application, use a database)
            if any(user['username'] == username for user in users):
                flash('Username already exists. Please choose another.', 'danger')
            else:
                # Store the user data (in a real application, use a database)
                hashed_password = generate_password_hash(password)
                users.append({'username': username, 'password': hashed_password})
                flash('Job applicant registration successful.', 'success')
                return redirect(url_for('index'))

        return render_template('applicant_register.html')

    else:
        flash('Invalid user type.', 'danger')
        return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = next((user for user in users if user['username'] == username), None)

        if user and check_password_hash(user['password'], password):
            session['user'] = user['username']
            flash('Login successful.', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login failed. Please check your username and password.', 'danger')

    return render_template('login.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/register/applicant', methods=['GET', 'POST'])
def register_applicant():
    if request.method == 'POST':
        # Registration logic for job applicants
        username = request.form['username']
        password = request.form['password']

        # Check if the username is already taken (in a real application, use a database)
        if any(user['username'] == username for user in users):
            flash('Username already exists. Please choose another.', 'danger')
        else:
            # Store the user data (in a real application, use a database)
            hashed_password = generate_password_hash(password)
            users.append({'username': username, 'password': hashed_password})
            flash('Job applicant registration successful.', 'success')
            return redirect(url_for('index'))
    else:
        flash('Invalid user type.', 'danger')
        return render_template('applicant_register.html')


@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

