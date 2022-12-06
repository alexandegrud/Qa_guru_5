from selene.support.shared import browser
import pytest

@pytest.fixture()
def practice_form_open_browser():
    browser.config.hold_browser_open = True
    browser.config.base_url = "https://demoqa.com"
    browser.config.window_width = 1080
    browser.config.window_height = 1920

    yield
    browser.close()
