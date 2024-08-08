from datetime import datetime

import allure
import mysql.connector

from hw_09.locators.locators import Selectors
from hw_09.pages.api.base_api import BasseAPI
from hw_09.schema.schemas import OrganizationsListSchema


class OrganizationsListApi(BasseAPI):

    @allure.step('Выполняется GET-запрос получение списка организаций')
    def get_organizations_list(self, params):
        self.organizations_list = self.get_valid_request(
            Selectors.ENDPOINT_ORGANIZATIONS,
            OrganizationsListSchema,
            params=params
        ).json()

    @allure.step('Получение объекта с внешнего портала')
    def get_vp_oject(self):
        return self.organizations_list['results'][0]

    @allure.step('Получение объекта из базы данных')
    def get_db_object(self, portal_id):
        db = mysql.connector.connect(
            host="77.244.210.184",
            port=44999,
            user="user_auto",
            password="crmbdpasswauto",
            database="db_auto"
        )
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM accounts WHERE portal_id=1")
        results = cursor.fetchall()
        db.close()
        return results[0]

    @allure.step('Выполняется проверка количества организаций в ответе')
    def check_organizations_count(self, excetped):
        assert len(self.organizations_list['results']) == excetped

    @allure.step('Выполняется проверка параметра "offset" запроса')
    def check_param_ofset(self, excetped):
        assert self.organizations_list['results'][0]['id'] == excetped + 1

    @allure.step('Выполняется проверка параметра "updated_at_from" запроса')
    def check_param__updated_at_from(self, excepted):
        setted_data = datetime.fromisoformat(excepted).date()
        actual_data = datetime.fromisoformat(
            self.organizations_list['results'][0]['updated_at']
        ).date()
        assert actual_data >= setted_data

    @allure.step('Выполняется проверка')
    def check_param__updated_at_to(self, excepted):
        setted_data = datetime.fromisoformat(excepted).date()
        actual_data = datetime.fromisoformat(
            self.organizations_list['results'][0]['updated_at']
        ).date()
        assert actual_data <= setted_data

    @allure.step('Выполняется проверка')
    def check_comparse_id_from_vp_and_db(self):
        vp_object = self.get_vp_oject()
        db_object = self.get_db_object(vp_object['id'])
        assert vp_object['id'] == int(db_object['portal_id'])

    @allure.step('Выполняется проверка')
    def check_comparse_title_from_vp_and_db(self):
        vp_object = self.get_vp_oject()
        db_object = self.get_db_object(vp_object['id'])
        assert (
            (vp_object['title'] == db_object['name']) or
            (vp_object['title'] == '' and db_object['name'] is None)
        )

    @allure.step('Выполняется проверка')
    def check_comparse_region_id_from_vp_and_db(self):
        vp_object = self.get_vp_oject()
        db_object = self.get_db_object(vp_object['id'])
        assert vp_object['region_id'] == int(db_object['region'])

    @allure.step('Выполняется проверка')
    def check_comparse_site_url_from_vp_and_db(self):
        vp_object = self.get_vp_oject()
        db_object = self.get_db_object(vp_object['id'])
        assert (
            (vp_object['site_url'] == db_object['website']) or
            (vp_object['site_url'] == 'http://-' and db_object['website'] is None)
        )

    @allure.step('Выполняется проверка')
    def check_comparse_baseyear_from_vp_and_db(self):
        vp_object = self.get_vp_oject()
        db_object = self.get_db_object(vp_object['id'])
        assert vp_object['base_year'] == db_object['base_year']
