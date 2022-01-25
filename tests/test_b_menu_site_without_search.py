from lib.page import MainPage
from lib.constants import Locators
import time


# проверяем ссылки в хедере, кроме поиска
def test_links_header_other_than_search(chrome):
    page = MainPage(chrome)
    page.go_to_site()
    main_title_element = page.wait_of_element_located(Locators.MAIN_TEXT)
    assert main_title_element.text == Locators.TITLE_TEXT

    for dict_window_key in Locators.DICT_WINDOWS:
        tag_name = Locators.DICT_WINDOWS[dict_window_key]
        page.tap_tag(tag_name)
        time.sleep(2)
        page.switch_to_second_tab()
        url = page.chrome.current_url
        assert Locators.HEADER_TOP_SIDEBAR_LINKS[dict_window_key] in url
        page.close_last_tab()

# pytest tests/test_b_menu_site_without_search.py --tb=short -s -v
