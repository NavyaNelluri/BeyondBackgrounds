import pytest
import snowflake.connector
from app import create_snowflake_connection  # Import your app's function



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
# Define your Snowflake connection parameters for testing 
#(this test case will pass since credentials are correct)
CORRECT_TEST_SNOWFLAKE_CONFIG = {
    'account': 'anohoex-igb93598',
        'user': 'BEYONDBACKGROUNDS',
        'password': 'Beyondpswd1',
        'warehouse': 'COMPUTE_WH',
        'database': 'BEYONDBACKGROUNDS',
        'schema': 'SCH_BEYONDBACKGROUNDS',
        'role': 'ACCOUNTADMIN'
}

def test_snowflake_connection01():
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

if __name__ == "__main__":
    pytest.main()
