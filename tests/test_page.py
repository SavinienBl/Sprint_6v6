from locators.page_locators import AccordionLocators
import allure
import pytest
from tests.data import *


class TestFAQPage:
    @allure.title('Проверка раздела Вопросы о важном')
    @allure.description('Проверка появления  текста ответа при нажатии на каждый из вопросов')
    @pytest.mark.parametrize('question, answer, expecteds',[
        (AccordionLocators.ACCORDION_QUESTION_1, AccordionLocators.ACCORDION_ANSWER_1,expected['text1']),
        (AccordionLocators.ACCORDION_QUESTION_2, AccordionLocators.ACCORDION_ANSWER_2,expected['text2']),
        (AccordionLocators.ACCORDION_QUESTION_3, AccordionLocators.ACCORDION_ANSWER_3,expected['text3']),
        (AccordionLocators.ACCORDION_QUESTION_4, AccordionLocators.ACCORDION_ANSWER_4,expected['text4']),
        (AccordionLocators.ACCORDION_QUESTION_5, AccordionLocators.ACCORDION_ANSWER_5,expected['text5']),
        (AccordionLocators.ACCORDION_QUESTION_6, AccordionLocators.ACCORDION_ANSWER_6,expected['text6']),
        (AccordionLocators.ACCORDION_QUESTION_7, AccordionLocators.ACCORDION_ANSWER_7,expected['text7']),
        (AccordionLocators.ACCORDION_QUESTION_8, AccordionLocators.ACCORDION_ANSWER_8,expected['text8'])
        ])

    def test_click_show_answer(self,driver,home_page,question, answer, expecteds):
        home_page.scrolling_to_faq()
        home_page.click_to_the_question(question)
        a = home_page.get_the_answer_text(answer)
        assert a == expecteds

    @allure.title('Проверка нажатия на лого Яндекс')
    def test_open_dzen(self, driver, home_page):
        home_page.click_open_dzen()
        assert driver.current_url == DZEN_URL

    @allure.title('Проверка нажатия на лого Самокат')
    def test_open_scooter(self, driver, home_page):
        home_page.click_open_scooter()
        assert driver.current_url == SCOOTER_URL
