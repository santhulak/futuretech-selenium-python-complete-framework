import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.config import BASE_URL
from utils.screenshot import capture_screenshot

@pytest.fixture
def driver(request):
    options = Options()
    options.add_argument("--window-size=1440,900")
    browser = webdriver.Chrome(options=options)
    browser.get(BASE_URL)
    browser.implicitly_wait(0)
    yield browser
    if getattr(request.node, "rep_call", None) and request.node.rep_call.failed:
        capture_screenshot(browser, request.node.name)
    browser.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
