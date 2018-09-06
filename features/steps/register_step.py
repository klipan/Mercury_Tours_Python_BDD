from behave import step, then

@step('Go to Mercury Tours site')
def step_impl(context):
    context.browser.open('http://newtours.demoaut.com/')
    assert context.browser.get_title() == 'Welcome: Mercury Tours'
@step('Click on Register tab')
def step_impl(context):
    context.browser.click_on_element('link', 'REGISTER')
@step('Fill out all required fields with valid credentials')
def step_impl(context):
    context.browser.send_text_to_element('css', '[name=email]', 'Pobeda')
    context.browser.send_text_to_element('css', '[name=password]', 'Hasta la Victoria Siempre')
    context.browser.send_text_to_element('css', '[name=confirmPassword]', 'Hasta la Victoria Siempre')
@step('Click Submit')
def step_impl(context):
    context.browser.click_on_element('css','[type=image]')
@step('Verify that submit is successful')
def step_impl(context):
    assert context.browser.get_url() == 'http://newtours.demoaut.com/create_account_success.php'
@step('Click on sign-in link')
def step_impl(context):
    context.browser.click_on_element('css', '[href="mercurysignon\.php"]')
@step('Fill out username and password with valid credentials')
def step_impl(context):
    context.browser.send_text_to_element('css', '[name=userName]', 'Pobeda')
    context.browser.send_text_to_element('css', '[name=password]', 'Hasta la Victoria Siempre')
@step('Verify that login is successful')
def step_impl(context):
    assert context.browser.get_title() == 'Find a Flight: Mercury Tours:'
@step('Fill out username and password with error credentials')
def step_impl(context):
    context.browser.send_text_to_element('css', '[name=userName]', 'SSS123')
    context.browser.send_text_to_element('css', '[name=password]', '123FDEWT')
@step('Verify that login is unsuccessful')
def step_impl(context):
    assert context.browser.get_title() == 'Sign-on: Mercury Tours'
@step('Fill in Flight Details and Preferences')
def step_impl(context):
    context.browser.select_from_dropdown('css', '[name=fromPort]', 'Paris')
    context.browser.select_from_dropdown('December', '[name=fromMonth]', 'css')
    context.browser.select_from_dropdown('12', '[name=fromDay]', 'css')
    context.browser.select_from_dropdown('October', '[name=fromMonth]', 'css')
    context.browser.select_from_dropdown('13', '[name=toDay]', 'css')
    context.browser.select_from_dropdown('October', '[name=toMonth]', 'css')
    context.browser.select_from_dropdown('Sydney', '[name=toPort]', 'css')
    context.browser.click_on_element('css', '[value = Business]')
    context.browser.select_from_dropdown('Blue Skies Airlines', '[name=airline]', 'css')
@step('Verify that page with listed flights is showing')
def step_impl(context):
    assert context.browser.get_title() == 'Select a Flight: Mercury Tours'

