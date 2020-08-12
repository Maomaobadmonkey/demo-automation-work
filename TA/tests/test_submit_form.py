import pytest

# My approach here, was to take the original elements and break them for a more general use
# By putting the case into a fixture, I was able to reduce reliance on copy pasting the same site per case

def test_submit_form_original(py):
    py.visit('https://demoqa.com/text-box')
    py.get('[id="userName"]').type("His name is Ramses")
    py.get('[id="userEmail"]').type('hisnameisramses@mailinator.com')
    py.get('[id="currentAddress"]').type('I live in random land drive')
    py.get('[id="permanentAddress"]').type('whatevers clevers, California')
    py.get('[id="submit"]').click()
    assert py.get('[id="submit"]').should().be_clickable()

# I created a new fixture for the site link since its going
# to be a constant for all the tests related to this page

@pytest.fixture
def visit_text_box(py):
    py.visit('https://demoqa.com/text-box')

# I broke out the first name field because in many forms first name tends to be always asked
def first_name_field(py):
    firstname = 'Buddy'
    py.get('[id="userName"]').type(firstname)

# I broke out the email field because similar to first name, emails are commonly used fields
def email_field(py):
    email = 'words@whatever.com'
    py.get('[id="userEmail"]').type(email)

# address fields are common in many programs that ask for shipping of products
def address_field_1(py):
    address = 'Somewhere Drive, 15191'
    py.get('[id="currentAddress"]').type(address)

# similar to address field 1
def address_field_2(py):
    address = 'whatevers clevers, California'
    py.get('[id="permanentAddress"]').type(address)


# My new test code using a more refactored approach
def test_submit_form_refactored(py,visit_text_box):
    first_name_field(py)
    email_field(py)
    address_field_1(py)
    address_field_2(py)
    py.get('[id="submit"]').click()
    assert py.get('[id="submit"]').should().be_clickable()
