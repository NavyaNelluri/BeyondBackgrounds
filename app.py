from flask import Flask, render_template, request, redirect, url_for, session, flash
import snowflake.connector

app = Flask(__name__)
app.secret_key = 'navya'

app.error_message = None

# Function to create a Snowflake connection
def create_snowflake_connection():
    snowflake_config = {
        'account': 'xjtvekn-em26794',
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
                query = "INSERT INTO UserDetails(Username, Password, details, ContactEmail,UserType) VALUES (%s, %s, %s, %s,%s)"
                cursor.execute(query, (Username_form, Password_form, CompanyName, ContactEmail,user_type))
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
        if request.method == 'POST':
            try:
                Username_form = request.form['username_form']
                Password_form = request.form['password_form']
                CompanyName = request.form['fullname']
                ContactEmail = request.form['email']
                print("hi")
                # Create a new Snowflake connection
                conn = create_snowflake_connection()
        
                # Execute an SQL insert statement using the Snowflake connection
                cursor = conn.cursor()
                query = "INSERT INTO UserDetails(Username, Password, details, ContactEmail, UserType) VALUES (%s, %s, %s, %s,%s)"
                cursor.execute(query, (Username_form, Password_form, CompanyName, ContactEmail,user_type))
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
        user_type = request.form['user_type']

        user_type_from_database = get_usertype(username)

        session['username'] = username
        
        # Check the database for the username and password
        if check_credentials(username, password) and user_type == user_type_from_database and user_type == 'recruiter':
            #Redirects to Dashboard on successful login
            return redirect(url_for('Recruiter_home'))
        elif check_credentials(username, password) and user_type == user_type_from_database and user_type == 'applicant':
            return redirect(url_for('Applicant_home'))
        else:
            #Error message on login failure
            app.error_message = 'Invalid username or password or user type'

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

@app.route('/')
def home():
    return render_template('home.html')

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
            GENDER = request.form['GENDER']
            Email = request.form['Email']
            SKILLS = request.form['SKILLS']
            EXPECTED_SALARY = request.form['EXPECTED_SALARY']
            CURRENT_EMPLOYER = request.form['CURRENT_EMPLOYER']
            CURRENT_SALARY = request.form['CURRENT_SALARY']
            PREFERRED_LOCATION = request.form['PREFERRED_LOCATION']
            Criminal_Record = request.form['CriminalRecord']
            Reason = request.form.get('Reason') if Criminal_Record == 'yes' else "Not Applicable"
            print(f"Criminal_Record: {Criminal_Record}, Reason: {Reason}")

            # Create a new Snowflake connection
            conn = create_snowflake_connection()
 
            # Execute an SQL insert statement using the Snowflake connection
            cursor = conn.cursor()
 
            query = """
INSERT INTO JOBAPPLICANTS (NAME, CONTACT_NUMBER,GENDER, Email, SKILLS, EXPECTED_SALARY, CURRENT_EMPLOYER, CURRENT_SALARY, PREFERRED_LOCATION, Criminal_Record, Reason)
VALUES (%s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s)
"""         
            # Execute the query with parameters
            cursor.execute(query, (
                NAME, CONTACT_NUMBER,GENDER,  Email, SKILLS, EXPECTED_SALARY, CURRENT_EMPLOYER,
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
        
@app.route('/AppliedJobs')
def AppliedJobs():
  try:
        # Create a Snowflake connection
        conn = create_snowflake_connection()

        # Execute an SQL select statement using the Snowflake connection
        cursor = conn.cursor()
        query = "SELECT * FROM AppliedJobs"
        cursor.execute(query)
        jobs = cursor.fetchall()

        cursor.close()
        conn.close()
        print(jobs)
        return render_template('AppliedJobs.html', jobs=jobs)
  except Exception as e:
        print(e)
        app.logger.error(f"An error occurred: {str(e)}")
        flash('An error occurred. Please try again later.', 'error')
@app.route('/filter_applicants', methods=['GET', 'POST'])
def filter_applicants():
    try:
        if request.method == 'POST':
            # Retrieve filter parameters from the form
            skills_filter = request.form.get('skills')
            criminal_record_filter = request.form.get('criminal_record')

            # Create a Snowflake connection
            conn = create_snowflake_connection()

            # Build the SQL query based on the filter parameters
            query = "SELECT * FROM JOBAPPLICANTS WHERE "

            if skills_filter:
                query += f"  SKILLS LIKE '%{skills_filter}%' and"
            else:
                query += f" "                
            if criminal_record_filter == 'yes':
                query += "   CRIMINAL_RECORD = 'yes'"
            elif criminal_record_filter == 'no':
                query += "   CRIMINAL_RECORD = 'no'"
            else:
                query = "SELECT * FROM JOBAPPLICANTS"
            print(query)

            # Execute the SQL query
            cursor = conn.cursor()
            cursor.execute(query)
            print("hi")
            filtered_applicants = cursor.fetchall()
            cursor.close()
            conn.close()

            return render_template('filter_applicants.html', jobs=filtered_applicants)

    except Exception as e:
        print(e)
        app.logger.error(f"An error occurred: {str(e)}")
        flash('An error occurred. Please try again later.', 'error')

        # You can include additional information in the template context
        return render_template('filter_applicants.html', jobs=[], error_message=str(e))

    # Add a fallback return statement if the 'try' block doesn't execute successfully
    return render_template('filter_applicants.html', jobs=[], error_message="An unexpected error occurred.")


def get_user_details(username):
    # Replace the connection details with your database connection
    conn = create_snowflake_connection()
    cursor = conn.cursor()

    # Assuming there's a 'users' table with columns 'name', 'email', etc.
    cursor.execute("SELECT name, gender, contact_number, email,skills, expected_salary, current_employer, \
                   preferred_location, criminal_record, reason  FROM JOBAPPLICANTS WHERE name = %s", (username,))  # Change the query as needed
    user_details = cursor.fetchone()

    conn.close()

    return user_details


def update_user_details(username, field, new_value):
    conn = create_snowflake_connection()
    cursor = conn.cursor()
    if field != 'name' and field != 'gender':
        update_query = f"UPDATE jobapplicants SET {field} = %s WHERE name = %s"
        cursor.execute(update_query, (new_value, username))
    conn.commit()
    conn.close()

@app.route('/UserProfile')
def user_profile():
    username = session.get('username')
    user_details = get_user_details(username)
    return render_template('UserProfile.html', user_details=user_details)

@app.route('/update_profile', methods=['POST'])
def update_profile():
    if request.method == 'POST':
        username = session.get('username')
        updated_fields = ['email', 'contact_number', 'skills', 'expected_salary', 'current_employer', 'preferred_location']
        for field in updated_fields:
            new_value = request.form.get(field)
            if new_value is not None and new_value != '':
                update_user_details(username, field, new_value)
        return redirect(url_for('user_profile'))
    else:
        return redirect(url_for('user_profile'))

@app.route('/recruiter/dashboard')
def recruiter_dashboard():
    return render_template('recruiter_dashboard.html')
    
@app.route('/JobPostings')
def JobPostingsPage():
    return render_template('JobPostings.html')

@app.route('/ApplicantDetails')
def ApplicantDetailsPage():
    return render_template('ApplicantDetails.html')
    
@app.route('/apply_for_job/<job_id>')
def apply_for_job(job_id):
    try:
        # Your logic to handle the job application using the job_id
        # This could involve updating the database, logging the application, etc.
        conn = create_snowflake_connection()
        cursor = conn.cursor()
        username = session.get('username')
        insert_query = """
        INSERT INTO AppliedJobs (JobID, ApplicantUsername, ApplicationDate)
        VALUES
            ('{}', '{}', CURRENT_TIMESTAMP());
        """.format(job_id, username)
        print(insert_query)
        # Execute the insert query
        cursor.execute(insert_query)

        # Commit the transaction
        conn.commit()

        # Close the Snowflake connection
        conn.close()

        flash('Application submitted successfully!', 'success')
        return redirect(url_for('JobPortal'))

    except Exception as e:
        # Handle exceptions if necessary
        print(e)
        flash('An error occurred. Please try again later.', 'error')
        return redirect(url_for('JobPortal'))
    
if __name__ == '__main__':
    app.run(debug=True)
