import pytest
import uuid
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
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
    browser.set_window_size(1400, 1000)
    browser.get('http://petfriends.skillfactory.ru/login')

    _ = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'email')))

    field_email = browser.find_element('id',"email")
    field_email.clear()
    field_email.send_keys(valid_email)

    _ = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'pass')))

    field_pass = browser.find_element('id', "pass")
    field_pass.clear()
    field_pass.send_keys(valid_password)

    _ = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))

    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    _ = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'Мои питомцы')))

    browser.find_element(By.LINK_TEXT, "Мои питомцы").click()


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




