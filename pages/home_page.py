from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators
from locators.base_page_locators import BasePageLocators
from selenium.webdriver.common.by import By
import allure

class HomePage(BasePage):

    @allure.step('Клик по кнопке "Заказать" в шапке или внизу страницы')
    def click_order_button(self, entry_point):
        # Вынес метод клика по кнопке "Заказать" в шапке в класс BasePage. 
        # Или вообще не нужно совмещать клик по этим кнопкам в классе HomePage, 
        # а логику выбора точки входа выносить в тест?
        if entry_point == 'top':
            self.click_header_order_button()
        elif entry_point == 'bottom':
            self.scroll_to_element(HomePageLocators.HOME_FINISH_ORDER_BUTTON)
            self.click_element_with_wait(HomePageLocators.HOME_FINISH_ORDER_BUTTON)

    @allure.step('Клик по вопросу в FAQ')
    def click_faq_question(self, question_index):
        self.click_element_with_wait((By.ID, f'accordion__heading-{question_index}'))

    @allure.step('Получение текста ответа на вопрос в FAQ')
    def get_faq_answer_text(self, question_index):
        return self.get_element_text((By.XPATH, f'//div[@id="accordion__panel-{question_index}"]/p'))
