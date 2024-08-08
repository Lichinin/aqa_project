import allure

from hw_09.locators.locators import Selectors
from hw_09.pages.ui.base_page import BasePage


class CompaniesPage(BasePage):

    @allure.step('Нажимается кнопка "Предприятия"')
    def click_button_companies(self):
        self.get_element(Selectors.BUTTON_COMPANIES).click()

    @allure.step('Нажимается кнопка "Создать"')
    def click_button_create_company(self):
        self.get_element(Selectors.BUTTON_CREATE_NEW_ITEM).click()

    @allure.step('Заполняется поле "ИНН"')
    def fill_inn_field(self, inn='0106008761'):
        self.fill_the_field(Selectors.COMPANY_FIELD_INN, inn)

    @allure.step('Нажимается кнопка "Получить данные с ВП"')
    def click_button_get_data_vp(self):
        self.fill_the_field(Selectors.GET_DATA_VP).click()

    @allure.step('Заполняется номер телефона')
    def fill_phone_number_field(self):
        self.fill_the_field(
            Selectors.FIELD_COMPANY_PHONE_NUMBER,
            Selectors.TEST_USER_PHONE
        )

    @allure.step('Выполняется проверка открытия модуля "Предприятия" по нажатия на кнопку "Предприятия"')
    def assert_companies_title(self):
        self.assert_equals(
            'ПРЕДПРИЯТИЯ',
            self.get_element(Selectors.ADMINISTRATION_PAGE_TITLE).text.strip()
        )

    @allure.step('Выполняется проверка заполнения поля ИНН корректным значением')
    def assert_inn_field(self):
        self.assert_equals(
            '0106008761',
            self.get_element(
                Selectors.COMPANY_FIELD_INN
            ).get_attribute('value')
        )

    @allure.step('Выполняется проверка заполнения поля "Номер телефона" корректным значением')
    def assert_phone_field(self):
        self.assert_equals(
            Selectors.TEST_USER_PHONE,
            self.get_element(
                Selectors.FIELD_COMPANY_PHONE_NUMBER
            ).get_attribute('value')
        )
