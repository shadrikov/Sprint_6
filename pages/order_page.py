from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
import allure

class OrderPage(BasePage):

    @allure.step('Выбор станции метро')
    def select_subway_station(self, order_data):
        self.input_text(OrderPageLocators.SUBWAY_FIELD, order_data["subway_station"])
        self.click_element_with_wait(OrderPageLocators.SUBWAY_STATION_LIST_OPTION)
    
    @allure.step('Выбор срока аренды')
    def select_rental_period(self, order_data):
        self.click_element_with_wait(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        rental_period_options = self.find_elements_with_wait(OrderPageLocators.RENTAL_PERIOD_DROPDOWN_OPTION)
        for option in rental_period_options:
            if order_data["rental_period"] in option.text:
                option.click()
                break

    @allure.step('Выбор цвета самоката')
    def select_scooter_color(self, order_data):
        if order_data.get("color"):
            if order_data["color"] == "black":
                self.click_element_with_wait(OrderPageLocators.SCOOTER_COLOR_BLACK_CHECKBOX)
            elif order_data["color"] == "grey":
                self.click_element_with_wait(OrderPageLocators.SCOOTER_COLOR_GREY_CHECKBOX)

    @allure.step('Заполнение полей формы "Для кого самокат"')
    def fill_form_user_data(self, order_data):
        self.input_text(OrderPageLocators.NAME_FIELD, order_data["name"])
        self.input_text(OrderPageLocators.SURNAME_FIELD, order_data["surname"])
        self.input_text(OrderPageLocators.ADDRESS_FIELD, order_data["address"])
        self.select_subway_station(order_data)
        self.input_text(OrderPageLocators.PHONE_NUMBER_FIELD, order_data["phone_number"])
        self.click_element_with_wait(OrderPageLocators.ORDER_NEXT_BUTTON)

    @allure.step('Заполнение полей формы "Про аренду"')
    def fill_form_about_rent(self, order_data):
        self.input_text(OrderPageLocators.DATEPICKER_FIELD, order_data["date"])
        self.click_element_with_wait(OrderPageLocators.ORDER_HEADER_ABOUT_RENT)
        self.select_rental_period(order_data)
        self.select_scooter_color(order_data)
        if order_data.get("comment"):
            self.input_text(OrderPageLocators.COMMENT_FOR_COURIER_FIELD, order_data["comment"])
        self.click_element_with_wait(OrderPageLocators.ORDER_BUTTON)

    @allure.step('Подтверждение оформления заказа')
    def confirm_order(self):
        self.click_element_with_wait(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step('Появление формы "Заказ оформлен"')
    def order_success_form_is_visible(self):
        return self.find_element_with_wait(OrderPageLocators.SUCCESS_ORDER_HEADER)