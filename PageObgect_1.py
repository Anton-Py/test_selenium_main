from BaseApp import BasePage
from constants import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


class MovaviLocators:
    LOCATOR_HAD_SEARCH = HEADER_SEARCH
    LOCATOR_ENTR_FIRLD = ENTRY_FIELD
    LOCATOR_SEARCH = SEARCH
    LOCATOR_MN_PAGE = MAIN_TEXT
    LOCATOR_UI = LOC_UI


class MainPage(BasePage):

    def act_first(self, tag_name):
        element = self.wait_of_element_located(tag_name)
        ActionChains(self.chrome) \
            .move_to_element(element) \
            .key_down(Keys.CONTROL) \
            .click(element) \
            .key_up(Keys.CONTROL) \
            .perform()

    def act_second(self):
        element = self.wait_of_element_located(MovaviLocators.LOCATOR_SEARCH)
        ActionChains(self.chrome) \
            .move_to_element(element) \
            .key_down(Keys.CONTROL) \
            .click(element) \
            .key_up(Keys.CONTROL) \
            .perform()

    def handle(self):
        default_handle = self.chrome.window_handles
        self.chrome.switch_to.window(default_handle[1])
        return default_handle

    # Проверяем ссылки в хедере, кроме поиска
    def test_main_page(self):
        main_page = self.wait_of_element_located(MovaviLocators.LOCATOR_MN_PAGE)
        assert main_page.text == TITLE_TXT
        for dict_window_key in DICT_WINDOWS:
            tag_name = DICT_WINDOWS[dict_window_key]
            self.act_first(tag_name)
            self.handle()
            url = self.chrome.current_url
            assert (ASRT[0] in url) or (ASRT[1] in url) or (ASRT[2] in url) or (ASRT[3] in url) or (ASRT[4] in url)
            self.chrome.switch_to.window(self.handle()[0])
            default_handle = self.chrome.current_window_handle
            handles = list(self.chrome.window_handles)
            assert len(handles) > 1
            handles.remove(default_handle)
            assert len(handles) > 0
            self.chrome.switch_to_window(handles[0])
            self.chrome.close()
            self.chrome.switch_to_window(default_handle)

    # Проверяем кнопку поиска в хедере
    def site_search(self):
        element = self.wait_of_element_located(MovaviLocators.LOCATOR_HAD_SEARCH)
        element.click()
        entry = self.wait_of_element_located(MovaviLocators.LOCATOR_ENTR_FIRLD)
        entry.send_keys(TEXT_SEARCH)
        self.act_second()
        self.handle()
        time.sleep(3)
        body_text = self.chrome.find_element_by_tag_name('body').text
        assert (PAGE_SORCE_ONE and PAGE_SORCE_TWO) in body_text, "страница не соответствует запросу"
        self.chrome.switch_to.window(self.handle()[0])
        default_handle = self.chrome.current_window_handle
        handles = list(self.chrome.window_handles)
        assert len(handles) > 1
        handles.remove(default_handle)
        assert len(handles) > 0
        self.chrome.switch_to_window(handles[0])
        self.chrome.close()
        self.chrome.switch_to_window(default_handle)

    def main_ui(self):
        ui = self.wait_of_element_located(MovaviLocators.LOCATOR_UI).click()
        time.sleep(2)

        self.act_second()
        # find_element_by_partial_link_text(constants.MENU_VIDEO_ITEM).click()
