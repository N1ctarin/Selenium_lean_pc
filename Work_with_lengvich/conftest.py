import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose browser: es or ru")


@pytest.fixture(scope="function")
def browser(request):
    browser_language = request.config.getoption("language")
    browser = None
    if browser_language == "es":
        print("\nstart es browser for test..")
        browser = webdriver.Chrome()
    elif browser_language == "ru":
        print("\nstart ru browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()