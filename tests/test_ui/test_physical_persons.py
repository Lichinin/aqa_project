import allure
import pytest


@allure.epic('FCK project')
@allure.suite('UI tests')
@allure.feature('Страница работы с физическими лицами')
@allure.title(
    'Проверка значений выпадающего списка по нажанию по кнопке "Все"'
)
@pytest.mark.ui_test
def test_header_button_all(login_as_admin_physical_person):
    page = login_as_admin_physical_person
    page.click_button_all()
    page.assert_button_all_values()


@allure.epic('FCK project')
@allure.suite('UI tests')
@allure.feature('Страница работы с физическими лицами')
@allure.title('Проверка нажатия на кнопку "Физические лица"')
@pytest.mark.ui_test
def test_button_physical_persons(login_as_admin_physical_person):
    page = login_as_admin_physical_person
    page.click_button_all()
    page.click_button_physical_persons()
    page.assert_physical_persons_page_title()


@allure.epic('FCK project')
@allure.suite('UI tests')
@allure.feature('Страница работы с физическими лицами')
@allure.title('Проверка нажатия на кнопку "Создать физическое лицо"')
@pytest.mark.ui_test
def test_button_create_physical_persons(login_as_admin_physical_person):
    page = login_as_admin_physical_person
    page.click_button_all()
    page.click_button_physical_persons()
    page.click_button_create_physical_persons()
    page.assert_create_physical_persons_page_title()


@allure.epic('FCK project')
@allure.suite('UI tests')
@allure.feature('Страница работы с физическими лицами')
@allure.title('Проверка заполнения поля "Фамилия"')
@pytest.mark.ui_test
def test_surname_field(login_as_admin_physical_person):
    page = login_as_admin_physical_person
    page.click_button_all()
    page.click_button_physical_persons()
    page.click_button_create_physical_persons()
    page.fill_surname_field()
    page.assert_surname_field()


@allure.epic('FCK project')
@allure.suite('UI tests')
@allure.feature('Страница работы с физическими лицами')
@allure.title('Проверка заполнения поля "Имя"')
@pytest.mark.ui_test
def test_first_name_field(login_as_admin_physical_person):
    page = login_as_admin_physical_person
    page.click_button_all()
    page.click_button_physical_persons()
    page.click_button_create_physical_persons()
    page.fill_first_name_field()
    page.assert_first_name_field()


@allure.epic('FCK project')
@allure.suite('UI tests')
@allure.feature('Страница работы с физическими лицами')
@allure.title('Проверка заполнения поля "Отчество"')
@pytest.mark.ui_test
def test_second_name_field(login_as_admin_physical_person):
    page = login_as_admin_physical_person
    page.click_button_all()
    page.click_button_physical_persons()
    page.click_button_create_physical_persons()
    page.fill_second_name_field()
    page.assert_second_name_field()


@allure.epic('FCK project')
@allure.suite('UI tests')
@allure.feature('Страница работы с физическими лицами')
@allure.title('Проверка выбра поля "Категория контакта"')
@pytest.mark.ui_test
def test_contact_category_field(login_as_admin_physical_person):
    page = login_as_admin_physical_person
    page.click_button_all()
    page.click_button_physical_persons()
    page.click_button_create_physical_persons()
    page.click_contact_category_field()
    page.click_contact_category_staff_field()
    page.assert_contact_category_field()


@allure.epic('FCK project')
@allure.suite('UI tests')
@allure.feature('Страница работы с физическими лицами')
@allure.title('Проверка нажатия кнопки выбора предприятия')
@pytest.mark.ui_test
def test_enterpsrise_button(login_as_admin_physical_person):
    page = login_as_admin_physical_person
    page.click_button_all()
    page.click_button_physical_persons()
    page.click_button_create_physical_persons()
    page.click_enterprise_button()
    page.switch_to_new_window()
    page.assert_enterprice_window_text()


@allure.epic('FCK project')
@allure.suite('UI tests')
@allure.feature('Страница работы с физическими лицами')
@allure.title('Проверка заполнения поля "ИНН"')
@pytest.mark.ui_test
def test_inn_field(login_as_admin_physical_person):
    page = login_as_admin_physical_person
    page.click_button_all()
    page.click_button_physical_persons()
    page.click_button_create_physical_persons()
    page.click_enterprise_button()
    page.switch_to_new_window()
    page.fill_inn_field()
    page.assert_inn_field()


@allure.epic('FCK project')
@allure.suite('UI tests')
@allure.feature('Страница работы с физическими лицами')
@allure.title('Проверка поиска предприятия по заданному ИНН')
@pytest.mark.ui_test
def test_search_enterprise_by_inn(login_as_admin_physical_person):
    page = login_as_admin_physical_person
    page.click_button_all()
    page.click_button_all()
    page.click_button_physical_persons()
    page.click_button_create_physical_persons()
    page.click_enterprise_button()
    page.switch_to_new_window()
    page.fill_inn_field()
    page.click_enterprise_search_button()
    page.assert_enterprise_search_results()


@allure.epic('FCK project')
@allure.suite('UI tests')
@allure.feature('Страница работы с физическими лицами')
@allure.title('Проверка выбра предприятия, найденного по заданному ИНН')
@pytest.mark.ui_test
def test_select_found_company(login_as_admin_physical_person):
    page = login_as_admin_physical_person
    page.click_button_all()
    page.click_button_physical_persons()
    page.click_button_create_physical_persons()
    page.click_enterprise_button()
    page.switch_to_new_window()
    page.fill_inn_field()
    page.click_enterprise_search_button()
    page.click_found_company()
    page.switch_to_main_window()
    page.assert_select_found_company()


@allure.epic('FCK project')
@allure.suite('UI tests')
@allure.feature('Страница работы с физическими лицами')
@allure.title('Проверка заполнения поля "Должность"')
@pytest.mark.ui_test
def test_position_field(login_as_admin_physical_person):
    page = login_as_admin_physical_person
    page.click_button_all()
    page.click_button_physical_persons()
    page.click_button_create_physical_persons()
    page.fill_position_field()
    page.assert_position_field()


@allure.epic('FCK project')
@allure.suite('UI tests')
@allure.feature('Страница работы с физическими лицами')
@allure.title('Проверка заполнения поля "Номер телефона"')
@pytest.mark.ui_test
def test_phone_number_field(login_as_admin_physical_person):
    page = login_as_admin_physical_person
    page.click_button_all()
    page.click_button_physical_persons()
    page.click_button_create_physical_persons()
    page.fill_phone_number_field()
    page.assert_phone_field()


@allure.epic('FCK project')
@allure.suite('UI tests')
@allure.feature('Страница работы с физическими лицами')
@allure.title('Проверка заполнения поля "Email"')
@pytest.mark.ui_test
def test_email_field(login_as_admin_physical_person):
    page = login_as_admin_physical_person
    page.click_button_all()
    page.click_button_physical_persons()
    page.click_button_create_physical_persons()
    page.fill_email_field()
    page.assert_email_field()


@allure.epic('FCK project')
@allure.suite('UI tests')
@allure.feature('Страница работы с физическими лицами')
@allure.title("""
              Проверка нажатия кнопки "Сохранить и выйти"
              с заполненными данными
            """)
@pytest.mark.ui_test
def test_save_and_close_button(login_as_admin_physical_person,
                               delete_created_user
                               ):
    page = login_as_admin_physical_person
    page.click_button_all()
    page.click_button_physical_persons()
    page.click_button_create_physical_persons()
    page.fill_surname_field()
    page.fill_first_name_field()
    page.fill_second_name_field()
    page.click_contact_category_field()
    page.click_contact_category_staff_field()
    page.click_enterprise_button()
    page.switch_to_new_window()
    page.fill_inn_field()
    page.click_enterprise_search_button()
    page.click_found_company()
    page.switch_to_main_window()
    page.fill_position_field()
    page.fill_phone_number_field()
    page.fill_email_field()
    page.click_save_and_close_button()
    page.assert_created_user_page_text()


@allure.epic('FCK project')
@allure.suite('UI tests')
@allure.feature('Страница работы с физическими лицами')
@allure.story('TestCase #1. Создание физического лица')
@allure.title('Создание физического лица')
@pytest.mark.ui_test
def test_create_physical_person(login_as_admin_physical_person,
                                delete_created_user
                                ):
    page = login_as_admin_physical_person
    page.click_button_all()
    page.click_button_physical_persons()
    page.click_button_create_physical_persons()
    page.fill_surname_field()
    page.fill_first_name_field()
    page.fill_second_name_field()
    page.click_contact_category_field()
    page.click_contact_category_staff_field()
    page.click_enterprise_button()
    page.switch_to_new_window()
    page.fill_inn_field()
    page.click_enterprise_search_button()
    page.click_found_company()
    page.switch_to_main_window()
    page.fill_position_field()
    page.fill_phone_number_field()
    page.fill_email_field()
    page.click_save_and_close_button()
    page.assert_created_user_values()
