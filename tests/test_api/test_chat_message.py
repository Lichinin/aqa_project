
import allure
import pytest

from hw_09.locators.locators import Selectors
from hw_09.pages.api.chat_message_api import ChatMessageApi
from hw_09.schema.schemas import ChatMessageSchema


@allure.epic('FCK project')
@allure.suite('API tests')
@allure.feature('Запросы к таблице сообщений')
@allure.title('Проверка status-кода запроса')
@pytest.mark.api_test
def test_status_code(session_id):
    message_api = ChatMessageApi()
    message_api.create_post_body(session_id)
    message_api.check_post_status_code(
        endpoint=Selectors.ENDPOINT_POST,
        schema=ChatMessageSchema,
        params=message_api.payload
    )

@allure.epic('FCK project')
@allure.suite('API tests')
@allure.feature('Запросы к таблице сообщений')
@allure.title('Проверка создания оюращения')
@pytest.mark.skip(reason='Не готов. Не могу передать params в связанные таблицы')
@pytest.mark.api_test
def test_post_created_appeal_subject(session_id):
    message_api = ChatMessageApi()
    message_api.create_post_body(session_id)
    message_api.post_new_appeal(appeal_api.payload)
    message_api.check_created_appeal_subject()
