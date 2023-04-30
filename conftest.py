import pytest
import uuid
import time
from settings import valid_email, valid_password

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # This function helps to detect that some test failed
    # and pass this information to teardown:

    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture
def web_browser(request, selenium):

    browser = selenium

    browser.get('http://petfriends.skillfactory.ru/login')
    field_email = browser.find_element('id',"email")
    field_email.clear()
    field_email.send_keys(valid_email)

    field_pass = browser.find_element('id', "pass")
    field_pass.clear()
    field_pass.send_keys(valid_password)

    btn_submit = browser.find_element('xpath', "//button[@type='submit']")
    btn_submit.click()

    browser.implicitly_wait(10)

    browser.get("https://petfriends.skillfactory.ru/my_pets")

    assert browser.current_url == 'https://petfriends.skillfactory.ru/my_pets'

    # Return browser instance to test case:
    yield browser

    # Do teardown (this code will be executed after each test):

    if request.node.rep_call.failed:
        # Make the screen-shot if test failed:
        try:
            browser.execute_script("document.body.bgColor = 'white';")

            # Make screen-shot for local debug:
            browser.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')

            # For happy debugging:
            print('URL: ', browser.current_url)
            print('Browser logs:')
            for log in browser.get_log('browser'):
                print(log)

        except:
            pass # just ignore any errors here




#
# import pytest
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# import uuid
#
# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item, call):
#     # This function helps to detect that some test failed
#     # and pass this information to teardown:
#
#     outcome = yield
#     rep = outcome.get_result()
#     setattr(item, "rep_" + rep.when, rep)
#     return rep
#
# @pytest.fixture(autouse=True)
# def testing():
#     pytest.driver = webdriver.Chrome('./chromedriver.exe')
#
#     yield
#
#     pytest.driver.quit()
