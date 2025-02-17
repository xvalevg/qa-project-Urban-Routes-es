# from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time
import data
from selenium import webdriver




# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    ask_taxi_button = (By.CSS_SELECTOR, '.button.round')
    confort_tariff_button = (By.CSS_SELECTOR, 'div.tariff-picker div.tcard:nth-child(5)')
    confort_tariff_text = (By.CSS_SELECTOR, 'div.tariff-picker div.tcard:nth-child(5) div.tcard-title')
    phone_number_button = (By.CLASS_NAME, 'np-text')
    phone_field = (By.ID, 'phone')
    submit_phone_number_button = (By.XPATH, '//button[contains(text(), "Siguiente")]')
    #code for phone id
    code_for_phone_field = (By.CSS_SELECTOR, 'div.np-input div.input-container input#code')
    confirm_phone_button = (By.XPATH, '//button[contains(text(), "Confirmar")]')
    #code for card id
    card_button = (By.CLASS_NAME, 'pp-text')
    plus_card_button = (By.CLASS_NAME, 'pp-plus-container')
    card_number_field = (By.ID, 'number')
    card_code_field =  (By.CSS_SELECTOR, 'div.card-code div.card-code-input input#code')
    submit_card_button = (By.XPATH, '//button[contains(text(), "Agregar")]')
    card_close_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')
    card_field_text = (By.CSS_SELECTOR, 'div.pp-value div.pp-value-text')
    comment_field = (By.ID, 'comment')
    ask_requirements_switch = (By.CSS_SELECTOR, "div.reqs-body div:nth-child(1) div.switch")
    plus_icecream_button = (By.CSS_SELECTOR, "div.r-group div.r-group-items div:nth-child(1) div.r-counter-container div.r-counter div.counter div.counter-plus")
    ask_for_taxi = (By.CLASS_NAME, 'smart-button-secondary')
    search_car_text = (By.CLASS_NAME, 'order-header-title')
    driver_rating_info=(By.CLASS_NAME, 'order-btn-rating')



    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        WebDriverWait(self.driver,3).until(expected_conditions.visibility_of_element_located(self.from_field)).send_keys(from_address)

    def set_to(self, to_address):
         WebDriverWait(self.driver,3).until(expected_conditions.visibility_of_element_located(self.to_field)).send_keys(to_address)
       
    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)
        
    def get_from(self):
        return  WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.from_field)).get_property('value')


    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def click_ask_taxi_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.ask_taxi_button)).click()
    
    def click_confort_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.confort_tariff_button)).click()

    def get_comfort_value(self):
        return  WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.confort_tariff_text)).get_property('innerHTML')
    
    def click_phone_button(self):
        self.driver.find_element(*self.phone_number_button).click()
    
    def set_phone_number(self, phone_number):
        WebDriverWait(self.driver,3).until(expected_conditions.visibility_of_element_located(self.phone_field)).send_keys(phone_number)
    
    def click_submit_phone_number(self):
        self.driver.find_element(*self.submit_phone_number_button).click()
    
    def set_code_for_phone(self):
        time.sleep(2)
        codeFromPhone = retrieve_phone_code(driver=self.driver)
        print(codeFromPhone)
        WebDriverWait(self.driver,3).until(expected_conditions.visibility_of_element_located(self.code_for_phone_field)).send_keys(codeFromPhone)
    
    def set_confirm_code(self):
        self.driver.find_element(*self.confirm_phone_button).click()
    
    def get_phone_number(self):
        return  WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.phone_number_button)).get_property('innerHTML')

    def click_submit_card_number(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.card_button)).click()
    

    def click_add_card(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.plus_card_button)).click()

    def set_card_number(self, card_number):
        card_input =  WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.card_number_field))
        card_input.send_keys(card_number)
        card_input.send_keys(Keys.TAB)
    
    def set_code_card_number(self, code_card_number):
        self.driver.find_element(*self.card_code_field).send_keys(code_card_number)
    
    def click_add_card_button(self):
        self.driver.find_element(*self.submit_card_button).click()

    def click_close_cards_modal(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.card_close_button)).click()
        time.sleep(2)

    def get_card_text(self):
        return  WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.card_field_text)).get_property('innerHTML')

    def set_message_for_driver(self, message):
        WebDriverWait(self.driver,3).until(expected_conditions.visibility_of_element_located(self.comment_field)).send_keys(message)    

    def get_message_for_drive(self):
        return  WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.comment_field)).get_property('value')
    
    
    def ask_for_requirements(self):
        element =  WebDriverWait(self.driver,3).until(expected_conditions.visibility_of_element_located(self.ask_requirements_switch))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.find_element(*self.ask_requirements_switch).click()
    
    def ask_for_two_icecreams(self):
        element =  WebDriverWait(self.driver,3).until(expected_conditions.visibility_of_element_located(self.plus_icecream_button))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.find_element(*self.plus_icecream_button).click()
        self.driver.find_element(*self.plus_icecream_button).click()
    
    def click_ask_for_taxi(self):
        self.driver.find_element(*self.ask_for_taxi).click()

    def get_search_car_text(self):
        return  WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.search_car_text)).get_property('innerHTML')

    def get_driver_rating_info(self):
        return WebDriverWait(self.driver,60).until(expected_conditions.presence_of_element_located(self.driver_rating_info)).get_property('innerHTML')



class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("perfLoggingPrefs", {'enableNetwork': True, 'enablePage': True})
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
    
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome(desired_capabilities=capabilities)

    def set_route(self, routes_page):   
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)

    def test_set_route(self):
        address_from = data.address_from
        address_to = data.address_to
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        self.set_route(routes_page)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def select_comfort(self, routes_page):
        self.set_route(routes_page)
        routes_page.click_ask_taxi_button()
        routes_page.click_confort_button()

    def test_select_comfort(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        self.select_comfort(routes_page) 
        assert routes_page.get_comfort_value() == "Comfort"
        
    def add_phone_numner(self, routes_page):
        self.select_comfort(routes_page)
        routes_page.click_phone_button()
        routes_page.set_phone_number(data.phone_number)
        routes_page.click_submit_phone_number()
        routes_page.set_code_for_phone()
        routes_page.set_confirm_code()

    def test_add_phone_number(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        self.add_phone_numner(routes_page)
        assert routes_page.get_phone_number() == data.phone_number
        
    def add_card_number(self, routes_page):
        self.add_phone_numner(routes_page)
        routes_page.click_submit_card_number()
        routes_page.click_add_card()
        routes_page.set_card_number(data.card_number)
        routes_page.set_code_card_number(data.card_code)
        routes_page.click_add_card_button()
        routes_page.click_close_cards_modal()
    
    def test_add_card_number(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        self.add_card_number(routes_page)
        assert routes_page.get_card_text() == 'Tarjeta'
        
    def add_extra_info(self, routes_page):
        self.add_card_number(routes_page)
        routes_page.set_message_for_driver(data.message_for_driver)
        routes_page.ask_for_requirements()
        routes_page.ask_for_two_icecreams()

    def test_add_extra_info(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        self.add_extra_info(routes_page)
        assert routes_page.get_message_for_drive() == data.message_for_driver

    def ask_for_taxi(self, routes_page):
        self.add_extra_info(routes_page)
        routes_page.click_ask_for_taxi()
        
    
    def test_ask_for_taxi(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        self.ask_for_taxi(routes_page)
        assert routes_page.get_search_car_text() == 'Buscar automóvil'
        driver_rating_info = routes_page.get_driver_rating_info()
        assert driver_rating_info != ''




    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

