# import time
# from settings import valid_email, valid_password

# import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

def test_all_pets_displayed(web_browser, capsys):
    '''Тест проверяет, что на странице со списком питомцев пользователя присутствуют все питомцы.
    Использован явный вид ожидания.'''

    _ = WebDriverWait(web_browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.table.table-hover tbody tr')))

    users_profile=web_browser.find_elements(By.CSS_SELECTOR, '.\\.col-sm-4.left')

    with capsys.disabled():
        print(f"user profile is {users_profile[0].text}")

    number = users_profile[0].text.split('\n')
    number = number[1].split(' ')
    number = int(number[1])

    rows = web_browser.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
    assert number == len(rows)
