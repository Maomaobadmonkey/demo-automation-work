def test_radio_button_yes(py):
    py.visit('https://demoqa.com/radio-button')
    py.get('[id="yesRadio"]').click(force=True)
    assert py.get('.text-success').should().have_text('Yes')

def test_radio_button_impressive(py):
    py.visit('https://demoqa.com/radio-button')
    py.get('[id="impressiveRadio"]').click(force=True)
    assert py.get('.text-success').should().have_text('Impressive')

def test_radio_button_no(py):
    py.visit('https://demoqa.com/radio-button')
    enable_no = py.get('#noRadio')
    py.execute_script('arguments[0].disabled = false', enable_no.webelement)
    enable_no.click(force=True)
    assert enable_no.is_selected()

