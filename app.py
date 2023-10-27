from flask import Flask, request
import snowflake.connector

app = Flask(__name__)
app.secret_key = 'navya' 

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
    conn = snowflake.connector.connect(**snowflake_config)
    print(conn)
        

create_snowflake_connection()
