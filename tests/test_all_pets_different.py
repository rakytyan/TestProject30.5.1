from selenium.webdriver.common.by import By

def test_all_pets_have_full_info(web_browser, capsys):
    '''Тест проверяет, что в списке нет повторяющихся питомцев'''

    rows = web_browser.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
    ''' 
        Rows содержит список объектов соответствующих строкам таблицы с карточками питомцев.
        Возьмем html код каждой строки и разделим на ячейки <td>. Первая ячейка в каждой строке 
        содержит фотографию. Так как в задании было определено, что повторяющиеся питомцы — 
        это питомцы, у которых одинаковое имя, порода и возраст, соответственно проверка 
        уникальности фото не должна проводиться и в цикле первая ячейка индексом [0], 
        которая содержит фото, пропускается.   
        Соберем имя, породу и возраст в одну строку pet_element и сформируем список 
        pet_elements из получившихся элементов. Затем проверяем уникальность каждого элемента списка.  
        '''
    pets_elements = []
    for i in range(len(rows)):
        html = rows[i].get_attribute('innerHTML').replace('\n', '').replace('×', '')
        cells = html.split('<td>')
        pets_element = ''
        for k in range(1, len(cells)):
            pets_element += cells[k].replace('</td>', '').split('<td ')[0].strip()
        pets_elements.append(pets_element)

    # with capsys.disabled():
    #     print(f"user profile is {pets_elements}")

    count = 0
    for i in range(len(pets_elements)):
        if pets_elements.count(pets_elements[i]) > 1:
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







