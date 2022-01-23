from lib.page import MainPage
from lib.constants import Locators
import time


# проверяем ссылки в хедере, кроме поиска
def test_links_header_other_than_search(chrome):
    page = MainPage(chrome)
    page.go_to_site()
    main_page = page.wait_of_element_located(Locators.MAIN_TEXT)
    assert main_page.text == Locators.TITLE_TXT

    for dict_window_key in Locators.DICT_WINDOWS:
        tag_name = Locators.DICT_WINDOWS[dict_window_key]
        page.act_first(tag_name)
        time.sleep(2)
        page.handle()
        url = page.chrome.current_url
        assert (Locators.ASRT[0] in url) or (Locators.ASRT[1] in url) or (Locators.ASRT[2] in url) or (
                Locators.ASRT[3] in url) or (Locators.ASRT[4] in url)
        page.close_last_tab()

# pytest tests/test_b_menu_site_without_search.py --tb=short -s -v
