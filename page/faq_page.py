import allure
from page.general_page import QuestionPage
from page.order_page import OrderPage
from locators.page_locators import AccordionLocators
from locators.order_locators import *

class FaqPage(QuestionPage):

    @allure.step('Скроллинг до раздела вопросов')
    def scrolling_to_faq(self):
        self.scrolling(AccordionLocators.ACCORDION)
        self.find_element_with_wait(AccordionLocators.ACCORDION)

    @allure.step('Клик на вопрос')
    def click_to_the_question(self,question):
        self.find_element_with_wait(question)
        self.click(question)

    @allure.step('Получение текста ответа')
    def get_the_answer_text(self,answer):
        self.find_element_with_wait(answer)
        a = self.get_text_on_element(answer)
        return a
