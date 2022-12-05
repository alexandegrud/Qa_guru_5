from selene.support.shared import browser
import pytest

@pytest.fixture()
def practice_form_open_browser():
    browser.config.hold_browser_open = True
    browser.open('https://demoqa.com/automation-practice-form').driver.maximize_window()

    yield
    browser.close()
