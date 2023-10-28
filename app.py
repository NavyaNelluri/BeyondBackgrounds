from flask import Flask, render_template, request, redirect, url_for, session, flash
import snowflake.connector

app = Flask(__name__)
app.secret_key = 'navya'  # Replace with your own secret key



# Function to create a Snowflake connection
def create_snowflake_connection():
    snowflake_config = {
        'account': 'anohoex-igb93598',
        'user': 'BEYONDBACKGROUNDS',
        'password': 'Beyondpswd1',
        'warehouse': 'COMPUTE_WH',
        'database': 'BEYONDBACKGROUNDS',
        'schema': 'SCH_BEYONDBACKGROUNDS',
        'role': 'ACCOUNTADMIN'
    }

    try:
        conn = snowflake.connector.connect(**snowflake_config)
        return conn
    except Exception as e:
        print("Snowflake Connection Error:", str(e))
        raise e


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
                return redirect(url_for('user_details'))

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
                return redirect(url_for('user_details'))

        return render_template('applicant_register.html')

    else:
        flash('Invalid user type.', 'danger')
        return redirect(url_for('index'))
    
@app.route('/user_details')
def user_details():
    return render_template('user_details.html')

@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/home')
def home():
    return render_template('home.html')

def logout():
    session.pop('user', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)


