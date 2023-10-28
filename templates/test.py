# Test case for email field presence
def test_username():
    email_field_exists = False
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