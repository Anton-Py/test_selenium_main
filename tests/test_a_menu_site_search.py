from lib.page import MainPage
from lib.constants import Locators
import time

# проверяем поиск на сайте, по одному продукту
def test_site_search(chrome):
    page = MainPage(chrome)
    page.go_to_site()
    page.wait_of_element_located(Locators.HEADER_SEARCH).click()
    page.wait_of_element_located(Locators.ENTRY_FIELD).send_keys(Locators.TEXT_SEARCH)
    page.tap_tag(Locators.SEARCH)
    page.switch_to_second_tab()
    time.sleep(2)
    main_body_text = page.wait_of_element_located_tag_name('body').text
    assert Locators.SEARCH_RESULT_TEXT in main_body_text, "страница не соответствует запросу"
    page.close_last_tab()

# pytest tests/test_a_menu_site_search.py --tb=short -s