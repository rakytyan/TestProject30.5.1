from selenium.webdriver.common.by import By

def test_all_pets_have_full_info(web_browser, capsys):
    '''Тест проверяет, что у всех питомцев разные имена'''

    rows = web_browser.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
    ''' 
            Rows содержит список объектов соответствующих строкам таблицы с карточками питомцев.
            Возьмем html код каждой строки и разделим на ячейки <td>. Первая ячейка в каждой строке 
            содержит фотографию, поэтому для формирования списка names из имен питомцев  
            берем ячейку с индексом [1].
            Проверяем уникальность каждого элемента этого списка.
            '''
    names = []
    for i in range(len(rows)):
        html = rows[i].get_attribute('innerHTML').replace('\n', '').replace('×', '')
        cells = html.split('<td>')
        names.append(cells[1].replace('</td>', '').strip())

    # with capsys.disabled():
    #     print(f"user profile is {names}")

    count = 0
    for i in range(len(names)):
        if names.count(names[i]) > 1:
            count += 1
    assert count == 0

# <th scope="row"><img src="" style="max-width: 100px; max-height: 100px;"> </th>
 #      <td> Опасный и без фото </td>
 #      <td> бультерьер </td>
 #      <td> 2 </td>
 #
 #      <td class="smart_cell">
 #
 #        <a onclick="delete_pet(&quot;3353ccca-13ff-4a3a-b427-fc0d935aa6b4&quot;);" title="Удалить питомца">
 #          <div title="Удалить питомца">
 #          ×
 #          </div>
 #        </a>
 #
 #      </td>








