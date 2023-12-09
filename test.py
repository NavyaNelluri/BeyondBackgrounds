'''
The test.py contains all the test cases developed for the methods in the app.py
'''

#import required libraries
import pytest
import snowflake.connector
from app import check_credentials,get_usertype, get_user_details, update_user_details
from app import app

# Test snowflake connection
def test_snowflake_connection():
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

#Test case to test the pass scenario of login page
def test_check_credentials_pass():
    username = 'josna'
    password = 'josna123'

    #calls the function with wrong credentials
    result = check_credentials(username, password)
    print(result)

    assert result == True

#Test case to test the usertype as applicant
def test_usertype_applicant():
    username = 'josna'
    result = get_usertype(username)
    assert result == 'applicant'

#Test case to test the usertype as recruiter
def test_usertype_recruiter():
    username = 'Navya'
    result = get_usertype(username)
    assert result == 'recruiter'


#Test case to test the usertype as recruiter
def test_usertype_none():
    username = 'bcfjdhf'
    result = get_usertype(username)
    print(result)
    assert result == None

#Test case to test the genderinfo of the user 
def test_user_genderinfo():
    username = 'josna'
    result = get_user_details(username)
    print(result)

    assert result[1] == 'female'

#Test case to test the emailinfo of the user
def test_user_email():
    username = 'josna'
    result = get_user_details(username)

    assert result[3] == 'josna@gmail.com'

#Test case to test the non user scenario
def test_nonuser_info():
    username = 'ABC'
    result = get_user_details(username)

    assert result == None

#Test case to test the updation of location
def test_update_location():
    username = 'josna'
    field='preferred_location'
    new_value = 'chicago'
    update_user_details(username, field, new_value)
    result = get_user_details(username)

    assert result[7] == 'chicago'

#Test case to test to check name update
def test_update_name():
    username = 'josna'
    field='name'
    new_value = 'Josna'

    #the name should not be updated
    update_user_details(username, field, new_value)
    result = get_user_details(username)

    assert result[0] == 'josna'

#Test case to test to check gender update
def test_update_gender():
    username = 'josna'
    field='gender'
    new_value = 'male'

    #gender should not be updated
    update_user_details(username, field, new_value)
    result = get_user_details(username)

    assert result[1] == 'female'  

#test the about route
def test_about_route():
    client = app.test_client()
    response = client.get('/about')
    assert response.status_code == 200

#test the unavailable route
def test_route_fail():
    client = app.test_client()
    response = client.get('/index')
    assert response.status_code == 404
    
#test the applicants details route
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
    
#test the job postings route
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

