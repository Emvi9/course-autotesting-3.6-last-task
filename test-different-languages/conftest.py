import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])


def pytest_addoption(parser):
    parser.addoption('--language', default='ru', action='store', help='Choose your language: es / fr')


@pytest.fixture(scope='class')
def browser(request):
    browser_lang = request.config.getoption('language')
    browser = webdriver.Chrome(options=options)
    browser.get(f'http://selenium1py.pythonanywhere.com/{browser_lang}/catalogue/coders-at-work_207/')
    yield browser
    browser.quit()
