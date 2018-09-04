from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Browser:
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)


def close(context):
    context.driver.close()

def open(context, data):
    context.driver.get(data)

def get_title(context):
    return context.driver.title

def get_url(context):
    return context.driver.current_url

def get_by_type(context, locator_type):
    if locator_type == 'css':
        return By.CSS_SELECTOR
    elif locator_type == 'xpath':
        return By.XPATH
    elif locator_type == 'link':
        return By.LINK_TEXT
    else:
        print("Unknown selector")

def get_element(context, locator_type, locator):
    by_type = context.get_by_type(locator_type)
    element = context.driver.find_element(by_type, locator)
    return element

def click_on_element(context, locator_type, locator):
    context.get_element(locator_type, locator).click()

def send_text_to_element(context, locator_type, locator, data):
    context.get_element(locator_type, locator).send_keys(data)

def text_of_element(context, inner_text, locator, locator_type='xpath'):
    element_text = context.get_element(locator, locator_type)
    if element_text == inner_text:
        return True
    else:
        print("Error")
        return False

def select_from_dropdown(context, visible_text, locator_type, locator):
    try:
        select_dropdown = Select(context.get_element(locator_type, locator))
        select_dropdown.select_by_visible_text(visible_text)
        print("Selected element is: " + visible_text)
    except:
        print("Element not found " + locator)