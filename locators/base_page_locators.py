from selenium.webdriver.common.by import By

class BasePageLocators:

    HEADER_ORDER_BUTTON = [By.XPATH, '//div[contains(@class, "Header_Nav")]/button[text()="Заказать"]'] # Кнопка "Заказать" вверху страницы

    YANDEX_LOGO = [By.XPATH, '//a[contains(@class, "Header_LogoYandex")]'] # Логотип "Яндекс" вверху страницы

    SCOOTER_LOGO = [By.XPATH, '//a[contains(@class, "Header_LogoScooter")]'] # Логотип "Самокат" вверху страницы


    

