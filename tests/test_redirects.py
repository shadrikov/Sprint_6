import allure
from pages.base_page import BasePage
from urls import URLs

class TestRedirects:

    @allure.title('Проверка перехода на главную страницу по клику на логотип "Самокат" в шапке')
    @allure.description('Открываем страницу создания заказа. Кликаем на логотип "Самокат" в шапке и проверяем, что произошёл редирект на главную страницу Яндекс.Самокат')
    def test_redirect_to_home_page_by_click_on_scooter_logo(self, driver):
        base_page = BasePage(driver)
        base_page.driver.get(URLs.ORDER_PAGE_URL)
        base_page.click_scooter_logo()

        assert base_page.is_url_opened(URLs.HOME_PAGE_URL)

    @allure.title('Проверка перехода на страницу Дзена по клику на логотип "Яндекс" в шапке')
    @allure.description('Открываем главную страницу. Кликаем на логотип "Яндекс" в шапке и проверяем, что в новой вкладке браузера открылась страница Дзена')
    def test_redirect_to_dzen_page_in_new_tab_by_click_on_yandex_logo(self, main_page):
        driver = main_page
        base_page = BasePage(driver)
        base_page.click_yandex_logo()
        dzen_is_open = base_page.switch_to_new_tab(URLs.DZEN_URL)

        assert dzen_is_open