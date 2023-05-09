import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="firefox", help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None, help="Choose language: '--language=ru' or '--language=en' or '--language=es'"
                                                                      "or '--language=fr' or '--language=cs' or '--language=sk'")

#декоратор
@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None

    # Объявление нужного языка для Chrome
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    # Объявление нужного языка для Firefox
    options_firefox = OptionsFirefox()
    options_firefox.set_preference("intl.accept_languages", user_language)

    if browser_name == "chrome":
        print("\nstart browser chrome for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart browser firefox for test..")
        browser = webdriver.Firefox(options=options_firefox)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    # Финализатор, фикстура продолжает выполнение после прохождения теста
    yield browser
    print("\nquit browser")
    browser.quit()