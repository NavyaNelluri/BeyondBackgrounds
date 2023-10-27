import pytest
import app


def test_check_credentials_pass():
    username = 'Navya Nelluri'
    password = 'Navya.c@698'

    result = app.check_credentials(username, password)

    assert(result,True)


def test_check_credentials_fail():
    username = 'ABC'
    password = 'xyz'

    result = app.check_credentials(username, password)

    assert(result,False)



