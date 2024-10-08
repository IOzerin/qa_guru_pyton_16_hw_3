import pytest
from selene import browser


@pytest.fixture(scope="session")
def setting_browser():
    browser.config.window_height = 720
    browser.config.window_width = 1280

    yield

    browser.quit()
