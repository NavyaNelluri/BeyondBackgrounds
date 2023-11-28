
import pytest
import snowflake.connector
from app import check_credentials,get_usertype  # Import your app's function
from app import app



# Define your Snowflake connection parameters for testing 
#(this test case will pass since credentials are wrong)

def test_snowflake_connection():
    # This test checks if the Snowflake connection can be established.
    try:
        conn = snowflake.connector.connect(
    account='xjtvekn-em26794',
    user='BEYONDBACKGROUNDS',
    password='Beyondpswd1',
    warehouse='COMPUTE_WH',
    database='BEYONDBACKGROUNDS',
    schema='SCH_BEYONDBACKGROUNDS',
    role='ACCOUNTADMIN'
)

        print(conn)

        assert isinstance(conn, snowflake.connector.connection.SnowflakeConnection)
    except Exception as e:
        pytest.fail(f"Snowflake Connection Error: {str(e)}")



#Test case to test the fail scenario of login page
def test_check_credentials_fail():
    username = 'cjdh'
    password = 'xyz'

    #calls the function with wrong credentials
    result = check_credentials(username, password)
    print(result)

    assert result == False

#Test case to test the fail scenario of login page
def test_check_credentials_pass():
    username = 'Navya'
    password = 'Navya.c@698'

    #calls the function with wrong credentials
    result = check_credentials(username, password)
    print(result)

    assert result == True

#Test case to test the fail scenario of login page
def test_usertype_applicant():
    username = 'josna123'

    #calls the function with wrong credentials
    result = get_usertype(username)
    print(result)

    assert result == 'applicant'

#Test case to test the fail scenario of login page
def test_usertype_recruiter():
    username = 'Navya'

    #calls the function with wrong credentials
    result = get_usertype(username)
    print(result)

    assert result == 'recruiter'


#Test case to test the fail scenario of login page
def test_usertype_none():
    username = 'bcfjdhf'

    #calls the function with wrong credentials
    result = get_usertype(username)
    print(result)

    assert result == None

def test_about_route():
    client = app.test_client()
    response = client.get('/about')
    assert response.status_code == 200

def test_route_fail():
    client = app.test_client()
    response = client.get('/index')
    assert response.status_code == 404
    
def test_applicant_details_route():
    client = app.test_client()
    response = client.post('/Applicant_Details', data={
        'NAME': 'John Doe',
        'CONTACT_NUMBER': '1234567890',
        'Email': 'john.doe@example.com',
        'SKILLS': 'Python, Flask',
        'EXPECTED_SALARY': '100000',
        'CURRENT_EMPLOYER': 'ABC Inc.',
        'CURRENT_SALARY': '90000',
        'PREFERRED_LOCATION': 'City ABC',
        'Criminal Record': 'No',
        'Reason': 'Looking for new opportunities'
    })

    assert response.status_code == 302
    
def test_job_postings_route():
    client = app.test_client()
    response = client.post('/job_postings', data={
        'companyName': 'ABC Corp',
        'locations': 'City XYZ',
        'email': 'abc@example.com',
        'jobPosition': 'Software Engineer',
        'salary': '90000',
        'benefits': 'Health insurance, flexible hours',
        'shiftTimings': '9 AM to 5 PM',
        'offenceExemptions': 'No convictions',
        'notes': 'Additional notes',
        'mandatCriminalRecord': 'Yes'
    }, follow_redirects=True)

    assert response.status_code == 200


if __name__ == "__main__":
    pytest.main()

