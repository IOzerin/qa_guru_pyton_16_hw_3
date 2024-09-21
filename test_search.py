from selene import browser, be, have

def test_search(setting_browser):
    browser.open('https://www.ecosia.org')
    browser.element('[name="q"]').should(be.blank).type('rkgfdhjkljhdf').press_enter()
    browser.element('[data-test-id="layout-content"]').should(have.text('Unfortunately we didn’t find any results'))


