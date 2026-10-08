from selenium.webdriver.common.by import By

class OrderPageLocators:

    NAME_FIELD = [By.XPATH, '//input[contains(@placeholder, "Имя")]'] # Поле ввода "Имя"

    SURNAME_FIELD = [By.XPATH, '//input[contains(@placeholder, "Фамилия")]'] # Поле ввода "Фамилия"

    ADDRESS_FIELD = [By.XPATH, '//input[contains(@placeholder, "Адрес")]'] # Поле ввода "Адрес"

    SUBWAY_FIELD = [By.CLASS_NAME, 'select-search__input'] # Поле выбора станции метро

    SUBWAY_STATION_LIST_OPTION = [By.XPATH, '//button[contains(@class, "Order_SelectOption")]'] # Первая станция метро в выпадающем списке

    PHONE_NUMBER_FIELD = [By.XPATH, '//input[contains(@placeholder, "Телефон")]'] # Поле ввода "Телефон"

    ORDER_NEXT_BUTTON = [By.XPATH, '//button[contains(text(), "Далее")]'] # Кнопка "Далее"

    ORDER_HEADER_ABOUT_RENT = [By.XPATH, '//div[contains(@class, "Order_Header")]'] # Загловок "Про аренду"

    DATEPICKER_FIELD = [By.XPATH, '//div[contains(@class, "Order_MixedDatePicker")]//input'] # Поле выбора даты, когда привезти самокат

    RENTAL_PERIOD_DROPDOWN = [By.CLASS_NAME, 'Dropdown-control'] # Поле выбора срока аренды

    RENTAL_PERIOD_DROPDOWN_OPTION = [By.CLASS_NAME, 'Dropdown-option'] # Варианты из выпадающего списка срока аренды

    SELECTED_PERIOD_ONE_DAY = [By.XPATH, '//div[contains(@class, "Dropdown-option") and contains(text(), "сутки")]'] # Вариант "Сутки" в выпадающем списке

    SELECTED_PERIOD_SEVEN_DAYS = [By.XPATH, '//div[contains(@class, "Dropdown-option") and contains(text(), "семеро суток")]'] # Вариант "Семеро суток" в выпадающем списке

    SCOOTER_COLOR_BLACK_CHECKBOX = [By.CSS_SELECTOR, 'label[for="black"]'] # Чекбокс "черный жемчуг" для выбора цвета самоката

    SCOOTER_COLOR_GREY_CHECKBOX = [By.CSS_SELECTOR, 'label[for="grey"]'] # # Чекбокс "серая безысходность" для выбора цвета самоката

    COMMENT_FOR_COURIER_FIELD = [By.XPATH, '//input[contains(@placeholder, "Комментарий для курьера")]'] # Поле ввода "Комментарий для курьера"

    ORDER_BUTTON = [By.XPATH, '//div[contains(@class, "Order_Buttons")]/button[contains(text(), "Заказать")]'] # Кнопка "Заказать" после формы "Про аренду"

    CONFIRM_BUTTON = [By.XPATH, '//div[contains(@class, "Order_Buttons")]/button[contains(text(), "Да")]'] # Кнопка "Да" в форме подтверждения заказа

    SUCCESS_ORDER_HEADER = [By.XPATH, '//div[contains(@class, "Order_ModalHeader") and contains(text(), "Заказ оформлен")]'] # Заголовок формы об успешном оформлении заказа