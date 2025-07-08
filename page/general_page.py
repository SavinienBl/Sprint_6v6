import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_locators import Orderlocators
from tests.data import *



class QuestionPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Найти элемент с ожиданием')
    def find_element_with_wait(self,locator):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Проскролить до раздела ')
    def scrolling(self,locator):
        x = self.find_element_with_wait(locator)
        self.driver.execute_script('arguments[0].scrollIntoView();',x )

    @allure.step('Клик ')
    def click(self,locator):
        x = self.find_element_with_wait(locator)
        x.click()

    @allure.step('Получаем текст')
    def get_text_on_element(self,locator):
        x = self.find_element_with_wait(locator)
        return x.text

    @allure.step('Ввести значение в поле ввода')
    def input_text(self,locator,text):
        e = self.find_element_with_wait(locator)
        e.send_keys(text)

    @allure.step('Клик на кнопку заказа 1 ')
    def click_order_button_1(self):
        self.find_element_with_wait(Orderlocators.COOKIE)
        self.click(Orderlocators.COOKIE)
        self.find_element_with_wait(Orderlocators.ORDER)
        self.click(Orderlocators.ORDER)
        self.find_element_with_wait(Orderlocators.NEXT_BUTTON)
        self.click(Orderlocators. NEXT_BUTTON)

    @allure.step('Отображение элемента')
    def displaying_of_element(self,locator):
        return self.find_element_with_wait(locator)

    @allure.step('Клик на кнопку заказа 2 ')
    def click_order_button_2(self):
        self.find_element_with_wait(Orderlocators.COOKIE)
        self.click(Orderlocators.COOKIE)
        self.find_element_with_wait(Orderlocators.ORDER_2 )
        self.click(Orderlocators.ORDER_2)
        self.find_element_with_wait(Orderlocators.NEXT_BUTTON)
        self.click(Orderlocators.NEXT_BUTTON)

    @allure.step('Ожидаем урл')
    def wait_url(self, url):
        return WebDriverWait(self.driver, 6).until((expected_conditions.url_to_be(url)))

    @allure.step('Перейти на другую вкладку')
    def switch_to_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Переходим на страницу дзена')
    def click_open_dzen(self):
        self.find_element_with_wait(Orderlocators.YANDEX)
        self.click(Orderlocators.YANDEX)
        self.switch_to_next_tab()
        self.wait_url(DZEN_URL)

    def click_open_scooter(self):
        self.find_element_with_wait(Orderlocators.ORDER)
        self.click(Orderlocators.ORDER)
        self.find_element_with_wait(Orderlocators.SCOOTER)
        self.click(Orderlocators.SCOOTER)
        self.wait_url(SCOOTER_URL)