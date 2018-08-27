from selenium import webdriver
from selenium.webdriver.common.by import By

class Browser:
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    def close(context):
        context.driver.close()
    def open(context, data):
        context.driver.get(data)
    def get_title(context):
        return context.driver.title
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