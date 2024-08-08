import allure
import pytest

from hw_09.locators.locators import Selectors
from hw_09.pages.api.appeals_api import AppealsApi
from hw_09.schema.schemas import AppealsSchema


@allure.epic('FCK project')
@allure.suite('API tests')
@allure.feature('Запросы к таблице обращений')
@allure.title('Проверка status-кода запроса')
@pytest.mark.xxxx
def test_status_code(session_id):
    appeal_api = AppealsApi()
    appeal_api.create_post_body(session_id)
    appeal_api.check_post_status_code(
        endpoint=Selectors.ENDPOINT_POST,
        schema=AppealsSchema,
        params=appeal_api.payload
    )


@allure.epic('FCK project')
@allure.suite('API tests')
@allure.feature('Запросы к таблице обращений')
@allure.title('Проверка поля "subject" созданного обращения')
@pytest.mark.xxxx
def test_post_created_appeal_subject(session_id):
    appeal_api = AppealsApi()
    appeal_api.create_post_body(session_id)
    appeal_api.post_new_appeal(appeal_api.payload)
    appeal_api.check_created_appeal_subject()


@allure.epic('FCK project')
@allure.suite('API tests')
@allure.feature('Запросы к таблице обращений')
@allure.title('Проверка поля "short_name" созданного обращения')
@pytest.mark.api_test
def test_post_created_appeal_short_name(session_id):
    appeal_api = AppealsApi()
    appeal_api.create_post_body(session_id)
    appeal_api.post_new_appeal(appeal_api.payload)
    appeal_api.check_created_appeal_short_name()


@allure.epic('FCK project')
@allure.suite('API tests')
@allure.feature('Запросы к таблице обращений')
@allure.title('Проверка поля "description" созданного обращения')
@pytest.mark.api_test
def test_post_created_appeal_description(session_id):
    appeal_api = AppealsApi()
    appeal_api.create_post_body(session_id)
    appeal_api.post_new_appeal(appeal_api.payload)
    appeal_api.check_created_appeal_description()


@allure.epic('FCK project')
@allure.suite('API tests')
@allure.feature('Запросы к таблице обращений')
@allure.title('Проверка поля "date_entered" созданного обращения')
@pytest.mark.api_test
def test_post_created_appeal_date_entered(session_id):
    appeal_api = AppealsApi()
    appeal_api.create_post_body(session_id)
    appeal_api.post_new_appeal(appeal_api.payload)
    appeal_api.check_created_appeal_date_entered()


@allure.epic('FCK project')
@allure.suite('API tests')
@allure.feature('Запросы к таблице обращений')
@allure.title('Сравнение значения поля "subject" обращения в ВП и в БД')
@pytest.mark.api_test
def test_comparse_subject_from_vp_and_db(session_id):
    appeal_api = AppealsApi()
    appeal_api.create_post_body(session_id)
    appeal_api.post_new_appeal(appeal_api.payload)
    appeal_api.check_comparse_subject_from_vp_and_db()


@allure.epic('FCK project')
@allure.suite('API tests')
@allure.feature('Запросы к таблице обращений')
@allure.title('Сравнение значения поля "short_name" обращения в ВП и в БД')
@pytest.mark.api_test
def test_comparse_short_name_from_vp_and_db(session_id):
    appeal_api = AppealsApi()
    appeal_api.create_post_body(session_id)
    appeal_api.post_new_appeal(appeal_api.payload)
    appeal_api.check_comparse_short_name_from_vp_and_db()


@allure.epic('FCK project')
@allure.suite('API tests')
@allure.feature('Запросы к таблице обращений')
@allure.title('Сравнение значения поля "description" обращения в ВП и в БД')
@pytest.mark.api_test
def test_comparse_description_from_vp_and_db(session_id):
    appeal_api = AppealsApi()
    appeal_api.create_post_body(session_id)
    appeal_api.post_new_appeal(appeal_api.payload)
    appeal_api.check_comparse_description_from_vp_and_db()


@allure.epic('FCK project')
@allure.suite('API tests')
@allure.feature('Запросы к таблице обращений')
@allure.title('Сравнение значения поля "date_entered" обращения в ВП и в БД')
@pytest.mark.api_test
def test_comparse_date_entered_from_vp_and_db(session_id):
    appeal_api = AppealsApi()
    appeal_api.create_post_body(session_id)
    appeal_api.post_new_appeal(appeal_api.payload)
    appeal_api.check_comparse_date_entered_from_vp_and_db()
