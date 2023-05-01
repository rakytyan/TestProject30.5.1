# TestProject30.5.1

При выполнении задания 30.3.1 выполнены следующие тесты:

1. test_all_pets_displayed.py - тест, который проверяет, что на странице со списком питомцев пользователя 
присутствуют все питомцы.
2. test_half_pets_have_photo - тест, который проверяет, что хотя бы у половины питомцев есть фото.
3. test_all_pets_have_full_info.py - тест, который проверяет, что у всех питомцев есть имя, возраст и порода.
4. test_all_names_different.py - тест, который проверяет, что у всех питомцев разные имена.
5. test_all_pets_have_full_info.py - тест, который проверяет, что в списке нет повторяющихся питомцев. 

В рамках выполнения задания 30.5.1 был дополнительно написан тест:

test_all_pets_have_full_info_inc_photo.py , который проверяет, что у всех питомцев есть фото,имя, возраст и порода, 
в него добавлено неявное ожидание всех элементов. 
В тест test_all_pets_displayed.py (проверка таблицы питомцев ) добавлены явные ожидания элементов страницы.  

Файл conftest.py содержит две фикстуры:

1. фикстура @pytest.hookimpl отрабатывает отчеты о результатах прохождения тестов.
2. фикстура содержит запуск браузера в selenium, преход на страницу авторизации, а также переход
на страницу "Мои питомцы".
В файле conftest добавлены явные ожидания элементов страницы авторизации и страницы "Все питомцы".

Файл settings.py содержит данные для авторизации.

