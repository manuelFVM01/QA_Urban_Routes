import data
import RetrivePhoneCode
from selenium.webdriver.common.by import By

class UrbanRoutesPage:
    #rutas
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    button_taxi = (By.CLASS_NAME,'button.round')
    tcard_confort = (By.XPATH,'//img[@alt="Comfort"]')
    tcard_confort_active =(By.XPATH, '//button[@data-for="tariff-card-4"]')
    button_add_number = (By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div')
    input_number = (By.ID,'phone')
    input2_number = (By.CLASS_NAME,'np-text')
    button_next = (By.CLASS_NAME,'button.full')
    input_code = (By.ID,'code')
    button_confirm_code = (By.CSS_SELECTOR,'.section.active>form>.buttons>:nth-child(1)')
    add_payment_method = (By.CSS_SELECTOR,'.form >.pp-button.filled > div.pp-text')
    add_card = (By.CSS_SELECTOR,'.pp-selector >.pp-row.disabled >.pp-title')
    input_card_number = (By.ID,'number')
    input_code_number  = (By.XPATH,'//div[@class="card-code-input"]/input')
    button_confirm_card = (By.XPATH,'//div[@class="pp-buttons"]/button[@type="submit"]')
    payment_text = (By.CLASS_NAME, 'pp-value-text')
    payment_icon = (By.XPATH, '//div[@class="pp-value-container"]/img')
    button_close_payment = (By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[1]/button')
    coment_field = (By.CSS_SELECTOR,'.tariff-picker.shown >.form >:nth-child(3) > div > label')
    text_for_the_driver = (By.ID, 'comment')
    order_requeriments = (By.CLASS_NAME,'reqs-head')
    button_switch_blanket_scarves = (By.CLASS_NAME,'r-sw')
    button_add_icecream = (By.CSS_SELECTOR,'.r-counter>div>.counter-plus')
    counter_icrecream = (By.CSS_SELECTOR, '.r-counter>div>.counter-value')
    smart_button = (By.CLASS_NAME, 'smart-button-wrapper')
    modal_driver = (By.CLASS_NAME,'order-header-title')



    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)  # Espera implícita




        #configurar la direccion
    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)


    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self,from_address,to_address): #esta bien aca o al final
        self.set_from(from_address)
        self.set_to(to_address)


  #seleccionar la tarifa confort


    def click_button_taxi(self):
      self.driver.find_element(*self.button_taxi).click()

    def click_tcard_confort(self):
        self.driver.find_element(*self.tcard_confort).click()



    def confort_active(self):
        return self.driver.find_element(*self.tcard_confort_active).is_displayed()


    def set_confort(self):
      self.driver.implicitly_wait(3)
      self.click_button_taxi()
      self.click_tcard_confort()
      self.confort_active()


#rellenar el numero de telefono
    def click_button_add_number(self):
      self.driver.find_element(*self.button_add_number).click()
    def click_input_add_number(self):
      self.driver.find_element(*self.input_number).click()
    def write_input_number(self,phone_number):
      self.driver.find_element(*self.input_number).send_keys(phone_number)# q numero escribir
    def click_button_next(self):
      self.driver.find_element(*self.button_next).click()
    def write_input_code(self):
      self.driver.find_element(*self.input_code).send_keys(RetrivePhoneCode.retrieve_phone_code(self.driver))

    def click_button_confirm(self):
      self.driver.find_element(*self.button_confirm_code).click()

    def set_phone_number(self, phone_number):
      self.driver.implicitly_wait(3)
      self.click_button_add_number()
      self.write_input_number(phone_number)
      self.driver.implicitly_wait(4)
      self.click_button_next()
      self.write_input_code()
      self.click_button_confirm()
      self.get_add_number()
    def get_add_number(self):
        self.driver.implicitly_wait(3)
        return self.driver.find_element(*self.input2_number).text



    #agregar tarjeta
    def click_add_payment_method(self):
        self.driver.find_element(*self.add_payment_method).click()

    def click_add_card(self):
        self.driver.find_element(*self.add_card).click()
    def set_input_card_number(self, card_number):
        self.driver.find_element(*self.input_card_number).send_keys(card_number)
    def set_input_code_number(self,code_card):
        self.driver.find_element(*self.input_code_number).send_keys(code_card)

    def click_button_confirm_card(self):
        self.driver.find_element(*self.button_confirm_card).click()


    def click_button_close_payment(self):
        self.driver.find_element(*self.button_close_payment).click()

    def get_text(self):
        return self.driver.find_element(*self.payment_text).text
    def get_icon(self):
        return self.driver.find_element(*self.payment_icon).get_attribute("alt")
    def set_credit_card(self,number_card,code_card):
        self.driver.implicitly_wait(4)
        self.click_add_payment_method()
        self.click_add_card()
        self.set_input_card_number(number_card)
        self.set_input_code_number(code_card)
        self.click_button_confirm_card()
        self.driver.implicitly_wait(3)
        self.click_button_close_payment()
        self.get_text()
        self.get_icon()

    #escribir un mensaje para el controlador
    def click_coment_field(self):
        self.driver.find_element(*self.coment_field).click()
    def get_text_for_the_driver(self, message_for_driver):
        self.driver.find_element(*self.text_for_the_driver).clear()
        self.driver.find_element(*self.text_for_the_driver).send_keys(message_for_driver)


    def verification_sms(self):
        return self.driver.find_element(*self.text_for_the_driver).get_property('value')
    def sms_driver(self,message_for_driver):
        self.driver.implicitly_wait(3)
        self.click_coment_field()
        self.get_text_for_the_driver(message_for_driver)
        self.driver.implicitly_wait(3)
        self.verification_sms()

    #pedir manta y pañuelos

    def click_button_switch_blanket_scarves(self):
        self.driver.find_element(*self.button_switch_blanket_scarves).click()


    def verification_blanket_scarves(self):
        return self.driver.find_element(*self.button_switch_blanket_scarves).is_selected()
    def order_blanjet_scareves(self):
        self.driver.implicitly_wait(3)
        self.click_button_switch_blanket_scarves()
        self.verification_blanket_scarves()

    #pedir 2 helados
    def click2_button_add_icecream(self):
        self.driver.find_element(*self.button_add_icecream).click()
        self.driver.find_element(*self.button_add_icecream).click()

    def verification_icecream(self):
        return self.driver.find_element(*self.counter_icrecream).text

    def order_icecream(self):
        self.driver.implicitly_wait(3)
        self.click2_button_add_icecream()

    #aparece el modal para buscar un taxi

    def click_smart_button(self):

        self.driver.implicitly_wait(3)
        self.driver.find_element(*self.smart_button).click()


    def verification_smart_button(self):
        return self.driver.find_element(*self.modal_driver).is_displayed()






















