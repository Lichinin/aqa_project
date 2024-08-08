import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from hw_09.locators.locators import Selectors


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.logger = browser.logger

    @allure.step('Поиск элемента на странице')
    def get_element(self, locator: tuple, timeout=3):
        with allure.step(f'Поиск эелемента "{locator}"'):
            try:
                self.browser.logger.info(f'* Get element "{repr(locator)}"')
                return WebDriverWait(self.browser, timeout).until(
                    EC.visibility_of_element_located(locator)
                )
            except Exception:
                allure.attach(
                    name="failure_screenshot",
                    body=self.browser.get_screenshot_as_png(),
                    attachment_type=allure.attachment_type.PNG
                )
            self.logger.exception('Error: element not found!')
            raise

    @allure.step('Поиск элементов на странице')
    def get_elements(self, locator: tuple, timeout=3):
        with allure.step(f'Поиск элементов "{locator}"'):
            self.browser.logger.info(f'* Get elements {repr(locator)}')
            return WebDriverWait(self.browser, timeout).until(
                EC.visibility_of_all_elements_located(locator)
            )

    @allure.step('Поиск текста в заголовке браузера')
    def try_get_browser_title(self, expected_title):
        return WebDriverWait(self.browser, 10).until(
            (EC.title_contains(expected_title))
        )

    @allure.step('Вводится логин администратора')
    def fill_username(self, username):
        self.fill_the_field(Selectors.USERNAME_FIELD_SELECTOR, username)

    @allure.step('Вводится пароль администратора')
    def fill_password(self, password):
        self.fill_the_field(Selectors.PASSWORD_FIELD_SELECTOR, password)

    @allure.step('Нажимается кнопка "Login"')
    def click_login_button(self):
        self.get_element(Selectors.LOGIN_BUTTON_SELECTOR).click()

    @allure.step('Ожидание появления текста в элементе "{locator}"')
    def wait_for_text(self, element, locator, timeout=3):
        return WebDriverWait(self.browser, timeout).until(
            EC.text_to_be_present_in_element(element, locator)
        )

    @allure.step('Получаю заголовки "{locator}"')
    def get_headers(self, locator: tuple):
        button = self.get_elements(locator)
        return {text.text for text in button}

    @allure.step('Ввожу в поле "{locator}" текст "{text}"')
    def fill_the_field(self, locator, text):
        field = self.get_element(locator)
        field.click()
        field.send_keys(text)
        return field

    @allure.step('Ожидание загрузки страницы')
    def wait_for_loading_page(self):
        try:
            WebDriverWait(self.browser, 3).until_not(
                EC.presence_of_element_located(Selectors.LOADING_MASK)
            )
        except Exception:
            pass

    @allure.step('Переход по url-адресу')
    def open_page(self):
        self.browser.get(self.browser.url)

    @allure.step('Переключение на новую вкладку')
    def switch_to_new_window(self):
        all_windows = self.browser.window_handles
        self.browser.switch_to.window(all_windows[-1])

    @allure.step('Переключение на начальную вкладку')
    def switch_to_main_window(self):
        all_windows = self.browser.window_handles
        self.browser.switch_to.window(all_windows[0])

    @allure.step('Получение списка элементов по нажатию на кнопку "Все"')
    def get_button_all_values(self):
        button_all_values = self.get_elements(
            Selectors.HEADER_BUTTON_ALL_VALUES
        )
        button_all_values = {element.text for element in button_all_values}
        return button_all_values

    @allure.step('Нажатие кнопки "Все"')
    def click_button_all(self):
        self.get_element(Selectors.HEADER_BUTTON_ALL).click()

    @allure.step('Проверка assert_equals')
    def assert_equals(self, expected, actual):
        self.logger.info('* Check assertion assert_equals')
        try:
            assert expected == actual, f"Expected: '{expected}', Actual: '{actual}'"
            self.logger.info('*** Test completed successful ***')
        except AssertionError:
            allure.attach(
                name="failure_screenshot",
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            self.logger.exception('!!! Test failed !!!')
            raise

    @allure.step('Проверка assert_browser_title')
    def assert_browser_title(self, expected_title):
        self.logger.info('* Check assertion assert_browser_title')
        try:
            assert self.try_get_browser_title(expected_title), f"Title not contains '{expected_title}'"
            self.logger.info('*** Test completed successful ***')
        except AssertionError:
            allure.attach(
                name="failure_screenshot",
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            self.logger.exception('!!! Test failed !!!')
            raise

    @allure.step('Проверка assert_browser_url')
    def assert_browser_url(self, expected_url):
        self.logger.info('* Check assertion assert_browser_url')
        current_url = self.browser.current_url
        try:
            assert expected_url in current_url, f"{current_url} not contains '{expected_url}'"
            self.logger.info('*** Test completed successful ***')
        except AssertionError:
            allure.attach(
                name="failure_screenshot",
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            self.logger.exception('!!! Test failed !!!')
            raise

    @allure.step('Проверка assert_subset')
    def assert_subset(self, expected, actual):
        self.logger.info('* Check assertion assert_subset')
        try:
            assert expected.issubset(actual), 'Actual values not contain expected values'
            self.logger.info('*** Test completed successful ***')
        except AssertionError:
            allure.attach(
                name="failure_screenshot",
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            self.logger.exception('!!! Test failed !!!')
            raise

    @allure.step('Проверка assert_page_title')
    def assert_page_title(self, expected, locator):
        self.logger.info('* Check assertion assert_page_title')
        try:
            assert WebDriverWait(self.browser, 10).until(
                EC.text_to_be_present_in_element(locator, expected)
            ), f"Page not contains '{expected}'"
            self.logger.info('*** Test completed successful ***')
        except AssertionError:
            allure.attach(
                name="failure_screenshot",
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            self.logger.exception('!!! Test failed !!!')
            raise

    @allure.step('Выполняется проверка значений элементов, полученных по нажанию на кнопку "Все"')
    def assert_button_all_values(self):
        values = self.get_button_all_values()
        self.assert_equals(Selectors.HEADER_BUTTON_ALL_CORRECT_VALUES, values)

    @allure.step('Выполняется проверка title страницы')
    def assert_create_page_title(self):
        self.assert_browser_title('Создать')

    @allure.step('Нажатие кнопки OK в allert')
    def accept_allert(self):
        wait = WebDriverWait(self.browser, timeout=10)
        alert = wait.until(EC.alert_is_present())
        alert.accept()
