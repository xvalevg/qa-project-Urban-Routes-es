import data
from selenium import webdriver

from main import UrbanRoutesPage


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("perfLoggingPrefs", {'enableNetwork': True, 'enablePage': True})
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
    
    # def setup_class(cls):
    #     # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
    #     from selenium.webdriver import DesiredCapabilities
    #     capabilities = DesiredCapabilities.CHROME
    #     capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
    #     cls.driver = webdriver.Chrome(desired_capabilities=capabilities)

    def set_route(self, routes_page):   
        #NO ES UN TEST
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
        #NO ES UN TEST
        self.set_route(routes_page)
        routes_page.click_ask_taxi_button()
        routes_page.click_confort_button()

    def test_select_comfort(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        self.select_comfort(routes_page) 
        assert routes_page.get_comfort_value() == "Comfort"
        
    def add_phone_numner(self, routes_page):
        #NO ES UN TEST
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
        #NO ES UN TEST
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
        #NO ES UN TEST
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
        #NO ES UN TEST
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

