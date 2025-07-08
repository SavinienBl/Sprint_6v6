import pytest
import sys
import os
from selenium import webdriver
from data import URL
from page.faq_page import FaqPage
from page.order_page import OrderPage

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.get(URL)
    yield driver
    driver.quit()

@pytest.fixture
def home_page(driver):
    home_page = FaqPage(driver)
    return home_page

@pytest.fixture
def order_page(driver):
    order_page = OrderPage(driver)
    return order_page
