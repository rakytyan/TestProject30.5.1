from selenium.webdriver.common.by import By

def test_half_pets_have_photo(web_browser):
    '''Тест проверяет, что хотя бы у половины питомцев есть фото'''

    users_profile=web_browser.find_elements(By.CSS_SELECTOR, '.\\.col-sm-4.left')

    number = users_profile[0].text.split('\n')
    number = number[1].split(' ')
    number = int(number[1])

    images = web_browser.find_elements(By.CSS_SELECTOR, '.table.table-hover img')

    photos = 0
    for i in range(len(images)):
        if images[i].get_attribute('src') != '':
            photos += 1

    assert photos * 2 >= number



