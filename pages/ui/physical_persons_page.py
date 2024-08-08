# from faker import Faker
import allure
from selenium.webdriver.common.by import By

from hw_09.locators.locators import Selectors
from hw_09.pages.ui.base_page import BasePage


class PhysicalPersonPage(BasePage):

    @allure.step('Нажимается кнопка "Физические лица"')
    def click_button_physical_persons(self):
        self.get_element(Selectors.BUTTON_PHYSICAL_PERSONS).click()

    @allure.step('Нажимается кнопка "Создать"')
    def click_button_create_physical_persons(self):
        self.get_element(Selectors.BUTTON_CREATE_NEW_ITEM).click()

    @allure.step('Заполняется поле "Фамилия"')
    def fill_surname_field(self):
        self.fill_the_field(
            Selectors.FIELD_SURNAME,
            Selectors.TEST_USER_SURNAME
        )

    @allure.step('Заполняется поле "Имя"')
    def fill_first_name_field(self):
        self.fill_the_field(
            Selectors.FIELD_NAME,
            Selectors.TEST_USER_FIRSTNAME
        )

    @allure.step('Заполняется поле "Отчество"')
    def fill_second_name_field(self):
        self.fill_the_field(
            Selectors.FIELD_SECOND_NAME,
            Selectors.TEST_USER_SECONDNAME
        )

    @allure.step('Клик по категории контакта')
    def click_contact_category_field(self):
        self.get_element(Selectors.FIELD_CONTACT_CATEGORY).click()

    @allure.step('Клик по Должность')
    def click_contact_category_staff_field(self):
        self.get_element(Selectors.FIELD_CONTACT_CATEGORY_EMPLOYEE).click()

    @allure.step('Клик по кнопке со стрелкой')
    def click_enterprise_button(self):
        self.get_element(Selectors.BUTTON_ENTERPRISE).click()

    @allure.step('Заполняется поле "ИНН"')
    def fill_inn_field(self, inn='6321277661'):
        self.fill_the_field(Selectors.FIELD_INN, inn)

    @allure.step('Нажимается кнопка "Поиск"')
    def click_enterprise_search_button(self):
        self.get_element(Selectors.BUTTON_SEARCH).click()

    @allure.step('Получение списка предприятий')
    def get_enterprise_list(self):
        enterprises = self.get_elements(Selectors.ENTERPRISE_LIST)
        return enterprises

    @allure.step('Клик по найденной компании')
    def click_found_company(self):
        self.get_element(Selectors.FOUNDED_COMPANY).click()

    @allure.step('Заполняется поле "Должность"')
    def fill_position_field(self):
        self.fill_the_field(
            Selectors.FIELD_POSITION,
            Selectors.TEST_USER_POSITION
        )

    @allure.step('Заполняется номер телефона')
    def fill_phone_number_field(self):
        self.fill_the_field(
            Selectors.FIELD_PHONE_NUMBER,
            Selectors.TEST_USER_PHONE
        )

    @allure.step('Заполняется поле "email"')
    def fill_email_field(self):
        self.fill_the_field(Selectors.FIELD_EMAIL, Selectors.TEST_USER_EMAIL)

    @allure.step('Нажимается кнопка "Сохранить и выйти"')
    def click_save_and_close_button(self):
        self.get_element(Selectors.BUTTON_SAVE_AND_CLOSE).click()

    @allure.step('Нажимается кнопка "Действия"')
    def click_user_actions_button(self):
        self.get_element(Selectors.BUTTON_USER_ACTIONS).click()

    @allure.step('Нажимается кнопка "Удалить"')
    def click_delete_user_button(self):
        self.get_element(Selectors.BUTTON_DELETE_USER).click()

    @allure.step('Подтвержнается удаление')
    def confirm_user_delete(self):
        alert = self.browser.switch_to.alert
        alert.accept()

    @allure.step('Выполняется проверка нажатия на кнопку "Физические лица"')
    def assert_physical_persons_page_title(self):
        self.assert_equals(
            'ФИЗИЧЕСКИЕ ЛИЦА',
            self.get_element(Selectors.ACTUAL_PAGE_TITLE).text.strip()
        )

    @allure.step('Выполняется проверка нажатия на кнопку "Создать физическое лицо"')
    def assert_create_physical_persons_page_title(self):
        self.wait_for_loading_page()
        self.assert_equals(
            'СОЗДАТЬ',
            self.get_element(Selectors.ACTUAL_PAGE_TITLE).text.strip()
        )

    @allure.step('Выполняется проверка заполнения поля "Фамилия"')
    def assert_surname_field(self):
        self.assert_equals(
            Selectors.TEST_USER_SURNAME,
            self.get_element(Selectors.FIELD_SURNAME).get_attribute('value')
        )

    @allure.step('Выполняется проверка заполнения поля "Имя"')
    def assert_first_name_field(self):
        self.assert_equals(
            Selectors.TEST_USER_FIRSTNAME,
            self.get_element(Selectors.FIELD_NAME).get_attribute('value')
        )

    @allure.step('Выполняется проверка заполнения поля "Отчество')
    def assert_second_name_field(self):
        self.assert_equals(
            Selectors.TEST_USER_SECONDNAME,
            self.get_element(
                Selectors.FIELD_SECOND_NAME
            ).get_attribute('value')
        )

    @allure.step('Выполняется проверка выбра поля "Категория контакта"')
    def assert_contact_category_field(self):
        self.assert_equals(
            Selectors.TEST_USER_CATEGORY,
            self.get_element(Selectors.FIELD_CONTACT_CATEGORY_EMPLOYEE).text
        )

    @allure.step('Выполняется проверка нажатия кнопки выбора предприятия')
    def assert_enterprice_window_text(self):
        self.assert_equals(
            'Поиск предприятий',
            self.get_element(Selectors.ENTERPRISE_PAGE_TITLE).text
        )

    @allure.step('Выполняется проверка заполнения поля "ИНН"')
    def assert_inn_field(self):
        self.assert_equals(
            '6321277661',
            self.get_element(Selectors.FIELD_INN).get_attribute('value')
        )

    @allure.step('Выполняется проверка поиска предприятия по заданному ИНН')
    def assert_enterprise_search_results(self):
        enterprises = self.get_enterprise_list()
        self.assert_equals(1, len(enterprises))

    @allure.step('Выполняется проверка выбра предприятия, найденного по заданному ИНН')
    def assert_select_found_company(self):
        self.assert_equals(
            Selectors.TEST_USER_COMPANY,
            self.get_element(
                Selectors.FIELD_COMPANY_NAME
            ).get_attribute('value')
        )

    @allure.step('Выполняется проверка заполнения поля "Должность"')
    def assert_position_field(self):
        self.assert_equals(
            Selectors.TEST_USER_POSITION,
            self.get_element(Selectors.FIELD_POSITION).get_attribute('value')
        )

    @allure.step('Выполняется проверка заполнения поля "Номер телефона"')
    def assert_phone_field(self):
        self.assert_equals(
            Selectors.TEST_USER_PHONE,
            self.get_element(
                Selectors.FIELD_PHONE_NUMBER
            ).get_attribute('value')
        )

    @allure.step('Выполняется проверка заполнения поля "Email"')
    def assert_email_field(self):
        self.assert_equals(
            Selectors.TEST_USER_EMAIL,
            self.get_element(Selectors.FIELD_EMAIL).get_attribute('value')
        )

    @allure.step('Выполняется проверка нажатия кнопки "Сохранить и выйти" с заполненными данными')
    def assert_created_user_page_text(self):
        self.wait_for_loading_page()
        self.assert_equals(
            'SUАВТО FIТЕСТ SEТЕСТОВИЧ',
            self.get_element(Selectors.ACTUAL_PAGE_TITLE).text
        )

    @allure.step('Выполняется проверка значений полей созданного пользователя')
    def assert_created_user_values(self):
        values = self.get_elements((By.CLASS_NAME, 'detail-view-field'))
        actual_values = {element.text for element in values}
        expected_values = {
            (Selectors.TEST_USER_SURNAME.upper()),
            Selectors.TEST_USER_FIRSTNAME.upper(),
            Selectors.TEST_USER_SECONDNAME.upper(),
            Selectors.TEST_USER_CATEGORY,
            Selectors.TEST_USER_COMPANY,
            f'Рабочий: +7{Selectors.TEST_USER_PHONE} (Основной)',
            f'{Selectors.TEST_USER_EMAIL}\n (Основной )'
        }
        self.assert_subset(expected_values, actual_values)

    @allure.step('Нажимается кнопка "Выйти"')
    def click_logout_button(self):
        self.get_element(Selectors.BUTTON_LOGOUT).click()

    @allure.step('Нажимается кнопка "Пользователь"')
    def click_button_user(self):
        self.get_element(Selectors.BUTTON_USER).click()
