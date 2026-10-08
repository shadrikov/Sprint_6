import pytest
import allure
from data import Data
from pages.home_page import HomePage
from locators.home_page_locators import HomePageLocators

class TestFAQ:

    @allure.title('Проверка раскрытия текста ответа при клике на вопрос в блоке "Вопросы о важном"')
    @allure.description('На главной странице ищем блок "Вопросы о важном", кликаем по каждому вопросу в блоке и после раскрытия ответа проверяем текст ответа на соответствие требуемому ответу')
    # Параметризация теста: индекс вопроса/ответа и ожидаемый текст ответа
    @pytest.mark.parametrize("question_index, answer_text", [
            (0, Data.TEXT_FAQ_ANSWER_0),
            (1, Data.TEXT_FAQ_ANSWER_1),
            (2, Data.TEXT_FAQ_ANSWER_2),
            (3, Data.TEXT_FAQ_ANSWER_3),
            (4, Data.TEXT_FAQ_ANSWER_4),
            (5, Data.TEXT_FAQ_ANSWER_5),
            (6, Data.TEXT_FAQ_ANSWER_6),
            (7, Data.TEXT_FAQ_ANSWER_7)
        ])
    def test_faq_dropdown_answers_text_is_correct(self, main_page, question_index, answer_text):
        driver = main_page
        home_page = HomePage(driver)
        home_page.scroll_to_element(HomePageLocators.FAQ_AREA)
        home_page.click_faq_question(question_index)
        text = home_page.get_faq_answer_text(question_index)

        assert text == answer_text
