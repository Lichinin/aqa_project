from selenium.webdriver.common.by import By


class Selectors:

    ADMIN_LOGIN = 'paste_login'
    ADMIN_PASSWORD = 'paste_password'
    HEADER_BUTTON_ALL_CORRECT_VALUES = {"Домашняя страница", "Производственный календарь", "Предприятия", "Физические лица", "Проекты", "Администрирование обращений", "Справочники", "Заявки", "Логирование интеграционных сервисов", "Личные кабинеты на ВП", "Статистика предприятия", "Предложения", "Документы", "Отчеты", "E-mail", "Сводки", "Звонки", "Встречи", "Задачи", "Заметки", "Счета", "Договоры", "Обращения", "База знаний", "Шаблоны E-mail"}

    TEST_USER_SURNAME = 'SUАвто'
    TEST_USER_FIRSTNAME = 'FIТест'
    TEST_USER_SECONDNAME = 'SEТестович'
    TEST_USER_POSITION = 'Менеджер'
    TEST_USER_CATEGORY = 'Сотрудник предприятия'
    TEST_USER_COMPANY = 'ООО "СЕНТЯБРИНКА"'
    TEST_USER_PHONE = '7373737373'
    TEST_USER_EMAIL = '7373@mail.ru'

    USERNAME_FIELD_SELECTOR = (By.ID, 'user_name')
    PASSWORD_FIELD_SELECTOR = (By.ID, 'username_password')
    LOGIN_BUTTON_SELECTOR = (By.ID, 'bigbutton')

    HEADER_BUTTON_ALL = (By.ID, 'grouptab_1')
    HEADER_BUTTON_ALL_VALUES = (
        By.CSS_SELECTOR,
        'li.topnav.all > span.notCurrentTab > .dropdown-menu > li'
    )

    BUTTON_PHYSICAL_PERSONS = (
        By.CSS_SELECTOR,
        'li.topnav.all > span.notCurrentTab > .dropdown-menu > li:nth-of-type(4)'
    )
    ACTUAL_PAGE_TITLE = (By.CLASS_NAME, 'module-title-text')

    BUTTON_CREATE_NEW_ITEM = (
        By.CLASS_NAME,
        'suitepicon-action-create'
    )
    FIELD_SURNAME = (By.ID, 'last_name')
    FIELD_NAME = (By.ID, 'first_name')
    FIELD_SECOND_NAME = (By.ID, 'second_name')
    FIELD_CONTACT_CATEGORY = (By.ID, 'contact_category')
    FIELD_CONTACT_CATEGORY_EMPLOYEE = (
        By.CSS_SELECTOR,
        '#contact_category > option:nth-of-type(2)'
    )
    BUTTON_ENTERPRISE = (By.ID, 'btn_account_name')
    ENTERPRISE_PAGE_TITLE = (By.XPATH, '//span[.="Поиск предприятий"]')
    FIELD_INN = (By.ID, 'inn_advanced')
    BUTTON_SEARCH = (By.ID, 'search_form_submit')
    ENTERPRISE_LIST = (By.CSS_SELECTOR, '.list > tbody > tr')
    FOUNDED_COMPANY = (By.CSS_SELECTOR, 'a[href="javascript:void(0)"]')
    FIELD_COMPANY_NAME = (By.NAME, 'account_name')
    FIELD_POSITION = (By.ID, 'position')
    FIELD_PHONE_NUMBER = (By.NAME, 'phone_numberContacts0')
    FIELD_EMAIL = (By.ID, 'Contacts0emailAddress0')
    BUTTON_SAVE_AND_CLOSE = (By.ID, 'SAVE')
    BUTTON_USER_ACTIONS = (By.ID, 'tab-actions')
    BUTTON_DELETE_USER = (By.ID, 'delete_button')

############
    BUTTON_COMPANIES = (By.CSS_SELECTOR, 'li.topnav.all > span.notCurrentTab > .dropdown-menu > li:nth-of-type(3)')
    COMPANY_FIELD_INN = (By.ID, 'inn')
    GET_DATA_VP = (By.ID, 'get_data_vp')
    FIELD_COMPANY_PHONE_NUMBER = (By.NAME, 'phone_numberAccounts0')

##########
    BUTTON_USER = (By.ID, 'with-label')
    BUTTON_ADMIN_LINK = (By.CSS_SELECTOR, '.desktop-bar ul > li#globalLinks > ul > li:nth-of-type(3)')
    ADMINISTRATION_PAGE_TITLE = (By.CLASS_NAME, 'moduleTitle')
    BUTTON_CONFIG_SETTINGS = (By.ID, 'configphp_settings')
    BUTTON_LOG_VIEW = (By.LINK_TEXT, 'Просмотр журнала')
    BUTTON_CONTROL_POINT = (By.CSS_SELECTOR, 'input[name="mark"]')
    CLICK_CONTROL_POINT_MESSAGE = (By.CSS_SELECTOR, '#pagecontent > h3')
    BUTTON_APPEALS = (By.LINK_TEXT, 'Обращения')
    BUTTON_SELECT_CONTACT = (By.ID, 'btn_contact_created_by_name')
    SELECT_CONTACT_PAGE_TITLE = (By.XPATH, '//span[.="Поиск контактов"]')
    SELECT_CONTACT_FIELD_FIO = (By.ID, 'full_name_advanced')
    SELECT_CONTACT_FIELD_EMAIL = (By.ID, 'email_advanced')
    SEARCH_CONTACTS_RESULTS = (By.CSS_SELECTOR, 'tr.oddListRowS1')
    FINDED_CONTACT = (By.CSS_SELECTOR, 'tr.oddListRowS1 > td > a')
    FIELD_CONTACT_CREATED_NAME = (By.ID, 'contact_created_by_name')
    FIELD_CONTACT_CREATED_COMPANY = (By.ID, 'account_name')
    FIELD_CONTACT_CREATED_POSITION = (By.ID, 'position')
    APPEAL_CATEGORY = (By.ID, 'category')
    FCK_EMPLOYEE = (By.CSS_SELECTOR, 'option[value="fck"]')

    APPEAL_SUBTYPE = (By.ID, 'subtype')
    APPEAL_SUBTYPE_CONSULT = (By.CSS_SELECTOR, 'option[value="consult"]')
    APPEAL_SUBTYPE_INVITATION = (By.CSS_SELECTOR, 'option[value="invitation"]')

    APPEAL_THEME = (By.ID, 'subject')
    APPEAL_THEME_INVITATION_EVENTS = (By.CSS_SELECTOR, 'option[value="invitation_events"]')
    APPEAL_THEME_CONSULT_FCK = (By.CSS_SELECTOR, 'option[value="consult_fck"]')

    APPEAL_SUBTHEME = (By.ID, 'subsubject')
    APPEAL_SUBTHEME_INVITATION_EVENTS_OTHER = (By.CSS_SELECTOR, 'option[value="invitation_events_other"]')
    APPEAL_SUBTHEME_CONSULT_FCK_OTHER = (By.CSS_SELECTOR, 'option[value="consult_fck_other"]')

    APPEAL_DESCRIPTION = (By.CSS_SELECTOR, '#tinymce > p')
    DESCRIPTION_IFRAME = (By.CSS_SELECTOR, '.mceIframeContainer > iframe')

    CONNECT_TYPE = (By.ID, 'connect')
    CONNECT_TYPE_ANONYMUS = (By.ID, 'connect_anon_selection')
    CONNECT_TYPE_ANONYMUS_PHONE = (By.CSS_SELECTOR, '#connect_anon_selection > option[value="phone"]')
    CONNECT_TYPE_ANONYMUS_PHONE_VALUE = (By.ID, 'connect_anon_phone')
    ANONYMUS_APPEAL_PHONE_NUMBER = (By.CSS_SELECTOR, 'div[field="connect_anon_phone"]')

    CONNECT_TYPE_VALUES = (By.CSS_SELECTOR, '#connect > option')
    CONNECT_TYPE_EMAIL = (By.CSS_SELECTOR, '#connect > option[value="email"]')

    CONTACT_EMAIL_VALUES = (By.ID, 'contact_emails')
    CONTACT_USER_EMAIL = (By.CSS_SELECTOR, '#contact_emails > option:nth-of-type(2)')
    BUTTON_APPEAL_SAVE = (By.ID, 'SAVE')
    BUTTON_RELOAD_FROM_CONTROL_POINT = (By.NAME, 'display')
    LOG = (By.CSS_SELECTOR, 'pre')
    LOG_FILTER = (By.NAME, 'filter')
    CHECKBOX_ANONYMUS = (By.ID, 'anon')
    LOADING_MASK = (By.ID, 'ajaxloading_mask')

    PROCESSING_TIME = (By.ID, 'processing_time')
    PROCESSING_TIME_URL = 'paste_url'
    FESTIVE_DATE = (By.CSS_SELECTOR, 'td[field="festive_date"]')
    FESTIVE_URL = 'paste_url'
    VISIBLE_PROCESSING_DEADLINE = (By.ID, 'processing_deadline')

    APPEAL_WEIGHT = (By.ID, 'weight')
    CASE_WEIGHT = (By.ID, 'case_weight')
    CASE_PRIORRITY = (By.CSS_SELECTOR, 'div[field="case_priority"]')
    APPEAL_STATUS = (By.CSS_SELECTOR, 'div[field="status"]')
    APPEAL_STATE = (By.CSS_SELECTOR, 'div[field="state"]')
    BUTTON_APPEAL_ACTIONS = (By.ID, 'tab-actions')
    BUTTON_APPEAL_ACTIONS_DELETE = (By.ID, 'delete_button')

    BUTTON_CONNECTIONS = (By.ID, 'connector_settings')
    BUTTON_SET_URL_CONNECTIONS = (By.CSS_SELECTOR, 'img')
    BUTTON_URL_CONNECTIONS_PORTAL = (By.CSS_SELECTOR, '.yui-nav >li:nth-child(3)')
    TOKEN = (By.ID, 'ext_rest_portal_access_token')

    ENDPOINT_ORGANIZATIONS = '/api/v1/crm/organizations/'
    ENDPOINT_USERS = '/api/v1/crm/users/'
    ENDPOINT_POST = '/auto/custom/service/v4_1/rest.php'
    BUTTON_LOGOUT = (By.CSS_SELECTOR, '.desktop-bar ul > li#globalLinks > ul > li:nth-of-type(6)')
