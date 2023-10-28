import pytest
<<<<<<< HEAD
import snowflake.connector
from app import create_snowflake_connection


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



if __name__ == "__main__":
    pytest.main()
=======
import app


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



>>>>>>> 5aa57d8e9a8e1792a6ebe0acf101024967b67fda
