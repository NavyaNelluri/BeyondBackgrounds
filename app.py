from flask import Flask, render_template, request, redirect, url_for, session, flash
import snowflake.connector

app = Flask(__name__)
app.secret_key = 'navya'  # Replace with your own secret key

# Mock user data (replace with a database)
users = []

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
    return render_template('login.html')

@app.route('/register/<user_type>', methods=['GET', 'POST'])
def register(user_type):
    if user_type == 'recruiter':
        if request.method == 'POST':
            try:
                Username_form = request.form['username_form']
                Password_form = request.form['password_form']
                CompanyName = request.form['company']
                ContactEmail = request.form['email']
        
                # Create a new Snowflake connection
                conn = create_snowflake_connection()
        
                # Execute an SQL insert statement using the Snowflake connection
                cursor = conn.cursor()
                query = "INSERT INTO UserDetails(Username, Password, details, ContactEmail) VALUES (%s, %s, %s, %s)"
                cursor.execute(query, (Username_form, Password_form, CompanyName, ContactEmail))
                cursor.close()
        
                # Commit the transaction
                conn.commit()
        
                # Close the Snowflake connection
                conn.close()
        
                # If the insertion is successful, flash a success message and redirect to a different page
                flash('Registration successful', 'success')
            except Exception as e:
                print(e)
                app.logger.error(f"An error occurred: {str(e)}")
                flash('An error occurred. Please try again later.', 'error')

        return render_template('recruiter_register.html')

    elif user_type == 'applicant':
        return render_template('applicant_register.html')

    else:
        flash('Invalid user type.', 'danger')
        return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    print("hi")
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check the database for the record based on username and password
        if check_credentials(username, password):
            # Successful login
            return redirect(url_for('dashboard'))
        else:
            # Invalid credentials
            flash('Invalid username or password', 'error')

    return render_template('login.html')

def check_credentials(username, password):
    try:
        # Create a new Snowflake connection
        conn = create_snowflake_connection()

        # Execute an SQL query to check the credentials
        cursor = conn.cursor()
        query = "SELECT * FROM UserDetails WHERE USERNAME = %s AND PASSWORD = %s"
        cursor.execute(query, (username, password))

        results = cursor.fetchall()
        cursor.close()

        if results:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False

@app.route('/dashboard')
def dashboard():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/Recruiter_home')
def Recruiter_home():
    return render_template('Recruiter_home.html')

@app.route('/JobPostings')
def JobPostingsPage():
    return render_template('JobPostings.html')


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/register/applicant', methods=['GET', 'POST'])
def register_applicant():
    
    return render_template('applicant_register.html')

@app.route('/job_postings', methods=['POST'])
def job_postings():
    if request.method == 'POST':
        try:
            # Extract job details from the form
            company_name = request.form['companyName']
            locations = request.form['locations']
            email = request.form['email']
            job_position = request.form['jobPosition']
            salary = request.form['salary']
            benefits = request.form['benefits']
            shift_timings = request.form['shiftTimings']
            offence_exemptions = request.form['offenceExemptions']
            notes = request.form['notes']
            mandat_criminal_record = request.form['mandatCriminalRecord']

            # Create a new Snowflake connection
            conn = create_snowflake_connection()

            # Execute an SQL insert statement using the Snowflake connection
            cursor = conn.cursor()

            query = """
INSERT INTO JobDetails (CompanyName, Locations, Email, JobPosition, Salary, Benefits, shift_timings, OffenceExemptions, Notes, mandat_criminal_record)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""         
            # Execute the query with parameters
            cursor.execute(query, (
                company_name, locations, email, job_position, salary, benefits,
                shift_timings, offence_exemptions, notes, str(mandat_criminal_record)
            ))
            cursor.close()

            # Commit the transaction
            conn.commit()

            # Close the Snowflake connection
            conn.close()

            flash('Job posting details added to Snowflake.', 'success')

        except Exception as e:
            print(e)
            app.logger.error(f"An error occurred: {str(e)}")
            flash('An error occurred. Please try again later.', 'error')

    return redirect(url_for('JobPostingsPage'))
@app.route('/JobPortal')
def JobPortal():
    print("hi")
    try:
        # Create a Snowflake connection
        conn = create_snowflake_connection()

        # Execute an SQL select statement using the Snowflake connection
        cursor = conn.cursor()
        query = "SELECT * FROM JobDetails"
        cursor.execute(query)
        jobs = cursor.fetchall()

        cursor.close()
        conn.close()
        print(jobs)
        return render_template('JobPortal.html', jobs=jobs)
    except Exception as e:
        print(e)
        app.logger.error(f"An error occurred: {str(e)}")
        flash('An error occurred. Please try again later.', 'error')
        
if __name__ == '__main__':
    app.run(debug=True)
