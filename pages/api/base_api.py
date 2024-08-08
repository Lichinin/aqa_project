import allure
import requests


class BasseAPI():

    def __init__(self, authorization_token):
        self.base_url = 'https://xn--e1atd.xn--b1aedfedwqbdfbnzkf0oe.xn--p1ai'
        self.headers = authorization_token

    @allure.step('Выполнение GET-запроса с проверкой схемы')
    def get_valid_request(self, endpoint, schema, params=None, ):
        url = f'{self.base_url}{endpoint}'
        response = requests.get(
            url,
            params,
            headers=self.headers,
            verify=False
        )

        data = response.json()
        [schema(**item) for item in data['results']]
        return response

    @allure.step('Подготовка параметров для GET-запроса')
    def create_params(self, limit, offset, updated_at_from, updated_at_to):
        self.params = {
            "limit": limit,
            "offset": offset,
            "updated_at_from": updated_at_from,
            "updated_at_to": updated_at_to
        }

    @allure.step('Выполнение POST-запроса с проверкой схемы')
    def post_valid_request(self, endpoint, schema, params=None, ):
        url = f'{self.base_url}{endpoint}'
        response = requests.post(
            url,
            data=params,
            verify=False
        )

        data = response.json()
        schema.parse_obj(data)
        return response

    @allure.step('Проверка статус-кода ответа для GET-запроса')
    def check_status_code(self, endpoint, schema, params):
        response = self.get_valid_request(endpoint, schema, params)
        assert response.status_code == 200

    @allure.step('Проверка статус-кода ответа для POST-запроса')
    def check_post_status_code(self, endpoint, schema, params):
        response = self.post_valid_request(endpoint, schema, params)
        assert response.status_code == 200
