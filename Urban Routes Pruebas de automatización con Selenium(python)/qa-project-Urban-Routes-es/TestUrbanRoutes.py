import time
import data
from selenium import webdriver
import UrbanRoutesPage
class TestUrbanRoutes:

    driver = None


    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    #TEST 1 Configurar la dirección
    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        self.driver.implicitly_wait(3)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to #COMO CONFIRMO Q NO ES LA PALABRA EQUIVOCADA
    #TEST 2 Seleccionar la tarifa Comfort.
    def test_set_confort(self):
        routes_page=UrbanRoutesPage.UrbanRoutesPage(self.driver)
        routes_page.set_confort()
        assert routes_page.confort_active() == True

    #TEST 3 Rellenar el número de teléfono
    def test_set_phone_number(self):
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        phone_number = data.phone_number
        routes_page.set_phone_number(phone_number)
        print(phone_number)
        assert routes_page.get_add_number() == phone_number



    #TEST 4 Agregar una tarjeta de crédito
    def test_set_credit_card(self):
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        card_number = data.card_number
        card_code = data.card_code
        routes_page.set_credit_card(card_number,card_code)
        print(card_number)
        assert routes_page.get_text() == "Tarjeta"
        assert routes_page.get_icon() == "card"

    #TEST 5 escribir un mensaje para el controlador
    def test_sms_driver(self):
        message_for_driver = data.message_for_driver
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        routes_page.sms_driver(message_for_driver)
        assert routes_page.verification_sms() == message_for_driver

    #TEST 6 Pedir una manta y pañuelos
    def test_order_blanjet_scareves(self):
        self.driver.implicitly_wait(4)
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        routes_page.order_blanjet_scareves()
        #assert routes_page.verification_blanket_scarves() == True

    #TEST 7 Pedir 2 helados

    def test_order_icecream(self):
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        routes_page.order_icecream()
        assert routes_page.verification_icecream() == '2'
    #TEST 8 Aparece el modal para buscar un taxi
    def test_click_smart_button(self):
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        routes_page.click_smart_button()
        assert routes_page.verification_smart_button() == True


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
