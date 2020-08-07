def test_submit_form(py):
    py.visit('https://demoqa.com/text-box')
    py.get('[id="userName"]').type("His name is Ramses")
    py.get('[id="userEmail"]').type('hisnameisramses@mailinator.com')
    py.get('[id="currentAddress"]').type('I live in random land drive')
    py.get('[id="permanentAddress"]').type('whatevers clevers, California')
    py.get('[id="submit"]').click()
    assert py.get('[id="submit"]').should().be_clickable()

def test_submit_form_refactored(py):
    py.visit('https://demoqa.com/text-box')
    py.get('[id="submit"]').click()
    assert py.get('[id="submit"]').should().be_clickable()
    