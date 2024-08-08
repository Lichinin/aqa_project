import json
from typing import Dict

import allure
import mysql.connector
from faker import Faker

from hw_09.locators.locators import Selectors
from hw_09.pages.api.base_api import BasseAPI
from hw_09.schema.schemas import LeadSchema

fake = Faker()


class LeadApi(BasseAPI):

    def __init__(self):
        self.base_url = 'http://fckproject.itfbgroup.ru'

    @allure.step('Передается POST-запрос. Создается новый лид')
    def post_new_lead(self, params):
        self.created_lead = self.post_valid_request(
            Selectors.ENDPOINT_POST,
            LeadSchema,
            params=params
        ).json()

    @allure.step('Создание тела запроса')
    def create_post_body(self, session_id) -> Dict:
        self.last_name = fake.last_name()
        self.first_name = 'delete_it'
        self.second_name = fake.first_name()
        self.vp_date_modified = fake.date_time().strftime("%Y-%m-%d %H:%M:%S")
        self.phone_mobile = fake.phone_number()
        self.email1 = fake.email()
        self.acc_portal_inn = fake.ssn().replace("-", "")
        payload = {
            "method": 'set_entry',
            "input_type": 'JSON',
            "response_type": 'JSON',
            "rest_data": json.dumps({
                "session": session_id,
                "module": "Leads",
                "name_value_list": {
                    "portal_id": None,
                    "vp_date_modified": self.vp_date_modified,
                    "last_name": self.last_name,
                    "first_name": self.first_name,
                    "second_name": self.second_name,
                    "birthdate": None,
                    "gender": None,
                    "phone_mobile": self.phone_mobile,
                    "email1": self.email1,
                    "acc_portal_id": None,
                    "account_name": "",
                    "acc_portal_inn": self.acc_portal_inn,
                    "title": None,
                    "portal_user": True
                }
            })
        }
        self.payload = payload

    @allure.step('Получение объекта из базы данных')
    def get_db_lead_object(self):
        db = mysql.connector.connect(
            host="77.244.210.184",
            port=44999,
            user="user_auto",
            password="crmbdpasswauto",
            database="db_auto"
        )
        cursor = db.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM leads WHERE id='{self.created_lead['id']}'")
        results = cursor.fetchall()
        db.close()
        return results[0]

    @allure.step('Выполняется сравнение значения поля "inn" лида в ВП и в БД')
    def check_comparse_inn_from_vp_and_db(self):
        vp_object = self.created_lead
        db_object = self.get_db_lead_object()
        assert vp_object['entry_list']['acc_portal_inn']['value'] == db_object['acc_portal_inn']

    @allure.step('Выполняется сравнение значения поля "last_name" лида в ВП и в БД')
    def check_comparse_last_name_from_vp_and_db(self):
        vp_object = self.created_lead
        db_object = self.get_db_lead_object()
        assert vp_object['entry_list']['last_name']['value'] == db_object['last_name']

    @allure.step('Выполняется сравнение значения поля "vp_date_modified" лида в ВП и в БД')
    def check_comparse_vp_date_modified_from_vp_and_db(self):
        vp_object = self.created_lead
        db_object = self.get_db_lead_object()
        assert vp_object['entry_list']['vp_date_modified']['value'] == (db_object['vp_date_modified']).strftime('%Y-%m-%d %H:%M:%S')

    @allure.step('Выполняется проверка')
    def check_comparse_phone_mobile_from_vp_and_db(self):
        vp_object = self.created_lead
        db_object = self.get_db_lead_object()
        assert vp_object['entry_list']['phone_mobile']['value'] == db_object['phone_mobile']

    @allure.step('Выполняется сравнение значения поля "phone_mobile" лида в ВП и в БД')
    def check_created_lead_last_name(self):
        created_lead_last_name = self.created_lead['entry_list']['last_name']['value']
        setted_lead_last_name = self.last_name
        assert created_lead_last_name == setted_lead_last_name

    @allure.step('Выполняется проверка поля "second_name" созданного лида')
    def check_created_lead_second_name(self):
        created_lead_second_name = self.created_lead['entry_list']['second_name']['value']
        setted_lead_second_name = self.second_name
        assert created_lead_second_name == setted_lead_second_name

    @allure.step('Выполняется проверка поля "vp_date_modified" созданного лида')
    def check_created_lead_vp_date_modified(self):
        created_lead_vp_date_modified = self.created_lead['entry_list']['vp_date_modified']['value']
        setted_lead_vp_date_modified = self.vp_date_modified
        assert created_lead_vp_date_modified == setted_lead_vp_date_modified

    @allure.step('Выполняется проверка поля "phone_mobile" созданного лида')
    def check_created_lead_phone_mobile(self):
        created_lead_phone_mobil = self.created_lead['entry_list']['phone_mobile']['value']
        setted_lead_phone_mobil = self.phone_mobile
        assert created_lead_phone_mobil == setted_lead_phone_mobil

    @allure.step('Выполняется проверка поля "email" созданного лида')
    def check_created_lead_email(self):
        created_lead_email = self.created_lead['entry_list']['email1']['value']
        setted_lead_email = self.email1
        assert created_lead_email == setted_lead_email

    @allure.step('Выполняется проверка поля "acc_portal_inn" созданного лида')
    def check_created_lead_inn(self):
        created_lead_inn = self.created_lead['entry_list']['acc_portal_inn']['value']
        setted_lead_inn = self.acc_portal_inn
        assert created_lead_inn == setted_lead_inn
