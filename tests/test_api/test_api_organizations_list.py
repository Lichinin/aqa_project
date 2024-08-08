import allure
import pytest

from hw_09.locators.locators import Selectors
from hw_09.pages.api.organizations_list_api import OrganizationsListApi
from hw_09.schema.schemas import OrganizationsListSchema


@allure.epic('FCK project')
@allure.suite('API tests')
@allure.feature('Запросы к таблице организаций')
@allure.title('Проверка status-кода запроса')
@pytest.mark.api_test
def test_status_code(authorization_token):
    organizations_list = OrganizationsListApi(authorization_token)
    organizations_list.create_params(
        limit=3,
        offset=None,
        updated_at_from=None,
        updated_at_to=None
    )
    organizations_list.check_status_code(
        endpoint=Selectors.ENDPOINT_ORGANIZATIONS,
        schema=OrganizationsListSchema,
        params=organizations_list.params
    )


@allure.epic('FCK project')
@allure.suite('API tests')
@allure.feature('Запросы к таблице организаций')
@allure.title('Проверка количества организаций в ответе')
@pytest.mark.api_test
def test_get_limit_organizations_list(authorization_token):
    organizations_list = OrganizationsListApi(authorization_token)
    organizations_list.create_params(
        limit=3,
        offset=None,
        updated_at_from=None,
        updated_at_to=None
    )
    organizations_list.get_organizations_list(organizations_list.params)
    organizations_list.check_organizations_count(
        organizations_list.params['limit']
    )


@allure.epic('FCK project')
@allure.suite('API tests')
@allure.feature('Запросы к таблице организаций')
@allure.title('Проверка параметра "offset" запроса')
@pytest.mark.api_test
def test_get_ofset_organizations_list(authorization_token):
    organizations_list = OrganizationsListApi(authorization_token)
    organizations_list.create_params(
        limit=1,
        offset=1,
        updated_at_from=None,
        updated_at_to=None
    )
    organizations_list.get_organizations_list(organizations_list.params)
    organizations_list.check_param_ofset(organizations_list.params['offset'])


@allure.epic('FCK project')
@allure.suite('API tests')
@allure.feature('Запросы к таблице организаций')
@allure.title('Проверка параметра "updated_at_from" запроса')
@pytest.mark.api_test
def test_updated_at_from_organizations_list(authorization_token):
    organizations_list = OrganizationsListApi(authorization_token)
    organizations_list.create_params(
        limit=1,
        offset=None,
        updated_at_from='2024-01-01',
        updated_at_to=None
    )
    organizations_list.get_organizations_list(organizations_list.params)
    organizations_list.check_param__updated_at_from(
        organizations_list.params['updated_at_from']
    )


@allure.epic('FCK project')
@allure.suite('API tests')
@allure.feature('Запросы к таблице организаций')
@allure.title('Проверка параметра "updated_at_to" запроса')
@pytest.mark.api_test
def test_updated_at_to_organizations_list(authorization_token):
    organizations_list = OrganizationsListApi(authorization_token)
    organizations_list.create_params(
        limit=1,
        offset=None,
        updated_at_from=None,
        updated_at_to='2024-01-01'
    )
    organizations_list.get_organizations_list(organizations_list.params)
    organizations_list.check_param__updated_at_to(
        organizations_list.params['updated_at_to']
    )


@allure.epic('FCK project')
@allure.suite('API tests')
@allure.feature('Запросы к таблице организаций')
@allure.title('Сравнение значения поля "id" организации в ВП и в БД')
@pytest.mark.api_test
def test_comparse_id_from_vp_and_db(authorization_token):
    organizations_list = OrganizationsListApi(authorization_token)
    organizations_list.create_params(
        limit=3,
        offset=None,
        updated_at_from=None,
        updated_at_to=None
    )
    organizations_list.get_organizations_list(organizations_list.params)
    organizations_list.check_comparse_id_from_vp_and_db()


@allure.epic('FCK project')
@allure.suite('API tests')
@allure.feature('Запросы к таблице организаций')
@allure.title('Сравнение значения поля "title" организации в ВП и в БД')
@pytest.mark.api_test
def test_comparse_title_from_vp_and_db(authorization_token):
    organizations_list = OrganizationsListApi(authorization_token)
    organizations_list.create_params(
        limit=3,
        offset=None,
        updated_at_from=None,
        updated_at_to=None
    )
    organizations_list.get_organizations_list(organizations_list.params)
    organizations_list.check_comparse_title_from_vp_and_db()


@allure.epic('FCK project')
@allure.suite('API tests')
@allure.feature('Запросы к таблице организаций')
@allure.title('Сравнение значения поля "region_id" организации в ВП и в БД')
@pytest.mark.api_test
def test_comparse_region_id_from_vp_and_db(authorization_token):
    organizations_list = OrganizationsListApi(authorization_token)
    organizations_list.create_params(
        limit=3,
        offset=None,
        updated_at_from=None,
        updated_at_to=None
    )
    organizations_list.get_organizations_list(organizations_list.params)
    organizations_list.check_comparse_region_id_from_vp_and_db()


@allure.epic('FCK project')
@allure.suite('API tests')
@allure.feature('Запросы к таблице организаций')
@allure.title('Сравнение значения поля "site_url" организации в ВП и в БД')
@pytest.mark.api_test
def test_comparse_site_url_from_vp_and_db(authorization_token):
    organizations_list = OrganizationsListApi(authorization_token)
    organizations_list.create_params(
        limit=3,
        offset=None,
        updated_at_from=None,
        updated_at_to=None
    )
    organizations_list.get_organizations_list(organizations_list.params)
    organizations_list.check_comparse_site_url_from_vp_and_db()


@allure.epic('FCK project')
@allure.suite('API tests')
@allure.feature('Запросы к таблице организаций')
@allure.title('Сравнение значения поля "baseyear" организации в ВП и в БД')
@pytest.mark.api_test
def test_comparse_baseyear_from_vp_and_db(authorization_token):
    organizations_list = OrganizationsListApi(authorization_token)
    organizations_list.create_params(
        limit=3,
        offset=None,
        updated_at_from=None,
        updated_at_to=None
    )
    organizations_list.get_organizations_list(organizations_list.params)
    organizations_list.check_comparse_baseyear_from_vp_and_db()
