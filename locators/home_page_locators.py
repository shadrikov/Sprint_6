from selenium.webdriver.common.by import By

class HomePageLocators:

    FAQ_AREA = [By.CLASS_NAME, 'accordion'] # Область с вопросами/ответами FAQ

    HOME_FINISH_ORDER_BUTTON = [By.XPATH, '//div[contains(@class, "Home_FinishButton")]/button[text()="Заказать"]'] # Кнопка «Заказать» внизу страницы
