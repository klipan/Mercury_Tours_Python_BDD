from behave import step, then
from features.pages.elements import Elements
from features.pages.elements import Data

@step('Go to Mercury Tours site')
def step_impl(context):
    context.browser.open(Elements._URL_1)
    assert context.browser.get_title() == Elements._title_1page
@step('Click on Register tab')
def step_impl(context):
    context.browser.click_on_element(Elements._LINK, Elements._path_register)
@step('Fill out all required fields with valid credentials')
def step_impl(context):
    context.browser.send_text_to_element(Elements._CSS, Elements._path_email, Data._username)
    context.browser.send_text_to_element(Elements._CSS, Elements._path_password, Data._password)
    context.browser.send_text_to_element(Elements._CSS, Elements._path_confPass, Data._password)
@step('Click Submit')
def step_impl(context):
    context.browser.click_on_element(Elements._CSS,Elements._path_submit)
@step('Verify that submit is successful')
def step_impl(context):
    assert context.browser.get_url() == Elements._URL_2
@step('Click on sign-in link')
def step_impl(context):
    context.browser.click_on_element(Elements._CSS, Elements._path_singIn)
@step('Fill out username and password with valid credentials')
def step_impl(context):
    context.browser.send_text_to_element(Elements._CSS, Elements._path_username, Data._username)
    context.browser.send_text_to_element(Elements._CSS, Elements._path_password, Data._password)
@step('Verify that login is successful')
def step_impl(context):
    assert context.browser.get_title() == Elements._title_2page
@step('Fill out username and password with error credentials')
def step_impl(context):
    context.browser.send_text_to_element(Elements._CSS, Elements._path_username, Data._error_username)
    context.browser.send_text_to_element(Elements._CSS, Elements._path_password, Data._error_password)
@step('Verify that login is unsuccessful')
def step_impl(context):
    assert context.browser.get_title() == Elements._title_3page
@step('Fill in Flight Details and Preferences')
def step_impl(context):
    context.browser.select_from_dropdown(Elements._CSS, Elements._path_city_from, Data._city_from)
    context.browser.select_from_dropdown('December', Elements._path_month_from, Elements._CSS)
    context.browser.select_from_dropdown('12', Elements._path_day_from, Elements._CSS)
    context.browser.select_from_dropdown('October', Elements._path_month_from, Elements._CSS)
    context.browser.select_from_dropdown('13', Elements._path_day_to, Elements._CSS)
    context.browser.select_from_dropdown('October', Elements._path_month_to, Elements._CSS)
    context.browser.select_from_dropdown(Data._city_to, Elements._path_city_to, Elements._CSS)
    context.browser.click_on_element(Elements._CSS, Elements._business_class)
    context.browser.select_from_dropdown('Blue Skies Airlines', Elements._path_airline, Elements._CSS)
@step('Verify that page with listed flights is showing')
def step_impl(context):
    assert context.browser.get_title() == Elements._title_4page

