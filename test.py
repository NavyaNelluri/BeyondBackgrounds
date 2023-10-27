import pytest
import snowflake.connector
from app import create_snowflake_connection  # Import your app's function

# Define your Snowflake connection parameters for testing 
#(this test case will fail since credentials are wrong)
TEST_SNOWFLAKE_CONFIG = {
    'account': 'anohoex-igb93598',
        'user': 'BEYONDBACKGROUNDS01',
        'password': 'Beyondpswd1',
        'warehouse': 'COMPUTE_WH',
        'database': 'BEYONDBACKGROUNDS',
        'schema': 'SCH_BEYONDBACKGROUNDS',
        'role': 'ACCOUNTADMIN'
}

def test_snowflake_connection():
    # This test checks if the Snowflake connection can be established.
    try:
        conn = snowflake.connector.connect(**TEST_SNOWFLAKE_CONFIG)

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
        conn = snowflake.connector.connect(**CORRECT_TEST_SNOWFLAKE_CONFIG)

        assert isinstance(conn, snowflake.connector.connection.SnowflakeConnection)
    except Exception as e:
        pytest.fail(f"Snowflake Connection Error: {str(e)}")

if __name__ == "__main__":
    pytest.main()
