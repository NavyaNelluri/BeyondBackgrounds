# test.py

# Test case for email field presence
def test_email_field_presence():
    email_field_exists = False
    with open('index.html', 'r') as file:
        for line in file:
            if 'id="email"' in line:
                email_field_exists = True
                break

    if email_field_exists:
        print("passed")
    else:
        print("failed")

# Running the test case
test_email_field_presence()
