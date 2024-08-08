import allure
import pytest

from hw_09.locators.locators import Selectors
from hw_09.pages.api.lead_api import LeadApi
from hw_09.schema.schemas import LeadSchema


@allure.epic('FCK project')
@allure.suite('API tests')
@allure.feature('Запросы к таблице пользователей ВП')
@allure.title('Проверка status-кода запроса')
@pytest.mark.api_test
def test_status_code(session_id):
    lead_api = LeadApi()
    lead_api.create_post_body(session_id)
    lead_api.check_post_status_code(
        endpoint=Selectors.ENDPOINT_POST,
        schema=LeadSchema,
        params=lead_api.payload
    )


@allure.epic('FCK project')
@allure.suite('API tests')
@allure.feature('Запросы к таблице пользователей ВП')
@allure.title('Проверка поля "last_name" созданного лида')
@pytest.mark.api_test
def test_post_created_lead_last_name(session_id):
    lead_api = LeadApi()
    lead_api.create_post_body(session_id)
    lead_api.post_new_lead(lead_api.payload)
    lead_api.check_created_lead_last_name()


@allure.epic('FCK project')
@allure.suite('API tests')
@allure.feature('Запросы к таблице пользователей ВП')
@allure.title('Проверка поля "second_name" созданного лида')
@pytest.mark.api_test
def test_post_created_lead_second_name(session_id):
    lead_api = LeadApi()
    lead_api.create_post_body(session_id)
    lead_api.post_new_lead(lead_api.payload)
    lead_api.check_created_lead_second_name()


@allure.epic('FCK project')
@allure.suite('API tests')
@allure.feature('Запросы к таблице пользователей ВП')
@allure.title('Проверка поля "vp_date_modified" созданного лида')
@pytest.mark.api_test
def test_post_created_lead_vp_date_modified(session_id):
    lead_api = LeadApi()
    lead_api.create_post_body(session_id)
    lead_api.post_new_lead(lead_api.payload)
    lead_api.check_created_lead_vp_date_modified()


@allure.epic('FCK project')
@allure.suite('API tests')
@allure.feature('Запросы к таблице пользователей ВП')
@allure.title('Проверка поля "phone_mobile" созданного лида')
@pytest.mark.api_test
def test_post_created_lead_phone_mobile(session_id):
    lead_api = LeadApi()
    lead_api.create_post_body(session_id)
    lead_api.post_new_lead(lead_api.payload)
    lead_api.check_created_lead_phone_mobile()


@allure.epic('FCK project')
@allure.suite('API tests')
@allure.feature('Запросы к таблице пользователей ВП')
@allure.title('Проверка поля "email" созданного лида')
@pytest.mark.api_test
def test_post_created_lead_email(session_id):
    lead_api = LeadApi()
    lead_api.create_post_body(session_id)
    lead_api.post_new_lead(lead_api.payload)
    lead_api.check_created_lead_email()


@allure.epic('FCK project')
@allure.suite('API tests')
@allure.feature('Запросы к таблице пользователей ВП')
@allure.title('Проверка поля "acc_portal_inn" созданного лида')
@pytest.mark.api_test
def test_post_created_lead_acc_portal_inn(session_id):
    lead_api = LeadApi()
    lead_api.create_post_body(session_id)
    lead_api.post_new_lead(lead_api.payload)
    lead_api.check_created_lead_inn()


@allure.epic('FCK project')
@allure.suite('API tests')
@allure.feature('Запросы к таблице пользователей ВП')
@allure.title('Сравнение значения поля "inn" лида в ВП и в БД')
@pytest.mark.api_test
def test_comparse_inn_from_vp_and_db(session_id):
    lead_api = LeadApi()
    lead_api.create_post_body(session_id)
    lead_api.post_new_lead(lead_api.payload)
    lead_api.check_comparse_inn_from_vp_and_db()


@allure.epic('FCK project')
@allure.suite('API tests')
@allure.feature('Запросы к таблице пользователей ВП')
@allure.title('Сравнение значения поля "last_name" лида в ВП и в БД')
@pytest.mark.api_test
def test_comparse_last_name_from_vp_and_db(session_id):
    lead_api = LeadApi()
    lead_api.create_post_body(session_id)
    lead_api.post_new_lead(lead_api.payload)
    lead_api.check_comparse_last_name_from_vp_and_db()


@allure.epic('FCK project')
@allure.suite('API tests')
@allure.feature('Запросы к таблице пользователей ВП')
@allure.title('Сравнение значения поля "vp_date_modified" лида в ВП и в БД')
@pytest.mark.api_test
def test_comparse_vp_date_modified_from_vp_and_db(session_id):
    lead_api = LeadApi()
    lead_api.create_post_body(session_id)
    lead_api.post_new_lead(lead_api.payload)
    lead_api.check_comparse_vp_date_modified_from_vp_and_db()


@allure.epic('FCK project')
@allure.suite('API tests')
@allure.feature('Запросы к таблице пользователей ВП')
@allure.title('Сравнение значения поля "phone_mobile" лида в ВП и в БД')
@pytest.mark.api_test
def test_comparse_phone_mobile_from_vp_and_db(session_id):
    lead_api = LeadApi()
    lead_api.create_post_body(session_id)
    lead_api.post_new_lead(lead_api.payload)
    lead_api.check_comparse_phone_mobile_from_vp_and_db()
