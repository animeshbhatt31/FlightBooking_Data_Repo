
import pytest
from playwright.sync_api import Playwright
def pytest_addoption(parser):
    parser.addoption("--browser_name",action="store", default="chromium",
      help="run tests",choices=["chromium","firefox","webkit"])


@pytest.fixture(scope="session")
def browser_instance(playwright: Playwright,request):
    print("BROWSER LAUNCH")
    select_browser_name=request.config.getoption("--browser_name")
    browser_type=getattr(playwright,select_browser_name)
    browser=browser_type.launch(headless=False)
    yield browser
    print("BROWSER CLOSE")
    browser.close()


@pytest.fixture(scope="function")
def page_instance(browser_instance):

    context = browser_instance.new_context()
    page = context.new_page()

    yield page
    context.close()
