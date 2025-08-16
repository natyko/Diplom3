from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопка "Личный кабинет" на главной
    PROFILE_BUTTON = By.XPATH, "//a[@href = '/account']"
    # Ссылка на конструктор в личном кабинете
    CONSTRUCTOR_LINK = (By.XPATH, '//a[@class="AppHeader_header__link__3D_hX AppHeader_header__link_active__1IkJo"]')
    ORDER_FEED_LINK = By.XPATH, '//a[@href="/feed"]'

    # Лента заказов
    FIRST_ORDER_IN_FEED = By.XPATH, '//ul[@class="OrderFeed_list__OLh59"]/li[1]'
    ORDER_INFO = By.XPATH, '//div[@class="Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10"]'
    ORDER_FEED_HEADER = By.XPATH, '//h1[text()="Лента заказов"]'
    MY_ORDER_IN_ORDER_FEED = By.XPATH, '//p[text()="#0218482"]'
    ORDERS_FOR_ALL_TIME = By.XPATH, '//div[@class="undefined mb-15"]/p[2]'
    ORDERS_FOR_TODAY = By.XPATH, '//div[@class="OrderFeed_ordersData__1L6Iv"]/div[3]/p[2]'
    ORDER_IN_PROCESS_IN_FEED = By.XPATH, '//div/ul[2]/li[contains(@class,"text_type_digits-default")]'
    ORDER_IN_MODAL_WINDOW = By.XPATH, '//h2[@class="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]'

    CRATER_BUN = By.XPATH, "//img[@alt='Краторная булка N-200i']"
    CLOSE_MODAL_WINDOW_BUTTON = By.XPATH, '//button/*[name()="svg"]'
    BURGER_INGREDIENTS = By.XPATH, '//ul[@class="BurgerConstructor_basket__list__l9dp_"]'
    BUN_COUNTER = By.XPATH, '//p[text()="2"]'
    ORDER_ID = By.XPATH, '//p[text()="идентификатор заказа"]'
    BUTTON_MAKE_ORDER = By.XPATH, '//button[text()="Оформить заказ"]'
    EXTRA_ORDER_MODAL_WINDOW = By.CLASS_NAME, "Modal_modal__loading__3534A"

    SAUCES_LINK = (By.XPATH, "//span[text() = 'Соусы']")
    BUNS_LINK = (By.XPATH, "//span[text() = 'Булки']")
    FILLINGS_LINK = (By.XPATH, "//span[text() = 'Начинки']")