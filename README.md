**Проектная работа: "Автоматизация тестирования"**

Автор: Виталий Личинин

**Оглавление**
- [Цели](#цели)
- [Используемые библиотеки](#используемые-библиотеки)
- [Структура проекта](#структура-проекта)
- [Запуск проекта](#запуск-проекта)

- [Результаты выполнения тестов](#результаты-выполнения-тестов)
  - [Результаты выполнения тестов (локально)](#результаты-выполнения-тестов-локально)
  - [Результаты выполнения тестов (selenoid)](#результаты-выполнения-тестов-selenoid)



***
### Цели.

- Автоматизация тест-кейсов
- Возможность запуска на удаленной машине
- Построение отчетности через Allure
- Внедрение логирования для критически важного функционала
- В проекте необходимо использовать весь пройденный материал
- Для каждого элемента UI (за действенного в тесте) необходимо сделать проверку (столбец "Ожидаемый результат"), проверка должна быть в отдельном тесте.
***
### Используемые библиотеки.
poetry
python = "3.10"
pytest = "8.2.1"
pylint = "3.2.2"
requests = "2.32.2"
selenium = "4.21.0"
allure-pytest = "2.13.5"
faker = "25.3.0"
pytest-xdist = "3.6.1"
pydantic = "2.7.3"
mysql-connector-python = "8.4.0"
***
### Структура проекта.
```
hw_09                                                                 
├─ allure-report                                                      
├─ allure-results                                                     
├─ locators                                                           
│  └─ locators.py
├─ logs                                                           
├─ pages                                                              
│  ├─ api                                                             
│  │  ├─ appeals_api.py                                               
│  │  ├─ base_api.py                                                  
│  │  ├─ chat_message_api.py                                          
│  │  ├─ lead_api.py                                                  
│  │  ├─ organizations_list_api.py                                    
│  │  └─ user_list_api.py                                                                                                 
│  └─ ui                                                              
│     ├─ appeals_page.py                                              
│     ├─ base_page.py                                                 
│     ├─ companies_page.py                                            
│     └─ physical_persons_page.py                                                                                       
├─ schema                                                             
│  └─ schemas.py                                                      
├─ tests                                                              
│  ├─ test_api                                                        
│  │  ├─ test_api_appeals.py                                          
│  │  ├─ test_api_lead.py                                             
│  │  ├─ test_api_organizations_list.py                               
│  │  ├─ test_api_user_list.py                                        
│  │  └─ test_chat_message.py                                                                                           
│  └─ test_ui                                                         
│     ├─ test_appeals.py                                              
│     ├─ test_companies.py                                            
│     └─ test_physical_persons.py                                                                                       
├─ conftest.py                                                        
├─ Dockerfile                                                         
├─ poetry.lock                                                        
├─ pyproject.toml                                                     
├─ pytest.ini                                                         
└─ README.md                                                                                                                  

```
* Папка **/allure-report**: Сгенерированный Allure-отчет.

* Папка **/allure-results**: Файлы для генерации Allure-отчета.

* Папка **/locators**:
  * **locators.py**: Содержит класс с локаторами.

* Папка **/logs**: Лог работы.

* Папка **/pages**:
    * Папка **/api**:
        * **appeals_api.py**: Класс PageObject API для модуля "Обращения".
        * **base_api.py**: Базовый класс PageObject API, содержащий общие методы и свойства для всех модулей.
        * **chat_message_api.py**: Класс PageObject API для модуля "Сообщения".
        * **lead_api.py**: Класс PageObject API для модуля "Пользователи"".
        * **organizations_list_api.py**: Класс PageObject API для модуля "Организации".
        * **user_list_api.py**: Класс PageObject API для страницы "Физические лица".
    * Папка **/ui**:
        * **appeals_page.py**: Класс PageObject для страницы "Обращения".
        * **base_page.py**: Базовый класс PageObject , содержащий общие методы и свойства для всех страниц.
        * **companies_page.py**: Класс PageObject для страницы "Организации".
        * **physical_persons_page.py**: Класс PageObject для модуля "Физические лица"".

* Папка **/schema**:
  * **schema.py**: Содержит класс со схемами валидации api-запросов.

* Папка **/tests**:
    * Папка **/test_api**:
        * **test_api_appeals.py**: Автотесты API для модуля "Обращения".
        * **test_api_lead.py**: Автотесты API для модуля "Пользователи"".
        * **test_api_organizations_list.py**: Автотесты API для модуля "Организации".
        * **test_api_user_list.py**: Автотесты API для модуля "Пользователи"".
        * **test_chat_message.py**: Автотесты API для модуля "Сообщения".
    * Папка **/test_ui**:
        * **test_appeals.py**: Автотесты UI для страницы "Обращения".
        * **test_companies.py**: Автотесты UI для страницы "Организации".
        * **test_physical_persons.py**: Автотесты UI для модуля "Физические лица"".

* **conftest.py**: Файл с общими фикстурами для тестов, включая настройку браузера, логгера, тестовых данных и другой общей функциональности.
    Содержит следующие настройки и фикстуры:
    - **pytest_configure**: Добавляет два кастомных mark для тестов api_test и ui_test.
    - **pytest_addoption**: Добавляет команды для запуска тестов с различными параметрами, такими как выбор браузера, URL-адрес, уровень логирования, исполнитель (Selenoid) и версия браузера.
    - **logger**: Настраивает логгер RotatingFileHandler для записи информации о ходе выполнения тестов в файл. Создает файл логов с ограничением размера и количества бэкапов. Уровень логирования задается параметром --log_level.
    - **browser**: Настраивает и запускает веб-драйвер для выбранного браузера (Chrome, Firefox или Edge) в зависимости от параметров запуска. Поддерживает запуск тестов локально или в Selenoid.
    - **authorization_token**: Получает токен авторизации для GET-запросов.
    - **login_as_admin_physical_person(browser)**: Фикстура готовит PhysicalPersonPage объект с авторизованной главной страницей проекта.
    - **login_as_admin_companies(browser)**: Фикстура готовит CompaniesPage объект с авторизованной главной страницей проекта.
    - **login_as_admin_appeals(browser)**: Фикстура готовит AppealPage объект с авторизованной главной страницей проекта.
    - **delete_created_appeal(browser, request)**: Фикстура удаляет созданнное во время теста Обращение.
    - **setup_user_db()**: Фикстура создает пользователя для теста. После выболнения теста пользователь удаляется. Процесс выполняется через запросы в БД.
    - **setup_user(browser, login_as_admin_physical_person)**: Фикстура создает пользователя для теста. После выболнения теста пользователь удаляется. Процесс выполняется через UI.
    - **delete_created_user(browser, request)**: Фикстура удаляет созданного во время теста Пользователя.
    - **session_id()**: Фикстура получает session_id, необходимый для POST-запросов.
* **Dockerfile**: Конфигурация для создания Docker-образа проекта.
* **poetry.lock**, **pyproject.toml**: Файл конфигурации виртуального окружения Poetry.
* **pytest.ini**: Файл конфигурации для pytest, содержащий настройки для запуска тестов.
* **README.md**: Описание проекта.

***
### Запуск проекта.
1. Скачать репозиторий.
2. Установить Poetry:
    ```
    pip install poetry
    ```
3. Развернуть виртуальное окружение:
    ```
    poetry install
    ```
4. Запустить pytest:
    В проекте в pytest.ini преднастроено два варианта запуска pytest, для выбора запуска раскомментировать нужную строку:
        1) ```addopts = -n 1 -vv --alluredir=hw_09/allure-results --executor=192.168.1.117 --browser='chrome' --browser_version='100'```
        Запуск всех тестов в 1 поток на внешней машине (Selenoid), браузер Chrome v.100
        2) ```addopts = -n 1 -vv```
        Запуск тестов в 1 поток на локальной машине.
    Для запуска только API-тестов добавить флаг ```-m "api_test"```
    Для запуска только UI-тестов добавить флаг ```-m "ui_test"```
5. Для создания Docker-образа выполнить и з папки с проектом:
    ```docker build -t testproject .```
6. Для запуска тестов в образе выполнить:
    ```docker run -v /${PWD}/allure-results/:/hw_09/allure-results testproject```
    Команда запустит образ с проектом, смонтриует папку с отчетами allure на локальный диск, выполнит все тесты.
7. Для запуска только API-тестов в образе выполнить:
    ```docker run -v /${PWD}/allure-results/:/hw_09/allure-results testproject -m "api_test"```
8. Для запуска только UI-тестов в образе выполнить:
    ```docker run -v /${PWD}/allure-results/:/hw_09/allure-results testproject -m "Ui_test"```


### Результат выполнения тестов.
addopts = -n 1 -vv --alluredir=hw_09/allure-results --executor=192.168.1.117 --browser='chrome' --browser_version='100'
```
$ pytest
========================================================================================================= test session starts =========================================================================================================
platform win32 -- Python 3.10.6, pytest-8.2.1, pluggy-1.5.0 -- C:\Users\Lichi\AppData\Local\pypoetry\Cache\virtualenvs\hw-09-Zsb4Md5C-py3.10\Scripts\python.exe
cachedir: .pytest_cache
rootdir: E:\ITFB\DEV\vitaly-lichinin\hw_09
configfile: pytest.ini
plugins: allure-pytest-2.13.5, Faker-25.3.0, xdist-3.6.1
1 worker [91 items]    
scheduling tests via LoadScheduling

tests/test_api/test_api_appeals.py::test_status_code 
[gw0] [  1%] PASSED tests/test_api/test_api_appeals.py::test_status_code 
tests/test_api/test_api_appeals.py::test_post_created_appeal_subject 
[gw0] [  2%] PASSED tests/test_api/test_api_appeals.py::test_post_created_appeal_subject 
tests/test_api/test_api_appeals.py::test_post_created_appeal_short_name 
[gw0] [  3%] PASSED tests/test_api/test_api_appeals.py::test_post_created_appeal_short_name 
tests/test_api/test_api_appeals.py::test_post_created_appeal_description 
[gw0] [  4%] PASSED tests/test_api/test_api_appeals.py::test_post_created_appeal_description 
tests/test_api/test_api_appeals.py::test_post_created_appeal_date_entered 
[gw0] [  5%] PASSED tests/test_api/test_api_appeals.py::test_post_created_appeal_date_entered 
tests/test_api/test_api_appeals.py::test_comparse_subject_from_vp_and_db 
[gw0] [  6%] PASSED tests/test_api/test_api_appeals.py::test_comparse_subject_from_vp_and_db 
tests/test_api/test_api_appeals.py::test_comparse_short_name_from_vp_and_db 
[gw0] [  7%] PASSED tests/test_api/test_api_appeals.py::test_comparse_short_name_from_vp_and_db 
tests/test_api/test_api_appeals.py::test_comparse_description_from_vp_and_db 
[gw0] [  8%] PASSED tests/test_api/test_api_appeals.py::test_comparse_description_from_vp_and_db 
tests/test_api/test_api_appeals.py::test_comparse_date_entered_from_vp_and_db 
[gw0] [  9%] PASSED tests/test_api/test_api_appeals.py::test_comparse_date_entered_from_vp_and_db 
tests/test_api/test_api_lead.py::test_status_code 
[gw0] [ 10%] PASSED tests/test_api/test_api_lead.py::test_status_code 
tests/test_api/test_api_lead.py::test_post_created_lead_last_name
[gw0] [ 12%] PASSED tests/test_api/test_api_lead.py::test_post_created_lead_last_name 
tests/test_api/test_api_lead.py::test_post_created_lead_second_name
[gw0] [ 13%] PASSED tests/test_api/test_api_lead.py::test_post_created_lead_second_name 
tests/test_api/test_api_lead.py::test_post_created_lead_vp_date_modified
[gw0] [ 14%] PASSED tests/test_api/test_api_lead.py::test_post_created_lead_vp_date_modified 
tests/test_api/test_api_lead.py::test_post_created_lead_phone_mobile
[gw0] [ 15%] PASSED tests/test_api/test_api_lead.py::test_post_created_lead_phone_mobile 
tests/test_api/test_api_lead.py::test_post_created_lead_email
[gw0] [ 16%] PASSED tests/test_api/test_api_lead.py::test_post_created_lead_email 
tests/test_api/test_api_lead.py::test_post_created_lead_acc_portal_inn
[gw0] [ 17%] PASSED tests/test_api/test_api_lead.py::test_post_created_lead_acc_portal_inn 
tests/test_api/test_api_lead.py::test_comparse_inn_from_vp_and_db
[gw0] [ 18%] PASSED tests/test_api/test_api_lead.py::test_comparse_inn_from_vp_and_db 
tests/test_api/test_api_lead.py::test_comparse_last_name_from_vp_and_db
[gw0] [ 19%] PASSED tests/test_api/test_api_lead.py::test_comparse_last_name_from_vp_and_db 
tests/test_api/test_api_lead.py::test_comparse_vp_date_modified_from_vp_and_db 
[gw0] [ 20%] PASSED tests/test_api/test_api_lead.py::test_comparse_vp_date_modified_from_vp_and_db 
tests/test_api/test_api_lead.py::test_comparse_phone_mobile_from_vp_and_db
[gw0] [ 21%] PASSED tests/test_api/test_api_lead.py::test_comparse_phone_mobile_from_vp_and_db 
tests/test_api/test_api_organizations_list.py::test_status_code
[gw0] [ 23%] PASSED tests/test_api/test_api_organizations_list.py::test_status_code 
tests/test_api/test_api_organizations_list.py::test_get_limit_organizations_list 
[gw0] [ 24%] PASSED tests/test_api/test_api_organizations_list.py::test_get_limit_organizations_list 
tests/test_api/test_api_organizations_list.py::test_get_ofset_organizations_list 
[gw0] [ 25%] PASSED tests/test_api/test_api_organizations_list.py::test_get_ofset_organizations_list 
tests/test_api/test_api_organizations_list.py::test_updated_at_from_organizations_list 
[gw0] [ 26%] PASSED tests/test_api/test_api_organizations_list.py::test_updated_at_from_organizations_list 
tests/test_api/test_api_organizations_list.py::test_updated_at_to_organizations_list 
[gw0] [ 27%] PASSED tests/test_api/test_api_organizations_list.py::test_updated_at_to_organizations_list 
tests/test_api/test_api_organizations_list.py::test_comparse_id_from_vp_and_db 
[gw0] [ 28%] PASSED tests/test_api/test_api_organizations_list.py::test_comparse_id_from_vp_and_db 
tests/test_api/test_api_organizations_list.py::test_comparse_title_from_vp_and_db 
[gw0] [ 29%] PASSED tests/test_api/test_api_organizations_list.py::test_comparse_title_from_vp_and_db 
tests/test_api/test_api_organizations_list.py::test_comparse_region_id_from_vp_and_db 
[gw0] [ 30%] PASSED tests/test_api/test_api_organizations_list.py::test_comparse_region_id_from_vp_and_db 
tests/test_api/test_api_organizations_list.py::test_comparse_site_url_from_vp_and_db 
[gw0] [ 31%] PASSED tests/test_api/test_api_organizations_list.py::test_comparse_site_url_from_vp_and_db 
tests/test_api/test_api_organizations_list.py::test_comparse_baseyear_from_vp_and_db 
[gw0] [ 32%] PASSED tests/test_api/test_api_organizations_list.py::test_comparse_baseyear_from_vp_and_db 
tests/test_api/test_api_user_list.py::test_status_code 
[gw0] [ 34%] PASSED tests/test_api/test_api_user_list.py::test_status_code 
tests/test_api/test_api_user_list.py::test_param_limit_user_list 
[gw0] [ 35%] PASSED tests/test_api/test_api_user_list.py::test_param_limit_user_list 
tests/test_api/test_api_user_list.py::test_param_ofset_user_list 
[gw0] [ 36%] PASSED tests/test_api/test_api_user_list.py::test_param_ofset_user_list 
tests/test_api/test_api_user_list.py::test_param_updated_at_from_user_list 
[gw0] [ 37%] PASSED tests/test_api/test_api_user_list.py::test_param_updated_at_from_user_list 
tests/test_api/test_api_user_list.py::test_updated_at_to_user_list 
[gw0] [ 38%] PASSED tests/test_api/test_api_user_list.py::test_updated_at_to_user_list 
tests/test_api/test_api_user_list.py::test_comparse_id_from_vp_and_db 
[gw0] [ 39%] PASSED tests/test_api/test_api_user_list.py::test_comparse_id_from_vp_and_db 
tests/test_api/test_api_user_list.py::test_comparse_phone_number_from_vp_and_db 
[gw0] [ 40%] PASSED tests/test_api/test_api_user_list.py::test_comparse_phone_number_from_vp_and_db 
tests/test_api/test_api_user_list.py::test_comparse_position_from_vp_and_db 
[gw0] [ 41%] PASSED tests/test_api/test_api_user_list.py::test_comparse_position_from_vp_and_db 
tests/test_api/test_api_user_list.py::test_comparse_last_name_from_vp_and_db 
[gw0] [ 42%] PASSED tests/test_api/test_api_user_list.py::test_comparse_last_name_from_vp_and_db 
tests/test_api/test_api_user_list.py::test_comparse_first_name_from_vp_and_db 
[gw0] [ 43%] PASSED tests/test_api/test_api_user_list.py::test_comparse_first_name_from_vp_and_db 
tests/test_api/test_chat_message.py::test_status_code 
[gw0] [ 45%] PASSED tests/test_api/test_chat_message.py::test_status_code 
tests/test_api/test_chat_message.py::test_post_created_appeal_subject
[gw0] [ 46%] SKIPPED tests/test_api/test_chat_message.py::test_post_created_appeal_subject 
tests/test_ui/test_appeals.py::test_button_administration
[gw0] [ 47%] PASSED tests/test_ui/test_appeals.py::test_button_administration 
tests/test_ui/test_appeals.py::test_button_config_settings 
[gw0] [ 48%] PASSED tests/test_ui/test_appeals.py::test_button_config_settings 
tests/test_ui/test_appeals.py::test_button_log_view 
[gw0] [ 49%] PASSED tests/test_ui/test_appeals.py::test_button_log_view 
tests/test_ui/test_appeals.py::test_button_control_point 
[gw0] [ 50%] PASSED tests/test_ui/test_appeals.py::test_button_control_point 
tests/test_ui/test_appeals.py::test_header_button_all 
[gw0] [ 51%] PASSED tests/test_ui/test_appeals.py::test_header_button_all 
tests/test_ui/test_appeals.py::test_button_appeals 
[gw0] [ 52%] PASSED tests/test_ui/test_appeals.py::test_button_appeals 
tests/test_ui/test_appeals.py::test_button_create_new_appeal 
[gw0] [ 53%] PASSED tests/test_ui/test_appeals.py::test_button_create_new_appeal 
tests/test_ui/test_appeals.py::test_button_select_contact 
[gw0] [ 54%] PASSED tests/test_ui/test_appeals.py::test_button_select_contact 
tests/test_ui/test_appeals.py::test_fill_fio_field 
[gw0] [ 56%] PASSED tests/test_ui/test_appeals.py::test_fill_fio_field 
tests/test_ui/test_appeals.py::test_button_find_contact 
[gw0] [ 57%] PASSED tests/test_ui/test_appeals.py::test_button_find_contact 
tests/test_ui/test_appeals.py::test_click_on_finded_contact 
[gw0] [ 58%] PASSED tests/test_ui/test_appeals.py::test_click_on_finded_contact 
tests/test_ui/test_appeals.py::test_select_appeal_category_fck 
[gw0] [ 59%] PASSED tests/test_ui/test_appeals.py::test_select_appeal_category_fck 
tests/test_ui/test_appeals.py::test_select_appeal_subtype_consult 
[gw0] [ 60%] PASSED tests/test_ui/test_appeals.py::test_select_appeal_subtype_consult 
tests/test_ui/test_appeals.py::test_select_appeal_theme_consult_tech 
[gw0] [ 61%] PASSED tests/test_ui/test_appeals.py::test_select_appeal_theme_consult_tech 
tests/test_ui/test_appeals.py::test_select_appeal_subtheme_consult_fck_other 
[gw0] [ 62%] PASSED tests/test_ui/test_appeals.py::test_select_appeal_subtheme_consult_fck_other 
tests/test_ui/test_appeals.py::test_fill_appeal_description 
[gw0] [ 63%] FAILED tests/test_ui/test_appeals.py::test_fill_appeal_description 
tests/test_ui/test_appeals.py::test_click_connect_type 
[gw0] [ 64%] PASSED tests/test_ui/test_appeals.py::test_click_connect_type 
tests/test_ui/test_appeals.py::test_click_connect_type_email 
[gw0] [ 65%] PASSED tests/test_ui/test_appeals.py::test_click_connect_type_email 
tests/test_ui/test_appeals.py::test_click_connect_type_anonymus_phone 
[gw0] [ 67%] PASSED tests/test_ui/test_appeals.py::test_click_connect_type_anonymus_phone 
tests/test_ui/test_appeals.py::test_select_user_email 
[gw0] [ 68%] PASSED tests/test_ui/test_appeals.py::test_select_user_email 
tests/test_ui/test_appeals.py::test_fill_anonymus_phone 
[gw0] [ 69%] PASSED tests/test_ui/test_appeals.py::test_fill_anonymus_phone 
tests/test_ui/test_appeals.py::test_open_log_page 
[gw0] [ 70%] PASSED tests/test_ui/test_appeals.py::test_open_log_page 
tests/test_ui/test_appeals.py::test_check_anonymus 
[gw0] [ 71%] PASSED tests/test_ui/test_appeals.py::test_check_anonymus 
tests/test_ui/test_appeals.py::test_save_appeal 
[gw0] [ 72%] PASSED tests/test_ui/test_appeals.py::test_save_appeal 
tests/test_ui/test_appeals.py::test_create_appeal_by_admin_as_fl 
[gw0] [ 73%] PASSED tests/test_ui/test_appeals.py::test_create_appeal_by_admin_as_fl 
tests/test_ui/test_appeals.py::test_create_appeal_by_fl_with_lk 
[gw0] [ 74%] PASSED tests/test_ui/test_appeals.py::test_create_appeal_by_fl_with_lk 
tests/test_ui/test_appeals.py::test_create_appeal_by_anonymus 
[gw0] [ 75%] PASSED tests/test_ui/test_appeals.py::test_create_appeal_by_anonymus 
tests/test_ui/test_companies.py::test_header_button_all 
[gw0] [ 76%] PASSED tests/test_ui/test_companies.py::test_header_button_all 
tests/test_ui/test_companies.py::test_button_companies 
[gw0] [ 78%] PASSED tests/test_ui/test_companies.py::test_button_companies 
tests/test_ui/test_companies.py::test_button_create_company 
[gw0] [ 79%] PASSED tests/test_ui/test_companies.py::test_button_create_company 
tests/test_ui/test_companies.py::test_inn_field 
[gw0] [ 80%] PASSED tests/test_ui/test_companies.py::test_inn_field 
tests/test_ui/test_companies.py::test_get_data_from_vp 
[gw0] [ 81%] SKIPPED tests/test_ui/test_companies.py::test_get_data_from_vp
tests/test_ui/test_companies.py::test_phone_field
[gw0] [ 82%] PASSED tests/test_ui/test_companies.py::test_phone_field 
tests/test_ui/test_physical_persons.py::test_header_button_all 
[gw0] [ 83%] PASSED tests/test_ui/test_physical_persons.py::test_header_button_all 
tests/test_ui/test_physical_persons.py::test_button_physical_persons 
[gw0] [ 84%] PASSED tests/test_ui/test_physical_persons.py::test_button_physical_persons 
tests/test_ui/test_physical_persons.py::test_button_create_physical_persons 
[gw0] [ 85%] PASSED tests/test_ui/test_physical_persons.py::test_button_create_physical_persons 
tests/test_ui/test_physical_persons.py::test_surname_field 
[gw0] [ 86%] PASSED tests/test_ui/test_physical_persons.py::test_surname_field 
tests/test_ui/test_physical_persons.py::test_first_name_field 
[gw0] [ 87%] PASSED tests/test_ui/test_physical_persons.py::test_first_name_field 
tests/test_ui/test_physical_persons.py::test_second_name_field 
[gw0] [ 89%] PASSED tests/test_ui/test_physical_persons.py::test_second_name_field 
tests/test_ui/test_physical_persons.py::test_contact_category_field 
[gw0] [ 90%] PASSED tests/test_ui/test_physical_persons.py::test_contact_category_field 
tests/test_ui/test_physical_persons.py::test_enterpsrise_button 
[gw0] [ 91%] PASSED tests/test_ui/test_physical_persons.py::test_enterpsrise_button 
tests/test_ui/test_physical_persons.py::test_inn_field 
[gw0] [ 92%] PASSED tests/test_ui/test_physical_persons.py::test_inn_field 
tests/test_ui/test_physical_persons.py::test_search_enterprise_by_inn 
[gw0] [ 93%] PASSED tests/test_ui/test_physical_persons.py::test_search_enterprise_by_inn 
tests/test_ui/test_physical_persons.py::test_select_found_company 
[gw0] [ 94%] PASSED tests/test_ui/test_physical_persons.py::test_select_found_company 
tests/test_ui/test_physical_persons.py::test_position_field 
[gw0] [ 95%] PASSED tests/test_ui/test_physical_persons.py::test_position_field 
tests/test_ui/test_physical_persons.py::test_phone_number_field 
[gw0] [ 96%] PASSED tests/test_ui/test_physical_persons.py::test_phone_number_field 
tests/test_ui/test_physical_persons.py::test_email_field 
[gw0] [ 97%] PASSED tests/test_ui/test_physical_persons.py::test_email_field 
tests/test_ui/test_physical_persons.py::test_save_and_close_button 
[gw0] [ 98%] PASSED tests/test_ui/test_physical_persons.py::test_save_and_close_button 
tests/test_ui/test_physical_persons.py::test_create_physical_person 
[gw0] [100%] PASSED tests/test_ui/test_physical_persons.py::test_create_physical_person 

============================================================================================================== FAILURES =============================================================================================================== 
____________________________________________________________________________________________________ test_fill_appeal_description _____________________________________________________________________________________________________ 
[gw0] win32 -- Python 3.10.6 C:\Users\Lichi\AppData\Local\pypoetry\Cache\virtualenvs\hw-09-Zsb4Md5C-py3.10\Scripts\python.exe

login_as_admin_appeals = <hw_09.pages.ui.appeals_page.AppealPage object at 0x00000198AB8981C0>

    @allure.epic('FCK project')
    @allure.suite('UI tests')
    @allure.feature('Страница работы с обращениями')
    @allure.title('Проверка заполнения описания обращения')
    @pytest.mark.ui_test
    def test_fill_appeal_description(login_as_admin_appeals):
        page = login_as_admin_appeals
        page.click_button_all()
        page.click_button_appeals()
        page.click_button_create_new_appeal()
>       page.fill_appeal_description()

tests\test_ui\test_appeals.py:241:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pages\ui\appeals_page.py:120: in fill_appeal_description
    iframe = self.get_element(Selectors.DESCRIPTION_IFRAME)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <hw_09.pages.ui.appeals_page.AppealPage object at 0x00000198AB8981C0>, locator = ('css selector', '.mceIframeContainer > iframe'), timeout = 3

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
>           raise
E           RuntimeError: No active exception to reraise

pages\ui\base_page.py:29: RuntimeError
--------------------------------------------------------------------------------------------------------- Captured log setup ---------------------------------------------------------------------------------------------------------- 
INFO     test_fill_appeal_description:conftest.py:51 ===> Test test_fill_appeal_description started at 2024-06-20 00:55:08.821287
INFO     test_fill_appeal_description:conftest.py:121 Browser chrome v. 100 started
INFO     test_fill_appeal_description:base_page.py:18 * Get element "('id', 'user_name')"
INFO     test_fill_appeal_description:base_page.py:18 * Get element "('id', 'username_password')"
INFO     test_fill_appeal_description:base_page.py:18 * Get element "('id', 'bigbutton')"
---------------------------------------------------------------------------------------------------------- Captured log call ---------------------------------------------------------------------------------------------------------- 
INFO     test_fill_appeal_description:base_page.py:18 * Get element "('id', 'grouptab_1')"
INFO     test_fill_appeal_description:base_page.py:18 * Get element "('link text', 'Обращения')"
INFO     test_fill_appeal_description:base_page.py:18 * Get element "('class name', 'suitepicon-action-create')"
INFO     test_fill_appeal_description:base_page.py:18 * Get element "('css selector', '.mceIframeContainer > iframe')"
ERROR    test_fill_appeal_description:base_page.py:28 Error: element not found!
NoneType: None
-------------------------------------------------------------------------------------------------------- Captured log teardown -------------------------------------------------------------------------------------------------------- 
INFO     test_fill_appeal_description:conftest.py:55 ===> Test test_fill_appeal_description finished at 2024-06-20 00:55:32.479679
========================================================================================================== warnings summary =========================================================================================================== 
tests/test_api/test_api_appeals.py: 9 warnings
tests/test_api/test_api_lead.py: 11 warnings
tests/test_api/test_chat_message.py: 1 warning
  C:\Users\Lichi\AppData\Local\pypoetry\Cache\virtualenvs\hw-09-Zsb4Md5C-py3.10\lib\site-packages\pydantic\main.py:1115: PydanticDeprecatedSince20: The `parse_obj` method is deprecated; use `model_validate` instead. Deprecated in Pydantic V2.0 to be removed in V3.0. See Pydantic V2 Migration Guide at https://errors.pydantic.dev/2.7/migration/
    warnings.warn(

tests/test_api/test_api_organizations_list.py: 10 warnings
tests/test_api/test_api_user_list.py: 10 warnings
  C:\Users\Lichi\AppData\Local\pypoetry\Cache\virtualenvs\hw-09-Zsb4Md5C-py3.10\lib\site-packages\urllib3\connectionpool.py:1103: InsecureRequestWarning: Unverified HTTPS request is being made to host 'xn--e1atd.xn--b1aedfedwqbdfbnzkf0oe.xn--p1ai'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
======================================================================================================= short test summary info ======================================================================================================= 
FAILED tests/test_ui/test_appeals.py::test_fill_appeal_description - RuntimeError: No active exception to reraise
================================================================================== 1 failed, 88 passed, 2 skipped, 41 warnings in 1892.27s (0:31:32) ================================================================================== 
```