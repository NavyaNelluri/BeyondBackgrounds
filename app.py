from flask import Flask, render_template, request, redirect, url_for, session, flash
import snowflake.connector

app = Flask(__name__)
app.secret_key = 'navya'

app.error_message = None

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
        print("hi")
        if request.method == 'POST':
            try:
                Username_form = request.form['username_form']
                Password_form = request.form['password_form']
                CompanyName = request.form['fullname']
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

        return render_template('applicant_register.html')


#login page to enter username and password
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user_type = get_usertype(username)
        
        # Check the database for the username and password
        if check_credentials(username, password) and user_type == 'recruiter':
            #Redirects to Dashboard on successful login
            return redirect(url_for('recruiter_dashboard'))
        elif check_credentials(username, password) and user_type == 'applicant':
            return redirect(url_for('applicant_dashboard'))
        else:
            #Error message on login failure
            app.error_message = 'Invalid username or password'

    return render_template('login.html', error_message=app.error_message)


#Checks the provided crendentials for authentication
def check_credentials(username, password):
    try:
        #Database connection establishment 
        conn = create_snowflake_connection()
        cursor = conn.cursor()

        #Execute the query
        query = "SELECT * FROM UserDetails WHERE USERNAME = %s AND PASSWORD = %s"
        cursor.execute(query, (username, password))

        #Fetch the results
        results = cursor.fetchall()
        print(results)
        cursor.close()

        if results:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False
    
#Checks the provided crendentials for authentication
def get_usertype(username):
    try:
        # Database connection establishment 
        conn = create_snowflake_connection()
        cursor = conn.cursor()

        # Execute the query
        query = "SELECT usertype FROM UserDetails WHERE USERNAME = %s"
        cursor.execute(query, (username,))

        # Fetch the usertype from the result
        result = cursor.fetchone()

        cursor.close()

        if result:
            return result[0]  # Return the usertype
        else:
            return None  # No result found for the username
    except Exception as e:
        print(e)
        return None


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/Recruiter_home')
def Recruiter_home():
    return render_template('Recruiter_home.html')
@app.route('/Applicant_home')
def Applicant_home():
    return render_template('Applicant_home.html')

@app.route('/JobPostings')
def JobPostingsPage():
    return render_template('JobPostings.html')
@app.route('/ApplicantDetails')
def ApplicantDetailsPage():
    return render_template('ApplicantDetails.html')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register/applicant', methods=['GET', 'POST'])
def register_applicant():  
    return render_template('applicant_register.html')

@app.route('/applicant/dashboard')
def applicant_dashboard():
    return render_template('applicant_dashboard.html')

  
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

@app.route('/Applicant_Details', methods=['POST'])
def Applicant_Details():
    if request.method == 'POST':
        try:
            # Extract job details from the form
            NAME = request.form['NAME']
            CONTACT_NUMBER = request.form['CONTACT_NUMBER']
            Email = request.form['Email']
            SKILLS = request.form['SKILLS']
            EXPECTED_SALARY = request.form['EXPECTED_SALARY']
            CURRENT_EMPLOYER = request.form['CURRENT_EMPLOYER']
            CURRENT_SALARY = request.form['CURRENT_SALARY']
            PREFERRED_LOCATION = request.form['PREFERRED_LOCATION']
            Criminal_Record = request.form['Criminal Record']
            Reason = request.form['Reason']
 
            # Create a new Snowflake connection
            conn = create_snowflake_connection()
 
            # Execute an SQL insert statement using the Snowflake connection
            cursor = conn.cursor()
 
            query = """
INSERT INTO JOBAPPLICANTS (NAME, CONTACT_NUMBER, Email, SKILLS, EXPECTED_SALARY, CURRENT_EMPLOYER, CURRENT_SALARY, PREFERRED_LOCATION, Criminal_Record, Reason)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""         
            # Execute the query with parameters
            cursor.execute(query, (
                NAME, CONTACT_NUMBER, Email, SKILLS, EXPECTED_SALARY, CURRENT_EMPLOYER,
                CURRENT_SALARY, PREFERRED_LOCATION, Criminal_Record, Reason)  # Fix typo here
            )

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
 
    return redirect(url_for('ApplicantDetailsPage'))

@app.route('/JobPortal')
def JobPortal():
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

@app.route('/recruiter/dashboard')
def recruiter_dashboard():
    return render_template('recruiter_dashboard.html')

      
if __name__ == '__main__':
    app.run(debug=True)
