from datetime import datetime

import allure
import mysql.connector

from hw_09.locators.locators import Selectors
from hw_09.pages.api.base_api import BasseAPI
from hw_09.schema.schemas import UserListSchema


class UserListApi(BasseAPI):

    @allure.step('Выполняется GET-запрос получение списка пользователей')
    def get_user_list(self, params):
        self.user_list = self.get_valid_request(
            Selectors.ENDPOINT_USERS,
            UserListSchema,
            params=params
        ).json()

    @allure.step('Выполняется проверка количества пользователей в ответе')
    def check_users_count(self, excetped):
        assert len(self.user_list['results']) == excetped

    @allure.step('Выполняется проверка параметра offset ответа')
    def check_param_ofset_userlist(self, excetped):
        assert self.user_list['results'][0]['id'] == excetped + 1

    @allure.step('Выполняется проверка параметра updated_at_from ответа')
    def check_param__updated_at_from_userlist(self, excepted):
        setted_data = datetime.fromisoformat(excepted).date()
        actual_data = datetime.fromisoformat(
            self.user_list['results'][0]['updated_at']
        ).date()
        assert actual_data >= setted_data

    @allure.step('Выполняется проверка параметра updated_at_to ответа')
    def check_param__updated_at_to_userlist(self, excepted):
        setted_data = datetime.fromisoformat(excepted).date()
        actual_data = datetime.fromisoformat(
            self.user_list['results'][0]['updated_at']
        ).date()
        assert actual_data <= setted_data

    @allure.step('Получение объекта с внешнего портала')
    def get_vp_oject(self):
        return self.user_list['results'][0]

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
        cursor.execute(f"SELECT * FROM leads WHERE portal_id='{portal_id}'")
        results = cursor.fetchall()
        db.close()
        return results[0]

    @allure.step('Выполняется сравнение значения поля "id" пользователя в ВП и в БД')
    def check_comparse_id_from_vp_and_db(self):
        vp_object = self.get_vp_oject()
        db_object = self.get_db_object(vp_object['id'])
        assert vp_object['id'] == int(db_object['portal_id'])

    @allure.step('Выполняется сравнение значения поля "phone_number" пользователя в ВП и в БД')
    def check_comparse_phone_number_from_vp_and_db(self):
        vp_object = self.get_vp_oject()
        db_object = self.get_db_object(vp_object['id'])
        assert (
            (vp_object['phone_number'] == db_object['phone_mobile']) or
            (vp_object['phone_number'] == '' and db_object['phone_mobile'] is None)
        )

    @allure.step('Выполняется сравнение значения поля "position" пользователя в ВП и в БД')
    def check_comparse_position_from_vp_and_db(self):
        vp_object = self.get_vp_oject()
        db_object = self.get_db_object(vp_object['id'])
        assert vp_object['position'] == db_object['title']

    @allure.step('Выполняется сравнение значения поля "last_name" пользователя в ВП и в БД')
    def check_comparse_last_name_from_vp_and_db(self):
        vp_object = self.get_vp_oject()
        db_object = self.get_db_object(vp_object['id'])
        assert vp_object['last_name'] == db_object['last_name']

    @allure.step('Выполняется сравнение значения поля "first_name" пользователя в ВП и в БД')
    def check_comparse_first_name_from_vp_and_db(self):
        vp_object = self.get_vp_oject()
        db_object = self.get_db_object(vp_object['id'])
        assert vp_object['first_name'] == db_object['first_name']
