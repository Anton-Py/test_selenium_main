from BaseApp import BasePage
from constants import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


class MovaviLocators:
    LOCATOR_HAD_SEARCH = header_search
    LOCATOR_ENTR_FIRLD = entry_field
    LOCATOR_SEARCH = search
    LOCATOR_MN_PAGE = main_text
    LOCATOR_UI = loc_ui


class MainPage(BasePage):

    def act_first(self, tag_name):
        element = self.chrome.find_element(By.TAG_NAME, tag_name)
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

    # Проверяем ссылки в хедере, кроме поиска
    def test_main_page(self):
        main_page = self.wait_of_element_located(MovaviLocators.LOCATOR_MN_PAGE)
        assert main_page.text == title_txt
        for dict_window_key in dict_windows:
            tag_name = dict_windows[dict_window_key]
            self.act_first(tag_name)
            default_handle = self.chrome.window_handles
            self.chrome.switch_to.window(default_handle[1])  # Преключаемся на вторую вкладку
            url = self.chrome.current_url
            assert (asrt[0] in url) or (asrt[1] in url) or (asrt[2] in url) or (asrt[3] in url) or (asrt[4] in url)
            self.chrome.switch_to.window(default_handle[0])
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
        entry.send_keys(text_search)
        self.act_second()
        default_handle = self.chrome.window_handles
        self.chrome.switch_to.window(default_handle[1])
        time.sleep(3)
        body_text = self.chrome.find_element_by_tag_name('body').text
        assert (page_source_one and page_source_two) in body_text, "страница не соответствует запросу"
        self.chrome.switch_to.window(default_handle[0])
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
