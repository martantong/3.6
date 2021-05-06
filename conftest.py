import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en-gb', help="Choose language")


@pytest.fixture(scope="function")
def option_lang(request):
    return request.config.getoption("language")


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(3)
    yield browser
    browser.quit()
