import json
from typing import Dict

import allure
import mysql.connector
from faker import Faker

from hw_09.locators.locators import Selectors
from hw_09.pages.api.base_api import BasseAPI
from hw_09.schema.schemas import AppealsSchema

fake = Faker()


class AppealsApi(BasseAPI):

    def __init__(self):
        self.base_url = 'http://fckproject.itfbgroup.ru'

    @allure.step('Передается POST-запрос. Создается новое обращение')
    def post_new_appeal(self, params):
        self.created_appeal = self.post_valid_request(
            Selectors.ENDPOINT_POST,
            AppealsSchema,
            params=params
        ).json()

    @allure.step('Создание тела запроса')
    def create_post_body(self, session_id) -> Dict:
        self.last_name = fake.last_name()
        self.first_name = 'delete_it'
        self.second_name = fake.first_name()
        self.date_entered = fake.date_time().strftime("%Y-%m-%d %H:%M:%S")
        self.processing_deadline = fake.date_time().strftime("%Y-%m-%d %H:%M:%S")
        self.phone_mobile = fake.phone_number()
        self.email1 = fake.email()
        self.acc_portal_inn = fake.ssn().replace("-", "")
        self.subject = ' '.join(fake.words(5))
        self.short_name = ' '.join(fake.words(5))
        self.description = ' '.join(fake.words(5))
        payload = {
            "method": 'set_entry',
            "input_type": 'JSON',
            "response_type": 'JSON',
            "rest_data": json.dumps({
                "session": session_id,
                "module": "Cases",
                "name_value_list": {
                    "portal_id": None,
                    "id": None,
                    "last_name": self.last_name,
                    "first_name": self.first_name,
                    "mid_name": self.second_name,
                    "contact_emails": self.email1,
                    "channel": None,
                    "subject": self.subject,
                    "short_name": self.short_name,
                    "description": self.description,
                    "date_entered": self.date_entered,
                    "status": None,
                    "resolution": None,
                    "processing_deadline": self.processing_deadline,
                    "contacts_id": None,
                    "leads_portal_id": None,
                    "feedback": None,
                    "feedback_com": None
                }
            })
        }
        self.payload = payload

    @allure.step('Выполняется проверка поля "subject" созданного обращения')
    def check_created_appeal_subject(self):
        created_lead_subject = self.created_appeal['entry_list']['subject']['value']
        setted_lead_subject = self.subject
        assert created_lead_subject == setted_lead_subject

    @allure.step('Выполняется проверка поля "short_name" созданного обращения')
    def check_created_appeal_short_name(self):
        created_lead_short_name = self.created_appeal['entry_list']['short_name']['value']
        setted_lead_short_name = self.short_name
        assert created_lead_short_name == setted_lead_short_name

    @allure.step('Выполняется проверка поля "description" созданного обращения')
    def check_created_appeal_description(self):
        created_lead_description = self.created_appeal['entry_list']['description']['value']
        setted_lead_description = self.description
        assert created_lead_description == setted_lead_description

    @allure.step('Выполняется проверка поля "date_entered" созданного обращения')
    def check_created_appeal_date_entered(self):
        created_lead_date_entered = self.created_appeal['entry_list']['date_entered']['value']
        setted_lead_date_entered = self.date_entered
        assert created_lead_date_entered == setted_lead_date_entered

    @allure.step('Получение объекта из базы данных')
    def get_db_appeal_object(self):
        db = mysql.connector.connect(
            host="77.244.210.184",
            port=44999,
            user="user_auto",
            password="crmbdpasswauto",
            database="db_auto"
        )
        cursor = db.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM cases WHERE id='{self.created_appeal['id']}'")
        results = cursor.fetchall()
        db.close()
        return results[0]

    @allure.step('Выполняется сравнение значения поля "subject" обращения в ВП и в БД')
    def check_comparse_subject_from_vp_and_db(self):
        vp_object = self.created_appeal
        db_object = self.get_db_appeal_object()
        assert vp_object['entry_list']['subject']['value'] == db_object['subject']

    @allure.step('Выполняется сравнение значения поля "short_name" обращения в ВП и в БД')
    def check_comparse_short_name_from_vp_and_db(self):
        vp_object = self.created_appeal
        db_object = self.get_db_appeal_object()
        assert vp_object['entry_list']['short_name']['value'] == db_object['short_name']

    @allure.step('Выполняется сравнение значения поля "description" обращения в ВП и в БД')
    def check_comparse_description_from_vp_and_db(self):
        vp_object = self.created_appeal
        db_object = self.get_db_appeal_object()
        assert vp_object['entry_list']['description']['value'] == db_object['description']

    @allure.step('Выполняется сравнение значения поля "date_entered" обращения в ВП и в БД')
    def check_comparse_date_entered_from_vp_and_db(self):
        vp_object = self.created_appeal
        db_object = self.get_db_appeal_object()
        assert vp_object['entry_list']['date_entered']['value'] == (db_object['date_entered']).strftime('%Y-%m-%d %H:%M:%S')
