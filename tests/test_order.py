import pytest
import allure
from data import Data
from pages.home_page import HomePage
from pages.order_page import OrderPage

class TestOrder:

    @allure.title('Проверка успешного оформления заказа самоката')
    @allure.description('Нажимаем кнопку «Заказать» в шапке или внизу главной страницы. Заполняем форму заказа. Проверяем, что появилось всплывающее окно с сообщением об успешном создании заказа')
    # Параметризация теста: точка входа (кнопка "Заказать") и набор данных для заказа
    @pytest.mark.parametrize("entry_point, order_data", [
            ('top', Data.TEST_ORDER_1),
            ('bottom', Data.TEST_ORDER_2)
        ])
    def test_order_placement_order_successfully_placed(self, main_page, entry_point, order_data):
        driver = main_page
        home_page = HomePage(driver)
        order_page = OrderPage(driver)
        home_page.click_order_button(entry_point)
        order_page.fill_form_user_data(order_data)
        order_page.fill_form_about_rent(order_data)
        order_page.confirm_order()
        order_success_form = order_page.order_success_form_is_visible()

        assert order_success_form
