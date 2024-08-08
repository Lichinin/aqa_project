import allure
import pytest


@allure.epic('FCK project')
@allure.suite('UI tests')
@allure.feature('Страница работы с юридическими лицами')
@allure.title(
    'Проверка значений выпадающего списка по нажанию по кнопке "Все"'
)
@pytest.mark.ui_test
def test_header_button_all(login_as_admin_companies):
    page = login_as_admin_companies
    page.click_button_all()
    page.assert_button_all_values()


@allure.epic('FCK project')
@allure.suite('UI tests')
@allure.feature('Страница работы с юридическими лицами')
@allure.title("""
              Проверка открытия модуля 'Предприятия'
              по нажатия на кнопку 'Предприятия'
            """)
@pytest.mark.ui_test
def test_button_companies(login_as_admin_companies):
    page = login_as_admin_companies
    page.click_button_all()
    page.click_button_companies()
    page.assert_companies_title()


@allure.epic('FCK project')
@allure.suite('UI tests')
@allure.feature('Страница работы с юридическими лицами')
@allure.title("""
              Проверка открытия формы создания предприятия
              по нажатия на кнопку 'Создать предприятие'
            """)
@pytest.mark.ui_test
def test_button_create_company(login_as_admin_companies):
    page = login_as_admin_companies
    page.click_button_all()
    page.click_button_companies()
    page.click_button_create_company()
    page.assert_create_page_title()


@allure.epic('FCK project')
@allure.suite('UI tests')
@allure.feature('Страница работы с юридическими лицами')
@allure.title('Проверка заполнения поля ИНН корректным значением')
@pytest.mark.ui_test
def test_inn_field(login_as_admin_companies):
    page = login_as_admin_companies
    page.click_button_all()
    page.click_button_companies()
    page.click_button_create_company()
    page.fill_inn_field()
    page.assert_inn_field()


@pytest.mark.skip(reason='Не готов. Не работает на ветке /auto/')
@allure.epic('FCK project')
@allure.suite('UI tests')
@allure.feature('Страница работы с юридическими лицами')
@allure.title('Проверка получения данных с внешнего портала')
@pytest.mark.ui_test
def test_get_data_from_vp(login_as_admin_companies):
    page = login_as_admin_companies
    page.click_button_all()
    page.click_button_companies()
    page.click_button_create_company()
    page.fill_inn_field()
    page.click_button_get_data_vp()
    # page.assert_


@allure.epic('FCK project')
@allure.suite('UI tests')
@allure.feature('Страница работы с юридическими лицами')
@allure.title('Проверка заполнения поля "Номер телефона" корректным значением')
@pytest.mark.ui_test
def test_phone_field(login_as_admin_companies):
    page = login_as_admin_companies
    page.click_button_all()
    page.click_button_companies()
    page.click_button_create_company()
    page.fill_phone_number_field()
    page.assert_phone_field()
