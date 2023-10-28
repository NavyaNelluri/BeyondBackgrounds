from flask import Flask, request, render_template, redirect, url_for
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
    print("Snowflake Configuration:", snowflake_config)

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
        
        # Check the database for the username and password
        if check_credentials(username, password):
            #Redirects to Dashboard on successful login
            return redirect(url_for('dashboard'))
        else:
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

#Redirects to Dashboard
@app.route('/dashboard')
def dashboard():
    return 'Welcome to the Beyond Backgrounds'

if __name__ == '__main__':
    app.run(debug=True)
