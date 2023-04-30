from selenium.webdriver.common.by import By

def test_all_pets_have_full_info(web_browser, capsys):
    """
    Тест проверяет, что у всех питомцев есть имя, возраст и порода.
    """

    rows = web_browser.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
    ''' 
    rows содержит список объектов соответствующих строкам таблицы с карточками питомцев.
    Возьмем html код каждой строки и разделим на ячейки <td>. Первая ячейка в каждой строке 
    содержит фотографию. По условиям задания 30.3.1 проверяются только наличие имени, 
    возраста и породы, поэтому в цикле первая ячейка индексом [0], которая содержит фото,
    пропускается.   
    '''
    for i in range(len(rows)):
        html = rows[i].get_attribute('innerHTML').replace('\n', '').replace('×', '')
        cells = html.split('<td>')
        for k in range(1, len(cells)):
            x = cells[k].replace('</td>', '').split('<td ')[0].strip()
            assert len(x) > 0


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







