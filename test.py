import pytest
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



