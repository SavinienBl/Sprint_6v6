import allure
from page.general_page import QuestionPage
from locators.order_locators import Orderlocators
from selenium.webdriver.common.by import By
class OrderPage(QuestionPage):


    @allure.step('Заполняем Имя')
    def name(self,name):
        self.input_text(Orderlocators.NAME,name)
        return self

    @allure.step('Заполняем Фамилию')
    def surname(self,surname):
        self.input_text(Orderlocators. SURNAME, surname)
        return self

    @allure.step('Заполняем Адресс куда привезти ')
    def addres(self, addres):
        self.input_text(Orderlocators. ADDRES, addres)
        return self

    @allure.step('Заполняем станцию метро  ')
    def metro(self, metro ):
        self.click(Orderlocators.STATION)
        self.click(Orderlocators.SELECTED_STATION)
        return self

    @allure.step('Заполняем телефон')
    def telephone_number(self,number):
        self.input_text(Orderlocators.NUMBER, number)
        return self

    @allure.step('Нажимаем на кнопку Далее')
    def next(self):
        self.scrolling(Orderlocators.NEXT_BUTTON)
        self.click(Orderlocators.NEXT_BUTTON)

    @allure.step('Ввести дату заказа в Когда привезти самокат ')
    def date_of_delivery(self,date):
        self.input_text(Orderlocators.DATE_OF_DELIVERY, date)

    @allure.step('Указать срок аренды')
    def rental_period(self):
        self.click(Orderlocators.RENTAL_PERIOD)
        self.click(Orderlocators.DROPDOWN_RENTAL_PERIOD)

    @allure.step('Указать срок аренды')
    def check_box(self):
        self.click(Orderlocators.CHECKBOX_GREY)

    @allure.step('Добавить комментарий')
    def comment(self,comment):
        self.input_text(Orderlocators.DATE_OF_DELIVERY,comment)

    @allure.step('Нажать на Заказать')
    def order_footer(self):
        self.click(Orderlocators.MAKE_ORDER)

    @allure.step('Нажать на кнопку Да')
    def yes_button(self):
        self.click(Orderlocators.YES)

    @allure.step('Отображение кнопки Посмотреть статус')
    def status_box(self):
        return self.displaying_of_element(Orderlocators.STATUS)


    @allure.step('Первый этап заказа')
    def first_step_of_the_order(self,name,surname,addres,metro,number):
        self.name(name)
        self.surname(surname)
        self.addres(addres)
        self.metro(metro)
        self.telephone_number(number)
        self.next()

    @allure.step('Второй этап заказа')
    def second_step_of_the_order(self, date,comment):
        self.date_of_delivery(date)
        self.rental_period()
        self.check_box()
        self.comment(comment)
        self.order_footer()
        self.yes_button()