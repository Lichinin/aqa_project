import allure
import pytest


@allure.epic('FCK project')
@allure.suite('UI tests')
@allure.feature('Страница работы с обращениями')
@allure.title('Проверка открытия страницы "Администрирование"')
@pytest.mark.ui_test
def test_button_administration(login_as_admin_appeals):
    page = login_as_admin_appeals
    page.click_button_user()
    page.click_button_admin_link()
    page.assert_administration_page_title()


@allure.epic('FCK project')
@allure.suite('UI tests')
@allure.feature('Страница работы с обращениями')
@allure.title('Проверка открытия формы "Настройки конфигурации"')
@pytest.mark.ui_test
def test_button_config_settings(login_as_admin_appeals):
    page = login_as_admin_appeals
    page.click_button_user()
    page.click_button_admin_link()
    page.click_button_config_settings()
    page.assert_config_settings_title()


@allure.epic('FCK project')
@allure.suite('UI tests')
@allure.feature('Страница работы с обращениями')
@allure.title('Проверка открытия формы просмотра логов')
@pytest.mark.ui_test
def test_button_log_view(login_as_admin_appeals):
    page = login_as_admin_appeals
    page.click_button_user()
    page.click_button_admin_link()
    page.click_button_config_settings()
    page.click_button_log_view()
    page.switch_to_new_window()
    page.assert_log_view()


@allure.epic('FCK project')
@allure.suite('UI tests')
@allure.feature('Страница работы с обращениями')
@allure.title('Проверка установки контрольной точки для просмотра логов')
@pytest.mark.ui_test
def test_button_control_point(login_as_admin_appeals):
    page = login_as_admin_appeals
    page.click_button_user()
    page.click_button_admin_link()
    page.click_button_config_settings()
    page.click_button_log_view()
    page.switch_to_new_window()
    page.click_button_control_point()
    page.assert_add_control_point()


@allure.epic('FCK project')
@allure.suite('UI tests')
@allure.feature('Страница работы с обращениями')
@allure.title('Проверка раскрывающегося списка при нажатии на кнопу "Все"')
@pytest.mark.ui_test
def test_header_button_all(login_as_admin_appeals):
    page = login_as_admin_appeals
    page.click_button_all()
    page.assert_button_all_values()


@allure.epic('FCK project')
@allure.suite('UI tests')
@allure.feature('Страница работы с обращениями')
@allure.title('Проверка открытия модуля "Обращения"')
@pytest.mark.ui_test
def test_button_appeals(login_as_admin_appeals):
    page = login_as_admin_appeals
    page.click_button_all()
    page.click_button_appeals()
    page.assert_appeals_page_title()


@allure.epic('FCK project')
@allure.suite('UI tests')
@allure.feature('Страница работы с обращениями')
@allure.title('Проверка кнопки "Создать обращение"')
@pytest.mark.ui_test
def test_button_create_new_appeal(login_as_admin_appeals):
    page = login_as_admin_appeals
    page.click_button_all()
    page.click_button_appeals()
    page.click_button_create_new_appeal()
    page.assert_create_page_title()


@allure.epic('FCK project')
@allure.suite('UI tests')
@allure.feature('Страница работы с обращениями')
@allure.title('Проверка кнопки поиска контактов')
@pytest.mark.ui_test
def test_button_select_contact(login_as_admin_appeals):
    page = login_as_admin_appeals
    page.click_button_all()
    page.click_button_appeals()
    page.click_button_create_new_appeal()
    page.click_button_select_contact()
    page.switch_to_new_window()
    page.assert_select_contact_window_text()


@allure.epic('FCK project')
@allure.suite('UI tests')
@allure.feature('Страница работы с обращениями')
@allure.title('Проверка заполнения ФИО контакта')
@pytest.mark.ui_test
def test_fill_fio_field(login_as_admin_appeals):
    page = login_as_admin_appeals
    page.click_button_all()
    page.click_button_appeals()
    page.click_button_create_new_appeal()
    page.click_button_select_contact()
    page.switch_to_new_window()
    page.fill_fio_field()
    page.fill_email_field()
    page.assert_fio_field()


@allure.epic('FCK project')
@allure.suite('UI tests')
@allure.feature('Страница работы с обращениями')
@allure.title('Проверка поиска контакта')
@pytest.mark.ui_test
def test_button_find_contact(login_as_admin_appeals, setup_user_db):
    page = login_as_admin_appeals
    page.click_button_all()
    page.click_button_appeals()
    page.click_button_create_new_appeal()
    page.click_button_select_contact()
    page.switch_to_new_window()
    page.fill_fio_field()
    page.fill_email_field(email='')
    page.click_button_find()
    page.assert_search_results()


@allure.epic('FCK project')
@allure.suite('UI tests')
@allure.feature('Страница работы с обращениями')
@allure.title('Проверка проверка выбора найденного контакта')
@pytest.mark.ui_test
def test_click_on_finded_contact(setup_user, login_as_admin_appeals):
    page = login_as_admin_appeals
    page.click_button_all()
    page.click_button_appeals()
    page.click_button_create_new_appeal()
    page.click_button_select_contact()
    page.switch_to_new_window()
    page.fill_fio_field()
    page.fill_email_field()
    page.click_button_find()
    page.click_on_finded_contact()
    page.switch_to_new_window()
    page.assert_click_on_finded_contact()


@allure.epic('FCK project')
@allure.suite('UI tests')
@allure.feature('Страница работы с обращениями')
@allure.title('Проверка выбора категории обращения')
@pytest.mark.ui_test
def test_select_appeal_category_fck(login_as_admin_appeals):
    page = login_as_admin_appeals
    page.click_button_all()
    page.click_button_appeals()
    page.click_button_create_new_appeal()
    page.click_button_appeal_category()
    page.click_on_fck_employee()
    page.assert_select_appeal_category_fck()


@allure.epic('FCK project')
@allure.suite('UI tests')
@allure.feature('Страница работы с обращениями')
@allure.title('Проверка выбора подтипа обращения')
@pytest.mark.ui_test
def test_select_appeal_subtype_consult(login_as_admin_appeals):
    page = login_as_admin_appeals
    page.click_button_all()
    page.click_button_appeals()
    page.click_button_create_new_appeal()
    page.click_subtype()
    page.click_subtype_consult()
    page.assert_select_appeal_subtype_consult()


@allure.epic('FCK project')
@allure.suite('UI tests')
@allure.feature('Страница работы с обращениями')
@allure.title('Проверка выбора темы обращения')
@pytest.mark.ui_test
def test_select_appeal_theme_consult_tech(login_as_admin_appeals):
    page = login_as_admin_appeals
    page.click_button_all()
    page.click_button_appeals()
    page.click_button_create_new_appeal()
    page.click_theme()
    page.click_theme_consult_fck()
    page.assert_select_appeal_theme_consult_tech()


@allure.epic('FCK project')
@allure.suite('UI tests')
@allure.feature('Страница работы с обращениями')
@allure.title('Проверка выбора подтемы обращения')
@pytest.mark.ui_test
def test_select_appeal_subtheme_consult_fck_other(
    login_as_admin_appeals
):
    page = login_as_admin_appeals
    page.click_button_all()
    page.click_button_appeals()
    page.click_button_create_new_appeal()
    page.click_theme()
    page.click_theme_consult_fck()
    page.click_subtheme()
    page.click_subtheme_consult_fck_other()
    page.assert_select_appeal_subtheme_consult_fck_other()


@allure.epic('FCK project')
@allure.suite('UI tests')
@allure.feature('Страница работы с обращениями')
@allure.title('Проверка заполнения описания обращения')
@pytest.mark.ui_test
def test_fill_appeal_description(login_as_admin_appeals):
    page = login_as_admin_appeals
    page.click_button_all()
    page.click_button_appeals()
    page.click_button_create_new_appeal()
    page.fill_appeal_description()
    page.assert_fill_appeal_description()


@allure.epic('FCK project')
@allure.suite('UI tests')
@allure.feature('Страница работы с обращениями')
@allure.title('Проверка работы раскрывающегося списка "Желаемый способ связи"')
@pytest.mark.ui_test
def test_click_connect_type(login_as_admin_appeals):
    page = login_as_admin_appeals
    page.click_button_all()
    page.click_button_appeals()
    page.click_button_create_new_appeal()
    page.click_connect_type()
    page.assert_click_connect_type()


@allure.epic('FCK project')
@allure.suite('UI tests')
@allure.feature('Страница работы с обращениями')
@allure.title('Проверка выбора типа связи "email"')
@pytest.mark.ui_test
def test_click_connect_type_email(login_as_admin_appeals):
    page = login_as_admin_appeals
    page.click_button_all()
    page.click_button_appeals()
    page.click_button_create_new_appeal()
    page.click_connect_type()
    page.click_connect_type_email()
    page.assert_click_connect_type_email()


@allure.epic('FCK project')
@allure.suite('UI tests')
@allure.feature('Страница работы с обращениями')
@allure.title(
    'Проверка выбора контакта для связи "телефон" для анонимного обращения'
)
@pytest.mark.ui_test
def test_click_connect_type_anonymus_phone(login_as_admin_appeals):
    page = login_as_admin_appeals
    page.click_button_all()
    page.click_button_appeals()
    page.click_button_create_new_appeal()
    page.wait_for_loading_page()
    page.click_checkbox_anonymus()
    page.click_connect_type_anonymus()
    page.click_connect_type_anonymus_phone()
    page.assert_click_connect_type_anonymus_phone()


@allure.epic('FCK project')
@allure.suite('UI tests')
@allure.feature('Страница работы с обращениями')
@allure.title('Проверка выбора email пользователя для связи')
@pytest.mark.ui_test
def test_select_user_email(setup_user, login_as_admin_appeals):
    page = login_as_admin_appeals
    page.click_button_all()
    page.click_button_appeals()
    page.click_button_create_new_appeal()
    page.click_button_select_contact()
    page.switch_to_new_window()
    page.fill_fio_field()
    page.fill_email_field()
    page.click_button_find()
    page.click_on_finded_contact()
    page.switch_to_new_window()
    page.click_connect_type()
    page.click_connect_type_email()
    page.click_email_values()
    page.click_user_email()
    page.accert_select_user_email()


@allure.epic('FCK project')
@allure.suite('UI tests')
@allure.feature('Страница работы с обращениями')
@allure.title('Проверка заполнения поля "Телефон" для анонимного обращения')
@pytest.mark.ui_test
def test_fill_anonymus_phone(login_as_admin_appeals):
    page = login_as_admin_appeals
    page.click_button_all()
    page.click_button_appeals()
    page.click_button_create_new_appeal()
    page.wait_for_loading_page()
    page.click_checkbox_anonymus()
    page.click_connect_type_anonymus()
    page.click_connect_type_anonymus_phone()
    page.fill_anonymus_phone()
    page.assert_fill_anonymus_phone()


@allure.epic('FCK project')
@allure.suite('UI tests')
@allure.feature('Страница работы с обращениями')
@allure.title('Проверка лога работы системы')
@pytest.mark.ui_test
def test_open_log_page(login_as_admin_appeals):
    page = login_as_admin_appeals
    page.click_button_user()
    page.click_button_admin_link()
    page.click_button_config_settings()
    page.click_button_log_view()
    page.switch_to_new_window()
    page.accert_log_is_visible()


@allure.epic('FCK project')
@allure.suite('UI tests')
@allure.feature('Страница работы с обращениями')
@allure.title('Проверка нажатия чек-бокса "Анонимно"')
@pytest.mark.ui_test
def test_check_anonymus(login_as_admin_appeals):
    page = login_as_admin_appeals
    page.click_button_all()
    page.click_button_appeals()
    page.click_button_create_new_appeal()
    page.wait_for_loading_page()
    page.click_checkbox_anonymus()
    page.assert_click_checkbox_anonymus()


@allure.epic('FCK project')
@allure.suite('UI tests')
@allure.feature('Страница работы с обращениями')
@allure.title('Проверка кнопки "Сохранить и выйти"')
@pytest.mark.ui_test
def test_save_appeal(
    setup_user,
    login_as_admin_appeals,
    delete_created_appeal
):
    page = login_as_admin_appeals
    page.click_button_all()
    page.click_button_appeals()
    page.click_button_create_new_appeal()
    page.click_button_select_contact()
    page.switch_to_new_window()
    page.fill_fio_field()
    page.fill_email_field()
    page.click_button_find()
    page.click_on_finded_contact()
    page.switch_to_new_window()
    page.click_button_appeal_category()
    page.click_on_fck_employee()
    page.click_subtype()
    page.click_subtype_consult()
    page.click_theme()
    page.click_theme_consult_fck()
    page.click_subtheme()
    page.click_subtheme_consult_fck_other()
    page.fill_appeal_description()
    page.click_connect_type()
    page.click_connect_type_email()
    page.click_email_values()
    page.click_user_email()
    page.click_button_save_appeal()
    page.accert_save_appeal()


@allure.epic('FCK project')
@allure.suite('UI tests')
@allure.feature('Страница работы с обращениями')
@allure.story('TestCase #3. Создание обращения от ФЛ без ЛК')
@allure.title('Создание обращения от ФЛ без ЛК')
@pytest.mark.ui_test
def test_create_appeal_by_admin_as_fl(
    setup_user,
    login_as_admin_appeals,
    delete_created_appeal
):
    page = login_as_admin_appeals
    page.click_button_all()
    page.click_button_appeals()
    page.click_button_create_new_appeal()
    page.click_button_select_contact()
    page.switch_to_new_window()
    page.fill_fio_field()
    page.fill_email_field()
    page.click_button_find()
    page.click_on_finded_contact()
    page.switch_to_new_window()
    page.click_button_appeal_category()
    page.click_on_fck_employee()
    page.click_subtype()
    page.click_subtype_consult()
    page.click_theme()
    page.click_theme_consult_fck()
    page.click_subtheme()
    page.click_subtheme_consult_fck_other()
    page.fill_appeal_description()
    page.click_connect_type()
    page.click_connect_type_email()
    page.click_email_values()
    page.click_user_email()
    page.click_button_save_appeal()
    page.wait_for_loading_page()
    page.click_button_user()
    page.click_button_admin_link()
    page.click_button_config_settings()
    page.click_button_log_view()
    page.switch_to_new_window()
    page.click_button_reload_from_control_poin()
    page.accert_log_message()


@allure.epic('FCK project')
@allure.suite('UI tests')
@allure.feature('Страница работы с обращениями')
@allure.story('TestCase #4. Создание обращения от ФЛ с ЛК')
@allure.title('Создание обращения от ФЛ с ЛК')
@pytest.mark.ui_test
def test_create_appeal_by_fl_with_lk(
    setup_user,
    login_as_admin_appeals,
    delete_created_appeal
):
    page = login_as_admin_appeals
    page.click_button_all()
    page.click_button_appeals()
    page.click_button_create_new_appeal()
    page.click_button_select_contact()
    page.switch_to_new_window()
    page.fill_fio_field()
    page.fill_email_field(email='')
    page.click_button_find()
    page.click_on_finded_contact()
    page.switch_to_new_window()
    page.click_button_appeal_category()
    page.click_on_fck_employee()
    page.click_subtype()
    page.click_subtype_invitation()
    page.click_theme()
    page.click_theme_invitations_events()
    page.click_subtheme()
    page.click_subtheme_invitation_events_other()
    page.fill_appeal_description()
    page.click_connect_type()
    page.click_connect_type_email()
    page.click_email_values()
    page.click_user_email()
    page.click_button_save_appeal()
    page.check_processing_deadline()
    page.check_appeal_weight()
    page.check_appeal_status()
    page.check_appeal_state()


@allure.epic('FCK project')
@allure.suite('UI tests')
@allure.feature('Страница работы с обращениями')
@allure.story('TestCase #5. Создание обращения от анонимного пользователя')
@allure.title('Создание обращения от анонимного пользователя')
@pytest.mark.ui_test
def test_create_appeal_by_anonymus(
    login_as_admin_appeals,
    delete_created_appeal
):
    page = login_as_admin_appeals
    page.click_button_all()
    page.click_button_appeals()
    page.click_button_create_new_appeal()
    page.wait_for_loading_page()
    page.click_checkbox_anonymus()
    page.click_button_appeal_category()
    page.click_on_fck_employee()
    page.click_subtype()
    page.click_subtype_consult()
    page.click_theme()
    page.click_theme_consult_fck()
    page.click_subtheme()
    page.click_subtheme_consult_fck_other()
    page.fill_appeal_description()
    page.click_connect_type_anonymus()
    page.click_connect_type_anonymus_phone()
    page.fill_anonymus_phone()
    page.click_button_save_appeal()
    page.wait_for_loading_page()
    page.assert_create_appeal_by_anonymus()
