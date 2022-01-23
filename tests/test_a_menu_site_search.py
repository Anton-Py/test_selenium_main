from selenium.webdriver.common.by import By
from lib.page import MainPage
from lib.constants import Locators
import time

# проверяем поиск на сайте, по одному продукту
def test_site_search(chrome):
    page = MainPage(chrome)
    page.go_to_site()
    page.wait_of_element_located(Locators.HEADER_SEARCH).click()
    page.wait_of_element_located(Locators.ENTRY_FIELD).send_keys(Locators.TEXT_SEARCH)
    page.act_first(Locators.SEARCH)
    page.handle()
    time.sleep(2)
    body_text = page.chrome.find_element(By.TAG_NAME, 'body').text
    assert Locators.PAGE_SORCE_ONE in body_text, "страница не соответствует запросу"
    page.close_last_tab()

# pytest tests/test_a_menu_site_search.py --tb=short -s