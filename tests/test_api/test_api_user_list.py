import allure
import pytest

from hw_09.locators.locators import Selectors
from hw_09.pages.api.user_list_api import UserListApi
from hw_09.schema.schemas import UserListSchema


@allure.epic('FCK project')
@allure.suite('API tests')
@allure.feature('Запросы к таблице пользователей')
@allure.title('Проверка status-кода запроса')
@pytest.mark.api_test
def test_status_code(authorization_token):
    user_list = UserListApi(authorization_token)
    user_list.create_params(
        limit=3,
        offset=None,
        updated_at_from=None,
        updated_at_to=None
    )
    user_list.check_status_code(
        endpoint=Selectors.ENDPOINT_USERS,
        schema=UserListSchema,
        params=user_list.params
    )


@allure.epic('FCK project')
@allure.suite('API tests')
@allure.feature('Запросы к таблице пользователей')
@allure.title('Проверка количества пользователей в ответе')
@pytest.mark.api_test
def test_param_limit_user_list(authorization_token):
    user_list = UserListApi(authorization_token)
    user_list.create_params(
        limit=5,
        offset=None,
        updated_at_from=None,
        updated_at_to=None
    )
    user_list.get_user_list(user_list.params)
    user_list.check_users_count(user_list.params['limit'])


@allure.epic('FCK project')
@allure.suite('API tests')
@allure.feature('Запросы к таблице пользователей')
@allure.title('Проверка параметра offset ответа')
@pytest.mark.api_test
def test_param_ofset_user_list(authorization_token):
    user_list = UserListApi(authorization_token)
    user_list.create_params(
        limit=1,
        offset=1,
        updated_at_from=None,
        updated_at_to=None
    )
    user_list.get_user_list(user_list.params)
    user_list.check_param_ofset_userlist(user_list.params['offset'])


@allure.epic('FCK project')
@allure.suite('API tests')
@allure.feature('Запросы к таблице пользователей')
@allure.title('Проверка параметра updated_at_from ответа')
@pytest.mark.api_test
def test_param_updated_at_from_user_list(authorization_token):
    user_list = UserListApi(authorization_token)
    user_list.create_params(
        limit=1,
        offset=None,
        updated_at_from='2024-01-01',
        updated_at_to=None
    )
    user_list.get_user_list(user_list.params)
    user_list.check_param__updated_at_from_userlist(
        user_list.params['updated_at_from']
    )


@allure.epic('FCK project')
@allure.suite('API tests')
@allure.feature('Запросы к таблице пользователей')
@allure.title('Проверка параметра updated_at_to ответа')
@pytest.mark.api_test
def test_updated_at_to_user_list(authorization_token):
    user_list = UserListApi(authorization_token)
    user_list.create_params(
        limit=1,
        offset=None,
        updated_at_from=None,
        updated_at_to='2024-01-01'
    )
    user_list.get_user_list(user_list.params)
    user_list.check_param__updated_at_to_userlist(
        user_list.params['updated_at_to']
    )


@allure.epic('FCK project')
@allure.suite('API tests')
@allure.feature('Запросы к таблице пользователей')
@allure.title('Сравнение значения поля "id" пользователя в ВП и в БД')
@pytest.mark.api_test
def test_comparse_id_from_vp_and_db(authorization_token):
    user_list = UserListApi(authorization_token)
    user_list.create_params(
        limit=1,
        offset=1,
        updated_at_from=None,
        updated_at_to=None
    )
    user_list.get_user_list(user_list.params)
    user_list.check_comparse_id_from_vp_and_db()


@allure.epic('FCK project')
@allure.suite('API tests')
@allure.feature('Запросы к таблице пользователей')
@allure.title(
    'Сравнение значения поля "phone_number" пользователя в ВП и в БД'
)
@pytest.mark.api_test
def test_comparse_phone_number_from_vp_and_db(authorization_token):
    user_list = UserListApi(authorization_token)
    user_list.create_params(
        limit=1,
        offset=1,
        updated_at_from=None,
        updated_at_to=None
    )
    user_list.get_user_list(user_list.params)
    user_list.check_comparse_phone_number_from_vp_and_db()


@allure.epic('FCK project')
@allure.suite('API tests')
@allure.feature('Запросы к таблице пользователей')
@allure.title('Сравнение значения поля "position" пользователя в ВП и в БД')
@pytest.mark.api_test
def test_comparse_position_from_vp_and_db(authorization_token):
    user_list = UserListApi(authorization_token)
    user_list.create_params(
        limit=1,
        offset=1,
        updated_at_from=None,
        updated_at_to=None
    )
    user_list.get_user_list(user_list.params)
    user_list.check_comparse_position_from_vp_and_db()


@allure.epic('FCK project')
@allure.suite('API tests')
@allure.feature('Запросы к таблице пользователей')
@allure.title('Сравнение значения поля "last_name" пользователя в ВП и в БД')
@pytest.mark.api_test
def test_comparse_last_name_from_vp_and_db(authorization_token):
    user_list = UserListApi(authorization_token)
    user_list.create_params(
        limit=1,
        offset=1,
        updated_at_from=None,
        updated_at_to=None
    )
    user_list.get_user_list(user_list.params)
    user_list.check_comparse_last_name_from_vp_and_db()


@allure.epic('FCK project')
@allure.suite('API tests')
@allure.feature('Запросы к таблице пользователей')
@allure.title('Сравнение значения поля "first_name" пользователя в ВП и в БД')
@pytest.mark.api_test
def test_comparse_first_name_from_vp_and_db(authorization_token):
    user_list = UserListApi(authorization_token)
    user_list.create_params(
        limit=1,
        offset=1,
        updated_at_from=None,
        updated_at_to=None
    )
    user_list.get_user_list(user_list.params)
    user_list.check_comparse_first_name_from_vp_and_db()
