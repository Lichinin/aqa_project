import json
from typing import Dict

import allure
from faker import Faker

from hw_09.locators.locators import Selectors
from hw_09.pages.api.base_api import BasseAPI
from hw_09.schema.schemas import ChatMessageSchema

fake = Faker()


class ChatMessageApi(BasseAPI):

    def __init__(self):
        self.base_url = 'http://fckproject.itfbgroup.ru'

    @allure.step('Передается POST-запрос. Создается новое обращение')
    def post_new_appeal(self, params):
        self.created_message = self.post_valid_request(
            Selectors.ENDPOINT_POST,
            ChatMessageSchema,
            params=params
        ).json()

    @allure.step('Создание тела запроса')
    def create_post_body(self, session_id) -> Dict:
        self.name = ' '.join(fake.words(5))
        self.date_entered = fake.date_time().strftime('%d.%m.%Y %H:%M:%S')
        payload = {
            "method": 'set_entry',
            "input_type": 'JSON',
            "response_type": 'JSON',
            "rest_data": json.dumps({
                "session": session_id,
                "module": "Cases",
                "name_value_list": {
                    "id": '5f410391-bb3e-44c3-9c6e-261eb84ef536',
                    "notes": [
                        {
                            "id": None,
                            "filename": 'safsafasf.asf'
                        }
                    ],
                    "aop_case_updates": [
                        {
                            "case_id": '5f410391-bb3e-44c3-9c6e-261eb84ef536',
                            "name": 'sddsgdsg',
                            "date_entered": self.date_entered
                        }
                    ]
                }
            })
        }
        self.payload = payload

    @allure.step('Выполняется проверка')
    def check_created_appeal_subject(self):
        created_lead_subject = self.created_['entry_list']['subject']['value']
        setted_lead_subject = self.subject
        assert created_lead_subject == setted_lead_subject
