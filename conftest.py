import datetime
import logging
import logging.handlers
from logging.handlers import RotatingFileHandler
from pathlib import Path

import mysql.connector
import pytest
import requests
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.remote.webdriver import WebDriver

from hw_09.locators.locators import Selectors
from hw_09.pages.ui.appeals_page import AppealPage
from hw_09.pages.ui.companies_page import CompaniesPage
from hw_09.pages.ui.physical_persons_page import PhysicalPersonPage


def pytest_configure(config):
    config.addinivalue_line("markers", "api_test: mark a test as api test")
    config.addinivalue_line("markers", "ui_test: mark a test as ui test")
    config.addinivalue_line("markers", "xxxx: mark a test as ui test")



def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='firefox')
    parser.addoption('--url', action='store', default='paste_url')
    parser.addoption('--log_level', action='store', default="INFO")
    parser.addoption('--executor', action='store')
    parser.addoption('--browser_version', action='store')


@pytest.fixture(scope='function')
def logger(request):
    log_dir = Path(__file__).parent / 'log'
    log_dir.mkdir(exist_ok=True)
    log_level = request.config.getoption('--log_level')
    browser_name = request.config.getoption('--browser')
    logger = logging.getLogger(request.node.name)
    file_handler = RotatingFileHandler(
        str(log_dir / f'{request.node.name}({browser_name}).log'),
        maxBytes=30000000,
        backupCount=3)
    file_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info('===> Test %s started at %s' % (request.node.name, datetime.datetime.now()))

    yield logger

    logger.info('===> Test %s finished at %s' % (request.node.name, datetime.datetime.now()))

    for handler in logger.handlers:
        handler.close()
    logger.handlers.clear()


@pytest.fixture()
def browser(request, logger) -> WebDriver:
    browser_name = request.config.getoption('--browser')
    browser_version = request.config.getoption('--browser_version')
    executor = request.config.getoption('--executor')
    url = request.config.getoption('--url')

    if executor:
        if browser_name == 'chrome':
            options = ChromeOptions()
        elif browser_name == 'firefox':
            options = FirefoxOptions()
        elif browser_name == 'edge':
            options = EdgeOptions()
        else:
            raise ValueError(
                'Browser name must be "chrome", "firefox" or "edge"'
            )
        options.headless = False  # type: ignore
        capabilities = {
            'browserName': browser_name,
            'browserVersion': browser_version,
            'selenoid:options': {
                'enableVNC': True,
            },
        }
        for key, value in capabilities.items():
            options.set_capability(key, value)

        driver = webdriver.Remote(
            command_executor=f'http://{executor}:4444/wd/hub',
            options=options
        )
        driver.maximize_window()
    else:
        if browser_name == 'chrome':
            options = webdriver.ChromeOptions()
            options.add_argument("--headless=new")
            driver = webdriver.Chrome(options=options)
        elif browser_name == 'firefox':
            options = webdriver.FirefoxOptions()
            # options.add_argument("--start-maximized")
            # options.add_argument("--headless")
            driver = webdriver.Firefox(options=options)
            # driver.fullscreen_window()
        elif browser_name == 'edge':
            options = webdriver.EdgeOptions()
            options.use_chromium = True
            options.add_argument("--headless=new")
            driver = webdriver.Edge(options=options)
        else:
            raise ValueError(
                'Browser name must be "chrome", "firefox" or "edge"'
            )
    driver.get(url)
    driver.url = url
    driver.logger = logger
    driver.test_name = request.node.name

    logger.info("Browser %s v. %s started" % (browser_name, browser_version))

    yield driver
    driver.quit()


@pytest.fixture()
def authorization_token(browser):
    page = AppealPage(browser)
    page.fill_username(Selectors.ADMIN_LOGIN)
    page.fill_password(Selectors.ADMIN_PASSWORD)
    page.click_login_button()
    page.click_button_user()
    page.click_button_admin_link()
    page.click_button_connections()
    page.click_button_set_url_connections()
    page.click_button_portal()
    token = f'Bearer {page.get_token()}'
    return {'Authorization': token}


@pytest.fixture()
def login_as_admin_physical_person(browser) -> PhysicalPersonPage:
    page = PhysicalPersonPage(browser)
    page.fill_username(Selectors.ADMIN_LOGIN)
    page.fill_password(Selectors.ADMIN_PASSWORD)
    page.click_login_button()
    return page


@pytest.fixture()
def login_as_admin_companies(browser) -> CompaniesPage:
    page = CompaniesPage(browser)
    page.fill_username(Selectors.ADMIN_LOGIN)
    page.fill_password(Selectors.ADMIN_PASSWORD)
    page.click_login_button()
    return page


@pytest.fixture()
def login_as_admin_appeals(browser) -> AppealPage:
    page = AppealPage(browser)
    page.fill_username(Selectors.ADMIN_LOGIN)
    page.fill_password(Selectors.ADMIN_PASSWORD)
    page.click_login_button()
    return page


@pytest.fixture()
def delete_created_appeal(browser, request):
    page = request.getfixturevalue("login_as_admin_appeals")
    yield page
    browser.get(page.appeal_address)
    page.click_button_appeal_actions()
    page.click_button_appeal_delete()
    page.accept_allert()


@pytest.fixture()
def setup_user_db():

    db = mysql.connector.connect(
        host="paste_host_ip",
        port="paste_port",
        user="paste_username",
        password="paste_db_password",
        database="paste_db_name"
    )
    cursor = db.cursor(dictionary=True)

    first_name = 'FIТЕСТ'
    last_name = 'SUАВТО'
    second_name = 'SEТЕСТОВИЧ'
    contact_category = 'employee'
    id = 'd4795e0b-7f15-4681-9588-8e56990358b1'

    cursor.execute(f"INSERT INTO contacts (id, first_name, last_name, second_name, contact_category) VALUES ('{id}', '{first_name}', '{last_name}', '{second_name}', '{contact_category}')")
    db.commit()
    created_user_id = cursor.lastrowid

    yield db, cursor, created_user_id

    cursor.execute(f"DELETE FROM contacts WHERE id={created_user_id}")
    db.commit()
    db.close()


@pytest.fixture()
def setup_user(browser, login_as_admin_physical_person):
    page = login_as_admin_physical_person
    page.click_button_all()
    page.click_button_physical_persons()
    page.click_button_create_physical_persons()
    page.fill_surname_field()
    page.fill_first_name_field()
    page.fill_second_name_field()
    page.click_contact_category_field()
    page.click_contact_category_staff_field()
    page.click_enterprise_button()
    page.switch_to_new_window()
    page.fill_inn_field()
    page.click_enterprise_search_button()
    page.click_found_company()
    page.switch_to_main_window()
    page.fill_position_field()
    page.fill_phone_number_field()
    page.fill_email_field()
    page.click_save_and_close_button()
    user_url = page.browser.current_url
    page.click_button_user()
    page.click_logout_button()
    yield user_url, page
    browser.get(user_url)
    try:
        alert = browser.switch_to.alert
        alert.accept()
    except NoAlertPresentException:
        pass
    page.click_user_actions_button()
    page.click_delete_user_button()
    page.accept_allert()
    page.wait_for_loading_page()


@pytest.fixture()
def delete_created_user(browser, request):
    page = request.getfixturevalue("login_as_admin_physical_person")
    yield page
    page.click_user_actions_button()
    page.click_delete_user_button()
    page.accept_allert()
    page.wait_for_loading_page()


@pytest.fixture()
def session_id():
    url = 'paste_url'
    payload = {
        "method": 'login',
        "input_type": 'JSON',
        "response_type": 'JSON',
        "rest_data": '{ "user_auth": { "user_name": "paste_username", "password": "paste_password" } }'
    }
    response = requests.post(url, data=payload)
    return response.json()['id']
