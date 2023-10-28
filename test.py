import pytest
import snowflake.connector
from app import create_snowflake_connection  # Import your app's function




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

        assert isinstance(conn, snowflake.connector.connection.SnowflakeConnection)
    except Exception as e:
        pytest.fail(f"Snowflake Connection Error: {str(e)}")


# Test case for user namefield presence
def test_username():
    username = False
    with open('templates/applicant_register.html', 'r') as file:
        for line in file:
            if 'id="username"' in line:
                username = True
                break
    if username:
        print("passed")
    else:
        print("failed")
# Running the test case
test_username()

#Test case to test the success scenario of login page
def test_check_credentials_pass():
    username = 'Navya Nelluri'
    password = 'Navya.c@698'

    #calls the function with correct credentials
    result = app.check_credentials(username, password)

    assert(result,True)

#Test case to test the fail scenario of login page
def test_check_credentials_fail():
    username = 'ABC'
    password = 'xyz'

    #calls the function with wrong credentials
    result = app.check_credentials(username, password)

    assert(result,False)


if __name__ == "__main__":
    pytest.main()
