import pytest
import time
from selenium import webdriver


def test_add_to_cart_button_is_displayed(browser, option_lang):
    browser.get(f"http://selenium1py.pythonanywhere.com/{option_lang}/catalogue/coders-at-work_207/")
    add_to_cart_button = browser.find_element_by_css_selector(".btn-add-to-basket"), "Add button is not displayed"
    assert add_to_cart_button is not None
