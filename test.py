
import pytest
import snowflake.connector
from app import check_credentials,get_usertype  # Import your app's function
from app import app



# Define your Snowflake connection parameters for testing 
#(this test case will pass since credentials are wrong)

def test_snowflake_connection():
    # This test checks if the Snowflake connection can be established.
    try:
        conn = snowflake.connector.connect(account= 'anohoex-igb93598',
        user= 'BEYONDBACKGROUNDS',
        password= 'Beyondpswd1',
        warehouse= 'COMPUTE_WH',
        database= 'BEYONDBACKGROUNDS',
        schema= 'SCH_BEYONDBACKGROUNDS',
        role= 'ACCOUNTADMIN')
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
    username = 'ABC'
    password = 'abc'

    #calls the function with wrong credentials
    result = check_credentials(username, password)
    print(result)

    assert result == True

#Test case to test the fail scenario of login page
def test_usertype_applicant():
    username = 'ABC'

    #calls the function with wrong credentials
    result = get_usertype(username)
    print(result)

    assert result == 'applicant'

#Test case to test the fail scenario of login page
def test_usertype_recruiter():
    username = 'XYZ'

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

if __name__ == "__main__":
    pytest.main()

