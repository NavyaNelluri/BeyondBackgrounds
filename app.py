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

@app.route('/JobPostings')
def JobPostingsPage():
    return render_template('JobPostings.html')


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register/applicant', methods=['GET', 'POST'])
def register_applicant():  
    return render_template('applicant_register.html')

@app.route('/applicant/dashboard')
def applicant_dashboard():
    return render_template('applicant_dashboard.html')

@app.route('/recruiter/dashboard')
def recruiter_dashboard():
    return render_template('recruiter_dashboard.html')
      
if __name__ == '__main__':
    app.run(debug=True)
