from behave import step, then

@step('Go to Mercury Tours site')
def step_impl(context):
    context.browser.open('http://newtours.demoaut.com/')
    assert context.browser.get_title() == 'Welcome: Mercury Tours'
@step('Click on Register tab')
def step_impl(context):
    context.browser.click_on_element('link', 'REGISTER')
@step('Fill out all required fields')
def step_impl(context):
    pass
@step('Click Submit')
def step_impl(context):
    pass
@step('Verify that submit is successful')
def step_impl(context):
    pass