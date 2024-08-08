import datetime

import allure
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys

from hw_09.locators.locators import Selectors
from hw_09.pages.ui.base_page import BasePage


class AppealPage(BasePage):

    @allure.step('Нажимается кнопка "Пользователь"')
    def click_button_user(self):
        self.get_element(Selectors.BUTTON_USER).click()

    @allure.step('Нажимается кнопка "Администрирование"')
    def click_button_admin_link(self):
        self.get_element(Selectors.BUTTON_ADMIN_LINK).click()

    @allure.step('Нажимается кнопка "Настройка конфигурации"')
    def click_button_config_settings(self):
        self.get_element(Selectors.BUTTON_CONFIG_SETTINGS).click()

    @allure.step('Нажимается кнопка "Просмотр журнала"')
    def click_button_log_view(self):
        self.get_element(Selectors.BUTTON_LOG_VIEW).click()

    @allure.step('Переключение на новую открытую вкладку')
    def swith_to_new_handle(self):
        all_handles = self.browser.window_handles
        self.browser.switch_to.window(all_handles[1])

    @allure.step('Нажимается кнопка "Установить контрольную точку"')
    def click_button_control_point(self):
        self.get_element(Selectors.BUTTON_CONTROL_POINT).click()

    @allure.step('Нажимается кнопка "Обращения"')
    def click_button_appeals(self):
        self.get_element(Selectors.BUTTON_APPEALS).click()

    @allure.step('Нажимается кнопка "Создать обращение"')
    def click_button_create_new_appeal(self):
        self.get_element(Selectors.BUTTON_CREATE_NEW_ITEM).click()

    @allure.step('Нажимается кнопка выбора контакта')
    def click_button_select_contact(self):
        self.get_element(Selectors.BUTTON_SELECT_CONTACT).click()

    @allure.step('Заполняется поле ФИО')
    def fill_fio_field(self):
        self.fill_the_field(
            Selectors.SELECT_CONTACT_FIELD_FIO,
            Selectors.TEST_USER_SURNAME
        )

    @allure.step('Заполняется поле "Почта"')
    def fill_email_field(self, email=Selectors.TEST_USER_EMAIL):
        self.fill_the_field(
            Selectors.SELECT_CONTACT_FIELD_EMAIL,
            email
        )

    @allure.step('Нажимается кнопка "Найти"')
    def click_button_find(self):
        self.get_element(Selectors.BUTTON_SEARCH).click()

    @allure.step('Клик по контакту')
    def click_on_finded_contact(self):
        self.get_element(Selectors.FINDED_CONTACT).click()

    @allure.step('Нажимается кнопка "Категория обращения"')
    def click_button_appeal_category(self):
        self.get_element(Selectors.APPEAL_CATEGORY).click()

    @allure.step('Клик по "Сотрудник ФЦК"')
    def click_on_fck_employee(self):
        self.get_element(Selectors.FCK_EMPLOYEE).click()

    @allure.step('Нажимается кнопка "Подтип"')
    def click_subtype(self):
        self.get_element(Selectors.APPEAL_SUBTYPE).click()

    @allure.step('Клик по подтипу "Консультация"')
    def click_subtype_consult(self):
        self.get_element(Selectors.APPEAL_SUBTYPE_CONSULT).click()

    @allure.step('Клик по подтипу "Приглашение"')
    def click_subtype_invitation(self):
        self.get_element(Selectors.APPEAL_SUBTYPE_INVITATION).click()

    @allure.step('Нажимается кнопка "Тема"')
    def click_theme(self):
        self.get_element(Selectors.APPEAL_THEME).click()

    @allure.step('Клик по теме "Мероприятия"')
    def click_theme_invitations_events(self):
        self.get_element(Selectors.APPEAL_THEME_INVITATION_EVENTS).click()

    @allure.step('Клик по теме "Консультация"')
    def click_theme_consult_fck(self):
        self.get_element(Selectors.APPEAL_THEME_CONSULT_FCK).click()

    @allure.step('Нажимается кнопка "Подтема"')
    def click_subtheme(self):
        self.get_element(Selectors.APPEAL_SUBTHEME).click()

    @allure.step('Клик по подтеме "Прочее"')
    def click_subtheme_invitation_events_other(self):
        self.get_element(
            Selectors.APPEAL_SUBTHEME_INVITATION_EVENTS_OTHER
        ).click()

    @allure.step('Клик по подтеме "Прочее"')
    def click_subtheme_consult_fck_other(self):
        self.get_element(Selectors.APPEAL_SUBTHEME_CONSULT_FCK_OTHER).click()

    @allure.step('Заполняется описание обращения')
    def fill_appeal_description(self):
        iframe = self.get_element(Selectors.DESCRIPTION_IFRAME)
        self.browser.switch_to.frame(iframe)
        appeal_description_element = self.get_element(
            Selectors.APPEAL_DESCRIPTION
        )

        self.browser.execute_script(
            "arguments[0].innerHTML = 'Текст описания';",
            appeal_description_element
        )
        self.get_element(Selectors.APPEAL_DESCRIPTION).click()
        self.browser.switch_to.default_content()

    @allure.step('Клик по "Желаемый способ связи"')
    def click_connect_type(self):
        self.get_element(Selectors.CONNECT_TYPE).click()

    @allure.step('Клик по "Желаемый способ связи" (аноним)')
    def click_connect_type_anonymus(self):
        self.get_element(Selectors.CONNECT_TYPE_ANONYMUS).click()

    @allure.step('Клик по "Email"')
    def click_connect_type_email(self):
        self.get_element(Selectors.CONNECT_TYPE_EMAIL).click()

    @allure.step('Клик по "Телефон"')
    def click_connect_type_anonymus_phone(self):
        self.get_element(Selectors.CONNECT_TYPE_ANONYMUS_PHONE).click()

    @allure.step('Заполняется номер телефона')
    def fill_anonymus_phone(self):
        self.fill_the_field(
            Selectors.CONNECT_TYPE_ANONYMUS_PHONE_VALUE,
            Selectors.TEST_USER_PHONE
        )

    @allure.step('Клик по "email"')
    def click_email_values(self):
        self.get_element(Selectors.CONTACT_EMAIL_VALUES).click()

    @allure.step('Клик по email пользователя')
    def click_user_email(self):
        self.get_element(Selectors.CONTACT_USER_EMAIL).click()

    @allure.step('Нажимается кнопка "Сохранить обращение"')
    def click_button_save_appeal(self):
        try:
            self.get_element(Selectors.BUTTON_APPEAL_SAVE).click()
            self.appeal_address = self.browser.current_url
        except ElementClickInterceptedException:
            self.browser.execute_script(
                "arguments[0].click();",
                self.get_element(Selectors.BUTTON_APPEAL_SAVE)
            )
            self.appeal_address = self.browser.current_url

    @allure.step('Нажимается кнопка "Обновить с контрольной точки"')
    def click_button_reload_from_control_poin(self):
        self.get_element(Selectors.BUTTON_RELOAD_FROM_CONTROL_POINT).click()

    @allure.step('Поиск сообщения в логе')
    def find_log_message(self):
        self.fill_the_field(Selectors.LOG_FILTER, 'SugarPHPMailer')
        self.get_element(Selectors.LOG_FILTER).send_keys(Keys.ENTER)
        return self.get_element(Selectors.LOG).text

    @allure.step('Клик по чекбоксу "Анонимно"')
    def click_checkbox_anonymus(self):
        self.get_element(Selectors.CHECKBOX_ANONYMUS).click()

    @allure.step('Нажимается кнопка "Подключения"')
    def click_button_connections(self):
        self.get_element(Selectors.BUTTON_CONNECTIONS).click()

    @allure.step('Нажимается кнопка "Настройка URL подключения"')
    def click_button_set_url_connections(self):
        self.get_element(Selectors.BUTTON_SET_URL_CONNECTIONS).click()

    @allure.step('Клик по вкладке "Портал"')
    def click_button_portal(self):
        self.get_element(Selectors.BUTTON_URL_CONNECTIONS_PORTAL).click()

    @allure.step('Получение токена авторизации')
    def get_token(self):
        return self.get_element(Selectors.TOKEN).get_attribute('value')

    @allure.step('Выполняется проверка открытия страницы "Администрирование"')
    def assert_administration_page_title(self):
        self.assert_equals(
            'АДМИНИСТРИРОВАНИЕ',
            self.get_element(Selectors.ADMINISTRATION_PAGE_TITLE).text.strip()
        )

    @allure.step('Выполняется проверка открытия формы "Настройки конфигурации"')
    def assert_config_settings_title(self):
        self.assert_equals(
            'НАСТРОЙКА КОНФИГУРАЦИИ',
            self.get_element(Selectors.ACTUAL_PAGE_TITLE).text.strip()
        )

    @allure.step('Выполняется проверка открытия формы просмотра логов')
    def assert_log_view(self):
        assert self.get_element(Selectors.BUTTON_CONTROL_POINT)

    @allure.step('Выполняется проверка установки контрольной точки для просмотра логов')
    def assert_add_control_point(self):
        self.assert_equals(
            'Контрольная точка в журнале установлена',
            self.get_element(Selectors.CLICK_CONTROL_POINT_MESSAGE).text
        )

    @allure.step('Выполняется проверка открытия модуля "Обращения"')
    def assert_appeals_page_title(self):
        self.assert_equals(
            'ОБРАЩЕНИЯ',
            self.get_element(Selectors.ACTUAL_PAGE_TITLE).text.strip()
        )

    @allure.step('Выполняется проверка кнопки поиска контактов')
    def assert_select_contact_window_text(self):
        self.assert_equals(
            'Поиск контактов',
            self.get_element(Selectors.SELECT_CONTACT_PAGE_TITLE).text.strip()
        )

    @allure.step('Выполняется проверка заполнения ФИО контакта')
    def assert_fio_field(self):
        self.assert_equals(
            Selectors.TEST_USER_SURNAME,
            self.get_element(
                Selectors.SELECT_CONTACT_FIELD_FIO).get_attribute('value')
        )

    @allure.step('Выполняется проверка поиска контакта')
    def assert_search_results(self):
        search_results = self.get_elements(Selectors.SEARCH_CONTACTS_RESULTS)
        self.assert_equals(
            1,
            len(search_results)
        )

    @allure.step('Выполняется проверка выбора найденного контакта')
    def assert_click_on_finded_contact(self):
        exptected_values = set()
        exptected_values.add(
            (f'{Selectors.TEST_USER_SURNAME} {Selectors.TEST_USER_FIRSTNAME} {Selectors.TEST_USER_SECONDNAME}').upper()
        )
        exptected_values.add((Selectors.TEST_USER_COMPANY).upper())
        exptected_values.add((Selectors.TEST_USER_POSITION).lower())

        actual_values = set()
        actual_values.add(
            self.get_element(
                Selectors.FIELD_CONTACT_CREATED_NAME
            ).get_attribute('value')
        )
        actual_values.add(
            self.get_element(
                Selectors.FIELD_CONTACT_CREATED_COMPANY
            ).get_attribute('value')
        )
        actual_values.add(
            self.get_element(
                Selectors.FIELD_CONTACT_CREATED_POSITION
            ).get_attribute('value')
        )
        self.assert_equals(
            exptected_values,
            actual_values
        )

    @allure.step('Выполняется проверка выбора категории обращения')
    def assert_select_appeal_category_fck(self):
        self.assert_equals(
            'fck',
            self.get_element(Selectors.APPEAL_CATEGORY).get_attribute('value')
        )

    @allure.step('Выполняется проверка выбора подтипа обращения')
    def assert_select_appeal_subtype_consult(self):
        self.assert_equals(
            'consult',
            self.get_element(Selectors.APPEAL_SUBTYPE).get_attribute('value')
        )

    @allure.step('Выполняется проверка выбора темы обращения')
    def assert_select_appeal_theme_consult_tech(self):
        self.assert_equals(
            'consult_fck',
            self.get_element(Selectors.APPEAL_THEME).get_attribute('value')
        )

    @allure.step('Выполняется проверка выбора подтемы обращения')
    def assert_select_appeal_subtheme_consult_fck_other(self):
        self.assert_equals(
            'consult_fck_other',
            self.get_element(Selectors.APPEAL_SUBTHEME).get_attribute('value')
        )

    @allure.step('Выполняется проверка заполнения описания обращения')
    def assert_fill_appeal_description(self):
        iframe = self.get_element(Selectors.DESCRIPTION_IFRAME)
        self.browser.switch_to.frame(iframe)
        self.assert_equals(
            'Текст описания',
            self.get_element(Selectors.APPEAL_DESCRIPTION).text
        )

    @allure.step('Выполняется проверка работы раскрывающегося списка "Желаемый способ связи')
    def assert_click_connect_type(self):
        self.assert_equals(
            3,
            len(self.get_elements(Selectors.CONNECT_TYPE_VALUES))
        )

    @allure.step('Выполняется проверка выбора типа связи "email"')
    def assert_click_connect_type_email(self):
        self.assert_equals(
            'email',
            self.get_element(Selectors.CONNECT_TYPE).get_attribute('value')
        )

    @allure.step('Выполняется проверка выбора контакта для связи "телефон" для анонимного обращения')
    def assert_click_connect_type_anonymus_phone(self):
        self.assert_equals(
            'phone',
            self.get_element(
                Selectors.CONNECT_TYPE_ANONYMUS_PHONE
            ).get_attribute('value')
        )

    @allure.step('Выполняется проверка выбора email пользователя для связи')
    def accert_select_user_email(self):
        assert '7373@mail.ru' in self.get_element(
            Selectors.CONTACT_EMAIL_VALUES
        ).get_attribute('value')

    @allure.step('Выполняется проверка кнопки "Сохранить и выйти"')
    def accert_save_appeal(self):
        self.assert_page_title(
            'РАБОТА ФЦК',
            Selectors.ACTUAL_PAGE_TITLE
        )

    @allure.step('Выполняется проверка лога работы системы')
    def accert_log_is_visible(self):
        assert self.get_element(
            Selectors.BUTTON_RELOAD_FROM_CONTROL_POINT
        ).is_displayed()

    @allure.step('Выполняется проверка сообщений лога')
    def accert_log_message(self):
        now = datetime.datetime.now()
        current_hours = now.hour
        current_minutes = now.minute
        time_string = f"{current_hours:02d}:{current_minutes:02d}"
        log_messages = self.find_log_message()
        assert time_string in log_messages

    @allure.step('Выполняется проверка нажатия чек-бокса "Анонимно"')
    def assert_click_checkbox_anonymus(self):
        assert self.get_element(Selectors.CHECKBOX_ANONYMUS).is_selected()

    @allure.step('Выполняется проверка заполнения поля "Телефон" для анонимного обращения')
    def assert_fill_anonymus_phone(self):
        self.assert_equals(
            Selectors.TEST_USER_PHONE,
            self.get_element(
                Selectors.CONNECT_TYPE_ANONYMUS_PHONE_VALUE
            ).get_attribute('value')
        )

    @allure.step('Выполняется проверка значения номера телефона анонимного пользователя')
    def assert_create_appeal_by_anonymus(self):
        self.assert_equals(
            Selectors.TEST_USER_PHONE,
            self.get_element(Selectors.ANONYMUS_APPEAL_PHONE_NUMBER).text
        )

    @allure.step('Выполняется проверка расчетного времени выполнения обращения')
    def check_processing_deadline(self):
        creation_date = datetime.date.today()
        visible_processing_deadline = datetime.datetime.strptime(
            self.get_element(Selectors.VISIBLE_PROCESSING_DEADLINE).text,
            '%d.%m.%Y %H:%M'
        ).date()
        self.browser.execute_script("window.open('');")
        self.browser.switch_to.window(self.browser.window_handles[1])
        self.browser.get(Selectors.FESTIVE_URL)
        festive_dates = list(
            datetime.datetime.strptime(
                date.text, '%d.%m.%Y'
            ).date() for date in self.get_elements(Selectors.FESTIVE_DATE)
        )
        self.browser.get(Selectors.PROCESSING_TIME_URL)
        processing_time = int(self.get_element(Selectors.PROCESSING_TIME).text)
        weekend_days = 0
        for _ in range(processing_time):
            creation_date = creation_date + datetime.timedelta(days=1)
            if (creation_date in festive_dates) or (creation_date.weekday() in [5, 6]):
                weekend_days += 1
        calculated_processing_deadline = creation_date + datetime.timedelta(days=weekend_days)
        self.browser.close()
        self.browser.switch_to.window(self.browser.window_handles[0])
        self.assert_equals(
            calculated_processing_deadline,
            visible_processing_deadline
        )

    @allure.step('Выполняется проверка веса обращения')
    def check_appeal_weight(self):
        visible_appeal_weight = int(
            self.get_element(Selectors.APPEAL_WEIGHT).text
        )
        self.browser.execute_script("window.open('');")
        self.browser.switch_to.window(self.browser.window_handles[1])
        self.browser.get(Selectors.PROCESSING_TIME_URL)
        base_weight = int(self.get_element(Selectors.CASE_WEIGHT).text)
        priority_weight_dict = {'Высокий': 3, 'Средний': 2, 'Низкий': 1}
        priority_weight = priority_weight_dict[self.get_element(
            Selectors.CASE_PRIORRITY
        ).text.strip()]
        calculated_appeal_weight = base_weight + priority_weight
        self.browser.close()
        self.browser.switch_to.window(self.browser.window_handles[0])
        self.assert_equals(
            calculated_appeal_weight,
            visible_appeal_weight
        )

    @allure.step('Выполняется проверка статуса обращения')
    def check_appeal_status(self):
        status_text = self.get_element(Selectors.APPEAL_STATUS).text
        self.assert_equals(
            'Не назначено',
            status_text
        )

    @allure.step('Выполняется проверка состояния обращения')
    def check_appeal_state(self):
        status_text = self.get_element(Selectors.APPEAL_STATE).text
        self.assert_equals(
            'Открыто',
            status_text
        )

    @allure.step('Нажимается кнопка "Действия"')
    def click_button_appeal_actions(self):
        self.get_element(Selectors.BUTTON_APPEAL_ACTIONS).click()

    @allure.step('Нажимается кнопка "Удалить"')
    def click_button_appeal_delete(self):
        self.get_element(Selectors.BUTTON_APPEAL_ACTIONS_DELETE).click()
