from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BasePageLocators
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step('Получение элемента с ожиданием его видимости')
    def find_element_with_wait(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step('Клик по элементу, когда он становится кликабельным')
    def click_element_with_wait(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step('Проверка, что открыт нужный URL')
    def is_url_opened(self, url):
        try:
            self.wait.until(EC.url_to_be(url))
            return True
        except TimeoutException:
            return False 

    @allure.step('Получение текста элемента')
    def get_element_text(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step('Передача текста в поле')
    def input_text(self, locator, text):
        return self.find_element_with_wait(locator).send_keys(text)

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Получение набора элементов с ожиданием их видимости')
    def find_elements_with_wait(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    @allure.step('Клик по логотипу "Яндекс"')
    def click_yandex_logo(self):
        self.click_element_with_wait(BasePageLocators.YANDEX_LOGO)

    @allure.step('Клик по логотипу "Самокат"')
    def click_scooter_logo(self):
        self.click_element_with_wait(BasePageLocators.SCOOTER_LOGO)

    @allure.step('Переход в последнюю открытую вкладку браузера с проверкой url')
    def switch_to_new_tab(self, url):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        return self.wait.until(EC.url_contains(url))

    @allure.step('Клик по кнопке "Заказать" в шапке')
    def click_header_order_button(self):
        self.click_element_with_wait(BasePageLocators.HEADER_ORDER_BUTTON)